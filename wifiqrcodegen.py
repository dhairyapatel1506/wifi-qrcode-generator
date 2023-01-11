#Import modules
import platform
import subprocess
import wifi_qrcode_generator

os = platform.system()

print("Saved Wifi Networks:\n")
if(os=="Linux"):
    # Lists Network names
    savedNetworks = subprocess.check_output(['ls', '/etc/NetworkManager/system-connections/']).decode('utf-8').split("\n")
    for network in savedNetworks:
        print(f"\t{network.split('.nmconnection')[0]}")
    ssid = input("Enter SSID: ")
else:
    savedNetworks = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8').split("\n")
    for network in savedNetworks:
        if("All User Profile" in network):
            print(f"\t{network.split(':')[1]}")
    ssid = input("\nEnter SSID: ")
 
try:
    if(os=="Linux"): 
        # Retrieves Network Profile and extracts Password
        profile = subprocess.check_output(
            ['sudo', 'cat', f"/etc/NetworkManager/system-connections/{ssid}.nmconnection"]).decode('utf-8').split('\n')
         
        pwd = str([b.split("=")[1]
            for b in profile if "psk=" in b])[2:-2]
    else:
        profile = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear']).decode('utf-8').split('\n')

        pwd = str([b.split(':')[1].strip() for b in profile if "Key Content" in b])[2:-2]

    print("Password :", pwd)
     
except:

    print("Something's wrong")
     
# Generates QR code
picture = wifi_qrcode_generator.wifi_qrcode(ssid, False, 'WPA', pwd)
picture = picture.save(f"{ssid}.png")

print("The QR code has been stored in the current directory.")
