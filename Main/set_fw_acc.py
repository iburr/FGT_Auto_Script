from netmiko import ConnectHandler
from typing import Dict, List
import time as t

# Test connections for the devices in question
# Format: {"host": "IP", "username": "username", "password": "password"}
# Following script should not conflict with port binds if enabled via gui access
# Can test this in local enviorments of course.

Devices: List[Dict] = [
    {"host": "192.168.30.1", "username": "admin", "password": "admin"},
    {"host": "172.17.77.1", "username": "admin", "password": "admin"},
    # {"host": "Public_IP_addr", "username": "Router_num", "password": "__password__holder"},
    # {"host": "Public_IP_addr", "username": "Router_num", "password": "__password__holder"},
    # {"host": "Public_IP_addr", "username": "Router_num", "password": "__password__holder"},
    # {"host": "Public_IP_addr", "username": "Router_num", "password": "__password__holder"},
    # {"host": "Public_IP_addr", "username": "Router_num", "password": "__password__holder"},
    # {"host": "Public_IP_addr", "username": "Router_num", "password": "__password__holder"},
    # {"host": "Public_IP_addr", "username": "Router_num", "password": "__password__holder"},
    # {"host": "Public_IP_addr", "username": "Router_num", "password": "__password__holder"},
]

set_commands = [
    "config sys admin\n",
    "edit admin1\n", 
    # "set trusthost1 192.168.102.10/28\n",
    # "set trusthost2 10.10.80.1/29\n",
    # "set trusthost3 21.2.14.1/29\n",
]  # Will differ depending on vendor OS


def main():
    for Fortigate in Devices:
        print(f"\n Connecting to {Fortigate['username']} ({Fortigate['host']}) ...")

        # Global config layout
        device = {
            "device_type": "fortinet",  #  device in use ex/ arista_eos, cisco_ios, palo_alto_panos, zyxel_os
            "host": Fortigate["host"],
            "username": "admin",
            "password": Fortigate["password"],
        }

        try:
            with ConnectHandler(**device) as fw:
                print("\n +++++ Connected ++++++ \n")

                for cmd in set_commands:
                    zen = "." * 5
                    print(f"\n {zen}Running command: {cmd}")
                    output = fw.send_config_set(cmd, read_timeout=100)
                    # timeout is set to 100 cause connection is being established over WAN, slower compared to LAN
                    print(f"{output}")
                print(f" Test is finished on {Fortigate['username']}\n")
        except Exception as e:
            print(f"  Failed{e}\n")
        t.sleep(0.5)

    print("All connections have been established")


# Calls Logic first.. Cleaner
if __name__ == "__main__":
    main()
