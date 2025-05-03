import time
import subprocess

# Interval in seconds
INTERVAL = 5  # Adjust the interval as desired

while True:
    # Print the current time and date
    print(f"Current time and date: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Print OS information
    os_info = subprocess.getoutput("uname -a")
    print(f"OS Information: {os_info}")

    # Print Linux distribution information
    dist_info = subprocess.getoutput("lsb_release -a")
    print(f"Linux Distribution Information: {dist_info}")

    # Print CPU information
    cpu_info = subprocess.getoutput("lscpu")
    print(f"CPU Information: {cpu_info}")

    # Print RAM information
    ram_info = subprocess.getoutput("free -h")
    print(f"RAM Information: {ram_info}")

    # Print disk usage information
    disk_info = subprocess.getoutput("df -h")
    print(f"Disk Usage Information: {disk_info}")

    # Wait for the next interval
    time.sleep(INTERVAL)
