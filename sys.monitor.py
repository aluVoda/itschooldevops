#!/usr/bin/env python3

import time
import platform
import os
from datetime import datetime
import psutil
import distro  # You might need to install this: pip install distro

def print_system_info():
    print("=" * 60, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "=" * 60)
    
    # OS Info
    print("OS Information:")
    print(f"  Name: {distro.name()}")
    print(f"  Version: {distro.version()}")
    
    # CPU Info
    print("\nCPU Information:")
    print(f"  Architecture: {platform.machine()}")
    print(f"  Processor: {platform.processor()}")
    print(f"  Cores (logical): {psutil.cpu_count(logical=True)}")
    print(f"  Cores (physical): {psutil.cpu_count(logical=False)}")
    
    # RAM Info
    mem = psutil.virtual_memory()
    print("\nRAM Usage (in MB):")
    print(f"  Total: {mem.total // (1024 * 1024)} MB")
    print(f"  Used: {mem.used // (1024 * 1024)} MB")
    print(f"  Available: {mem.available // (1024 * 1024)} MB")
    
    # Disk Info
    disk = psutil.disk_usage('/')
    print("\nDisk Usage (/):")
    print(f"  Total: {disk.total // (1024 * 1024 * 1024)} GB")
    print(f"  Used: {disk.used // (1024 * 1024 * 1024)} GB")
    print(f"  Free: {disk.free // (1024 * 1024 * 1024)} GB")
    
    print("=" * 130 + "\n")

def main():
    while True:
        print_system_info()
        time.sleep(13)

if __name__ == "__main__":
    main()
