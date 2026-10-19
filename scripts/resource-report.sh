#!/bin/bash


echo "=================================="
echo "       RESOURCE REPORT"
echo "=================================="
echo

echo "Hostname:"
hostname

echo
echo "Uptime:"
uptime -p

echo
echo "Memory usage:"
free -h

echo
echo "Top 5 CPU processes:"
ps -eo pid,comm,%cpu --sort=-%cpu | head -n 6
