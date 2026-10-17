#!/bin/bash

# DevOps Lab - System Information Script

echo "=================================="
echo "      UBUNTU SERVER REPORT"
echo "=================================="

echo
echo "1. HOSTNAME"
hostname

echo
echo "2. OPERATING SYSTEM"
grep PRETTY_NAME /etc/os-release | cut -d '"' -f 2

echo
echo "3. SYSTEM UPTIME"
uptime -p

echo
echo "4. MEMORY USAGE"
free -h

echo
echo "5. DISK USAGE"
df -h /

echo
echo "5.1. DISK SPACE CHECK"

disk_usage=$(df / | awk 'NR==2 {gsub("%","",$5); print $5}')

if [ "$disk_usage" -ge 80 ]; then
    echo "WARNING: Disk usage is ${disk_usage}%"
else
    echo "OK: Disk usage is ${disk_usage}%"
fi

echo
echo "6. CPU COUNT"
nproc

echo
echo "7. INTERNET CONNECTIVITY"
if ping -c 1 -W 2 8.8.8.8 > /dev/null 2>&1; then
    echo "Internet connectivity: OK"
else
    echo "Internet connectivity: FAILED"
fi

echo
echo "8. DNS RESOLUTION"
if getent hosts github.com > /dev/null 2>&1; then
    echo "DNS resolution: OK"
else
    echo "DNS resolution: FAILED"
fi
