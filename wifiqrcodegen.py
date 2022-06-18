#Import modules
import subprocess
import wifi_qrcode_generator

print("Saved Wifi Networks:\n")
savedNetworks = subprocess.check_output(['ls', '/etc/NetworkManager/system-connections/']).decode('utf-8').split("\n")
for savedNetwork in savedNetworks:
    print(f"\t{savedNetwork.split('.')[0]}")

ssid = input("Enter SSID: ")
 
try:
   
    # Retrieve saved wifi data
    Id = subprocess.check_output(
        ['sudo', 'cat', f"/etc/NetworkManager/system-connections/{ssid}.nmconnection"]).decode('utf-8').split('\n')
     
    pwd = str([b.split("=")[1]
        for b in Id if "psk=" in b])[2:-2]

    print("Password :", pwd)
     
except:

    print("Something's wrong")
     
# Generate QR code
picture = wifi_qrcode_generator.wifi_qrcode(ssid, False, 'WPA', pwd)
picture = picture.save(f"{ssid}.png")

print("The QR code was succesfully generated and has been stored in the current directory.")
