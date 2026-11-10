#!/usr/bin/env python3

# DevOps Lab - System Report

import platform
import shutil
from datetime import datetime

def clasificar(uso):
    if uso >= 90:
        return "CRITICAL"
    elif uso >= 80:
        return "WARNING"
    else:
        return "normal"

def main():
    print("=" * 45)
    print("             SYSTEM REPORT")
    print("=" * 45)

    print(f"Hostname: {platform.node()}")
    print(f"Operating system: {platform.system()}")
    print(f"OS release: {platform.release()}")
    print(f"Python version: {platform.python_version()}")
    print(f"Report date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    print("\nMemory Usage:")

    with open("/proc/meminfo", "r", encoding="utf-8") as file:
        memory_info = {}

        for line in file:
            key, value = line.split(":", 1)
            if key in ("MemTotal", "MemAvailable"):
                memory_info[key] = int(value.strip().split()[0])

    total_memory = memory_info["MemTotal"]
    available_memory = memory_info["MemAvailable"]
    used_memory = total_memory - available_memory
    memory_percent = used_memory / total_memory * 100

    print(f"Total RAM: {total_memory / 1024:.2f} MB")
    print(f"Used RAM: {used_memory / 1024:.2f} MB")
    print(f"RAM usage: {memory_percent:.1f}% ({clasificar(memory_percent)})")

    print("\nDisk Usage (/):")

    total, used, free = shutil.disk_usage("/")
    disk_percent = used / total * 100

    print(f"Total disk: {total / (1024 ** 3):.2f} GB")
    print(f"Used disk: {used / (1024 ** 3):.2f} GB")
    print(f"Free disk: {free / (1024 ** 3):.2f} GB")
    print(f"Disk usage: {disk_percent:.1f}% ({clasificar(disk_percent)})")

if __name__ == "__main__":
    main()

