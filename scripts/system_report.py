#!/usr/bin/env python3

# DevOps Lab - System Report

import platform
from datetime import datetime

print("=" * 40)
print("          SYSTEM REPORT")
print("=" * 40)

print(f"Hostname: {platform.node()}")
print(f"Operating system: {platform.system()}")
print(f"OS release: {platform.release()}")
print(f"Python version: {platform.python_version()}")
print(f"Report date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
