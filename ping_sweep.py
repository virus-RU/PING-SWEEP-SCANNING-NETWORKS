import os
import platform

def ping_sweep(ip_range):
    # Determine the correct ping flag based on the operating system
    if platform.system().lower() == "windows":
        ping_command = "ping -n 1"
    else:
        ping_command = "ping -c 1"

    for i in range(1, 255):
        ip = f"{ip_range}.{i}"
        
        # Send a single ping to the host
        response = os.system(f"{ping_command} {ip}")
        
        # Check if the ping was successful
        if response == 0:
            print(f"Host {ip} is up.")
        else:
            print(f"Host {ip} is down.")
