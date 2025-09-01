# NetLocker

**NetLocker** is a Python-based command-line utility that monitors a VPN connection and blocks traffic if the VPN goes down, preventing accidental IP leaks.

## Features
- Monitor any VPN interface (e.g., tun0, wg0)
- Automatically block all traffic if VPN disconnects
- Restore traffic once VPN is back or script is stopped
- Lightweight and cross-platform compatible

## Requirements
- Python 3.8+
- `psutil` library

Install dependencies:
```bash
python3 -m pip install -r requirements.txt

## Usage

source venv/bin/activate
sudo python3 netlocker.py --vpn tun0

Replace tun0 with your VPN interface name.
Use Ctrl+C to stop the program safely.

## Demo
python3 netlocker.py --demo

