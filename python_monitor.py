#!/usr/bin/env python3

import time
import platform
from datetime import datetime
import psutil
import distro

def print_system_info():
    print("=" * 60, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "=" * 60, flush=True)

    print("OS Information:")
    print(f"  Name: {distro.name()}", flush=True)
    print(f"  Version: {distro.version()}", flush=True)

    print("\nCPU Information:", flush=True)
    print(f"  Architecture: {platform.machine()}", flush=True)
    print(f"  Processor: {platform.processor()}", flush=True)
    print(f"  Cores (logical): {psutil.cpu_count(logical=True)}", flush=True)
    print(f"  Cores (physical): {psutil.cpu_count(logical=False)}", flush=True)

    mem = psutil.virtual_memory()
    print("\nRAM Usage (in MB):", flush=True)
    print(f"  Total: {mem.total // (1024 * 1024)} MB", flush=True)
    print(f"  Used: {mem.used // (1024 * 1024)} MB", flush=True)
    print(f"  Available: {mem.available // (1024 * 1024)} MB", flush=True)

    disk = psutil.disk_usage('/')
    print("\nDisk Usage (/):", flush=True)
    print(f"  Total: {disk.total // (1024 * 1024 * 1024)} GB", flush=True)
    print(f"  Used: {disk.used // (1024 * 1024 * 1024)} GB", flush=True)
    print(f"  Free: {disk.free // (1024 * 1024 * 1024)} GB", flush=True)

    print("=" * 130 + "\n", flush=True)

def main():
    while True:
        print_system_info()
        time.sleep(13)

if __name__ == "__main__":
    main()
