# FGT_Auto_Script

# FortiGate ACL Automation with Netmiko

**A simple yet powerful Python script to automate SSH connections to FortiGate firewalls and apply configuration changes (such as ACL/trusthost updates).**

This script serves as a **production-ready template** for network engineers who want to safely and efficiently manage outbound access rules or admin trust hosts on multiple FortiGate devices.

---

## ✨ Features

- Connects to multiple FortiGate firewalls via SSH using **Netmiko**
- Applies configuration commands in bulk using `send_config_set`
- Built with error handling and clear console output
- Easily extensible — add more devices or commands
- Suitable for both **lab/testing** and **production** environments
- Works over WAN connections (increased timeout handling)

---

## 🛠 What It Does

The script:
1. Iterates through a list of FortiGate devices
2. Establishes an SSH connection to each one
3. Sends a set of configuration commands (currently focused on `config sys admin` → editing admin accounts and trust hosts)
4. Prints real-time output and status for each device
5. Handles connection failures gracefully

It is especially useful for quickly updating **outbound ACLs**, trust hosts, or other repetitive CLI configurations across multiple firewalls.

---

## 📋 Requirements

- **Python**: 3.9 or higher (tested up to 3.13)
- **Netmiko**: The multi-vendor SSH library by Kirk Byers

### Install Dependencies

```bash
pip install netmiko
