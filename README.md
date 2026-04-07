# FORTIGATE AUTOMATION SCRIPT

# FortiGate ACL Automation with Netmiko

**Python script to automate SSH connections to FortiGate firewalls and apply policy changes. This is a good baseline script that can be used for a multitude of use cases. Like firewall policy creation, Custom interfaces, or disabling features**

This script serves as a **production-ready template** for network engineers who want to safely and efficiently manage outbound access rules or admin trust hosts on multiple FortiGate devices.
This has been tested on F-Series and E-Series Devices, including Firmware OS images supported for 7.2.x - 7.6.x

Is also a good baseline automation script for multiple vendors like Cisco, Aruba, Palo-Alto, and Zyxel.
Script will need to be edited slightly to accommodate different vendors

---

## Features

- Connects to multiple FortiGate firewalls via SSH using **Netmiko**
- Applies configuration commands in bulk using `send_config_set`
- Built with error handling and clear console output
- Easily extensible — add more devices or commands
- Suitable for both **lab/testing** and **production** environments
- Works over WAN connections (increased timeout handling)

---

## What It Does

The script:
1. Iterates through a list of FortiGate devices
2. Establishes an SSH connection to each one
3. Sends a set of configuration commands (currently focused on `config sys admin` → editing admin accounts and trust hosts)
4. Prints real-time output and status for each device
5. Handles connection failures if a connection fails

It is especially useful for quickly updating **outbound ACLs**, trust hosts, or other repetitive CLI configurations across multiple firewalls.

---

## Requirements

- **Python**: 3.9 or higher (tested on 3.11.9 and 3.13)

### Install Dependencies

```bash
pip install netmiko
