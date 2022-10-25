import subprocess
import optparse as parser

def get_arguments():
    parserOpt = parser.OptionParser()

    parserOpt.add_option("-i", "--interface", dest = "interface", help = "Interface para o mudar o endereço MAC.")
    parserOpt.add_option("-m", "--mac", dest = "mac", help = "Novo endereço MAC.")

    return parserOpt.parse_args()

def mac_changer(interface, mac):
    print("Alterando o Endereço MAC para: " + interface)

    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

    print("MAC alterado para: " + mac) 