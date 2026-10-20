# Scripts Documentation

This document describes the Bash scripts developed for the DevOps Lab project. Each section explains the purpose, functionality, usage, and syntax validation of each script.

## 1. System Information

**File:** `scripts/system-info.sh`

### Purpose

Displays general information about the system and performs basic network connectivity checks.

### Features

- Displays the hostname.
- Shows the operating system.
- Reports system uptime.
- Displays memory usage.
- Displays root filesystem disk usage.
- Shows CPU information.
- Checks internet connectivity using ping.
- Checks DNS resolution using getent.
- Displays a warning when root filesystem usage reaches or exceeds 80%.

### Usage

Run the script from the root directory of the repository:

    ./scripts/system-info.sh

### Validation

Check the Bash syntax without executing the script:

    bash -n scripts/system-info.sh

## 2. Filesystem Explorer

**File:** `scripts/filesystem-explorer.sh`

### Purpose

Explores the current working directory and provides a summary of its contents.

### Features

- Displays the current working directory.
- Lists files and directories, including hidden entries.
- Counts the files in the current directory.
- Counts the subdirectories in the current directory.

### Usage

Run the script from the root directory of the repository:

    ./scripts/filesystem-explorer.sh

### Validation

Check the Bash syntax without executing the script:

    bash -n scripts/filesystem-explorer.sh

### Important Note

The script analyzes the directory from which it is executed. Running it from a different directory may produce different results.

## 3. Resource Report

**File:** `scripts/resource-report.sh`

### Purpose

Generates a report containing system resource information and details about the processes currently running on the server.

### Features

- Displays the server hostname.
- Shows system uptime.
- Reports RAM and swap usage.
- Lists the five processes using the most CPU.
- Displays each process ID (PID).
- Shows process command names and CPU usage percentages.

### Usage

Run the script from the root directory of the repository:

    ./scripts/resource-report.sh

### Validation

Check the Bash syntax without executing the script:

    bash -n scripts/resource-report.sh

## General Notes

- All scripts are written in Bash.
- Scripts should be executed from the root directory of the repository using their relative paths.
- The `bash -n` command checks syntax without executing the script.
- These scripts support practical learning in Linux administration, system information gathering, filesystem exploration, resource monitoring, and automation.

## 4. Python System Report

**File:** `scripts/system_report.py`

### Purpose

Generates a system report using Python's built-in modules and Linux system information.

### Features

- Displays the hostname and operating system.
- Shows the operating system release and Python version.
- Includes the date and time when the report is generated.
- Reads `/proc/meminfo` to calculate RAM usage.
- Reports total, used, and available memory.
- Uses the `shutil` module to calculate total, used, and free disk space.
- Displays memory and disk usage percentages.

### Usage

Run the script from the root directory of the repository:

    python3 scripts/system_report.py

### Validation

Check the Python syntax without executing the script:

    python3 -m py_compile scripts/system_report.py

### Dependencies

The script uses Python's standard library and Linux system information. No external Python packages are required.
