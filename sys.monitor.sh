#!/bin/bash

# Function to gather and print system information
print_system_info() {
    echo "======================== $(date) ========================"
    
    # OS / Distribution Info
    if [ -f /etc/os-release ]; then
        echo "OS Information:"
        cat /etc/os-release | grep -E '^(NAME|VERSION)='
    else
        echo "OS Information: Not available"
    fi

    # CPU Info
    echo -e "\nCPU Information:"
    lscpu | grep -E '^(Architecture|Model name|CPU\(s\))'

    # RAM Info
    echo -e "\nRAM Usage (in MB):"
    free -m | awk 'NR==1 || NR==2 {print}'

    # Disk Usage
    echo -e "\nDisk Usage:"
    df -h --total | grep -E 'Filesystem|total'

    echo "============================================================="
    echo ""
}

# Infinite loop, run every 13 seconds
while true; do
    print_system_info
    sleep 13
done
