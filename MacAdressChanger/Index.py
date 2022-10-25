
import Util.MacUtil as MacUtil

(options, arguments) = MacUtil.get_arguments()

interface = options.interface
mac = options.mac

MacUtil.mac_changer(interface, mac)

