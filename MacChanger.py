import subprocess
import optparse
import re


def giris():
    parse = optparse.OptionParser()
    parse.add_option("-i","--interface",dest="interface",help="interface degistirme :)")
    parse.add_option("-m","--mac",dest="mac_adress",help="yeni mac adres")

    return  parse.parse_args()

def mac(inter,mac_adress):
    subprocess.call(["ifconfig",inter,"down"])
    subprocess.call(["ifconfig",inter,"hw","ether",mac_adress])
    subprocess.call(["ifconfig",inter,"up"])

def kontrol(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    Ymac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)

    if Ymac :
        return Ymac.group(0)
    else :
        return None

print("mac changer launched by Devran13")

(userInput,arguments)= giris()
mac(userInput.interface,userInput.mac_adress)
Emac = kontrol(userInput.interface)

if  Emac == userInput.mac_adress:
    print("Your mac address has been successfully changed")
else :
    print("Please correct your mac address and try again.")