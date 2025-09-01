#!/usr/bin/env python3
import psutil
import time
import argparse
import os

def block_traffic():
    print("[!] VPN down! Blocking traffic...")
    os.system("sudo iptables -P OUTPUT DROP")

def unblock_traffic():
    print("[+] VPN up! Restoring traffic...")
    os.system("sudo iptables -P OUTPUT ACCEPT")

def monitor_vpn(vpn_iface):
    vpn_up = False
    try:
        while True:
            addrs = psutil.net_if_addrs()
            if vpn_iface in addrs:
                if not vpn_up:
                    vpn_up = True
                    unblock_traffic()
            else:
                if vpn_up or not vpn_up:
                    vpn_up = False
                    block_traffic()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[INFO] Stopped by user. Restoring traffic...")
        unblock_traffic()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NetLocker - VPN Leak Prevention Tool")
    parser.add_argument("--vpn", type=str, default="tun0", help="VPN interface to monitor")
    args = parser.parse_args()

    print(f"Monitoring VPN interface: {args.vpn}")
    monitor_vpn(args.vpn)

