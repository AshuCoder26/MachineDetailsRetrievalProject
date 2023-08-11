import socket
import platform
import datetime
import os
import uuid
import subprocess

def get_mac_address():
    try:
        mac = ':'.join(hex(i)[2:].zfill(2) for i in uuid.getnode().to_bytes(6, 'big'))
        return mac
    except Exception as e:
        return "Not available"

def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    except Exception as e:
        return "Not available"

def get_antivirus_info():
    try:
        
        command = 'wmic /namespace:\\\\root\SecurityCenter2 path AntiVirusProduct get displayName /value'
        output = subprocess.check_output(command, shell=True, text=True)
        antivirus_info = ""
        for line in output.split('\n'):
            if line.startswith("displayName"):
                antivirus_info = line.split('=')[1].strip()
                break
        return antivirus_info
    except Exception as e:
        return "Not available"

machine_name = platform.node()
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
ip_address = get_ip_address()
mac_address = get_mac_address()
antivirus_info = get_antivirus_info()

print("Machine Name:", machine_name)
print("IP Address:", ip_address)
print("MAC Address:", mac_address)
print("Current Date and Time:", current_datetime)
print("Antivirus Info:", antivirus_info)
