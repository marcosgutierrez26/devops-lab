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
