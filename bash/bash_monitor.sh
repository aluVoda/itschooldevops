#!/bin/bash

# Interval in seconds
INTERVAL=5  # Adjust the interval as desired

while true; do
    # Print the current time and date
    echo "Current time and date: $(date)"

    # Print OS information
    echo "OS Information: $(uname -a)"

    # Print Linux distribution information
    echo "Linux Distribution Information: $(lsb_release -a)"

    # Print CPU information
    echo "CPU Information: $(lscpu)"

    # Print RAM information
    echo "RAM Information: $(free -h)"

    # Print disk usage information
    echo "Disk Usage Information: $(df -h)"

    # Wait for the next interval
    sleep $INTERVAL
done
