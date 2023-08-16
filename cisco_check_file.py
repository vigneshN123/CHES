from netmiko import ConnectHandler
from pprint import pprint
from getpass import getpass
import datetime

user = input("Username: ")
passwd = getpass(prompt = "Password: ")


with open("kimball_switches.txt") as f:
        data = f.read()


d = data.splitlines()

for device in d:
    device_info = {
        'host' : device,
        'username' : user,
        'password' : passwd,
        'device_type' : 'cisco_ios',
        'session_log' : 'kimball_cisco_log.txt',
        'session_log_file_mode' : 'append',
        'fast_cli' : True
        }

    print(f"{datetime.datetime.now()} Connecting to {device}...")
    ssh = ConnectHandler(**device_info)
    print(f"Connection established : {ssh.find_prompt()}")

    x = ssh.find_prompt()
    y =  x.lower()
    y = y.split("-")
    z = y[3].split("#")
    a = z[0]+".txt"
    a = "more"+" "+a

    output = ssh.send_command(a,strip_prompt=False, strip_command=False)
    file1 = open("output.txt", "a")
    file1.write("\n #################################################################################### \n")
    file1.write(output)
    file1.write("\n #################################################################################### \n")
    file1.close()
   
    print(f"Disconnecting from {device}...")
    ssh.disconnect()
    print(f"{datetime.datetime.now()} Disconnected!")
    print()

