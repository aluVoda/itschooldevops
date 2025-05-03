#!/bin/bash

print_system_info() {
    echo "======================== $(date) ========================"
    
    if [ -f /etc/os-release ]; then
        echo "OS Information:"
        grep -E '^(NAME|VERSION)=' /etc/os-release
    else
        echo "OS Information: Not available"
    fi

    echo -e "\nCPU Information:"
    lscpu | grep -E '^(Architecture|Model name|CPU\(s\))'

    echo -e "\nRAM Usage (in MB):"
    free -m | awk 'NR==1 || NR==2 {print}'

    echo -e "\nDisk Usage:"
    df -h --total | grep -E 'Filesystem|total'

    echo "============================================================="
    echo ""
}

while true; do
    print_system_info
    sleep 13
done
