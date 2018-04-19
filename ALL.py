import getpass
import sys
import telnetlib

HOST=("192.168.68.148","192.168.68.151","192.168.68.150")
user=raw_input("Enter your username:")
password=getpass.getpass()

for i in HOST:
    if i is "192.168.68.148":
        tn=telnetlib.Telnet(HOST[0],timeout=15)
        tn.read_until("Username:")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("conf t\n")
        tn.write("int lo 1\n")
        tn.write("ip add 2.2.2.2 255.255.255.255\n")
        tn.write("end\n")
        tn.write("exit\n")
        print tn.read_all()

    elif i is  "192.168.68.151":
        tn=telnetlib.Telnet(HOST[1],timeout=15)
        tn.read_until("Username: ")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("en\n")
        tn.write("conf t\n")
        tn.write("int lo 1\n")
        tn.write("ip add 2.2.2.2 255.255.255.255\n")
        tn.write("end\n")
        tn.write("exit\n")  
        print tn.read_all()

    elif i is "192.168.68.150":
        tn=telnetlib.Telnet(HOST[2],timeout=15)
        tn.read_until("Username:")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(passwrod + "\n")
        tn.write("configure\n")
        tn.write("set interfaces lo0 unit 0 family inet address 3.3.3.3/32\n" )
        tn.write("commit and-quit\n")
        tn.write("exit\n")
        print tn.read_all()    
        


 
