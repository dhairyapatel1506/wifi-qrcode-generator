#Import modules
import subprocess
import wifi_qrcode_generator

ssid = input("SSID: ")
 
try:
   
    #Retrieve saved wifi data
    Id = subprocess.check_output(
        ['sudo', 'cat', f"/etc/NetworkManager/system-connections/{ssid}.nmconnection"]).decode('utf-8').split('\n')
     
    pwd = str([b.split("=")[1]
        for b in Id if "psk=" in b])[2:-2]

    print("Password :", pwd)
     
except:
    print("Something's wrong")
     
#Generate QR code
picture = wifi_qrcode_generator.wifi_qrcode(ssid, False, 'WPA', pwd)
picture = picture.save(f"{ssid}.png")
