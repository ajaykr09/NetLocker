import time

print("Demo: Simulating VPN up/down")
for i in range(3):
    print("VPN down - blocking traffic")
    time.sleep(2)
    print("VPN up - restoring traffic")
    time.sleep(2)

