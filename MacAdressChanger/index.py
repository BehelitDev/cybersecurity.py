


import subprocess

interface = input("Qual a interface? ")
mac = input("Qual o MAC? ")

print("Alterando o Endereço MAC para: " + interface)

subprocess.call(["sudo ifconfig ", interface, " down "])
subprocess.call(["sudo ifconfig ", interface, " hw ether ", mac])
subprocess.call(["sudo ifconfig ", interface, " up "])

print("MAC alterado para: " + mac)