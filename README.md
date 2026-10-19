# devops-lab

Hands-on DevOps learning lab covering Linux, networking, Docker, CI/CD, Terraform, Ansible and Kubernetes.

## Infrastructure

- **Hypervisor:** VMware
- **Operating System:** Ubuntu Server
- **Network mode:** NAT

## Scripts

# Filesystem Explorer

The `scripts/filesystem-explorer.sh` script displays the current directory, lists its contents, and counts files and directories.

## Usage

Run the script from the directory you want to inspect:

```bash
~/devops-lab/scripts/filesystem-explorer.sh
```

---

# System Information

The `scripts/system-info.sh` script collects basic information about the Ubuntu Server environment.

## Usage

```bash
~/devops-lab/scripts/system-info.sh
```

It reports:

- Hostname and operating system
- System uptime
- Memory usage
- Root filesystem disk usage
- Number of available CPUs
- Internet connectivity
- DNS resolution
- Disk usage warning when usage reaches 80%

### Usage

Run the script from the repository root:

```bash
chmod +x scripts/system-info.sh
./scripts/system-info.sh
```

### Validation

Check the script syntax before running it:

```bash
bash -n scripts/script_name.sh
```

## Project Goals

- Develop Linux administration skills
- Automate tasks with Bash
- Learn networking fundamentals
- Practice Docker and CI/CD
- Build practical DevOps projects

## Current Status

The project is currently focused on Linux fundamentals
and Bash scripting.


- **Day 1 — Environment Setup:** Configured Ubuntu Server in VMware and connected the repository to GitHub.
- **Day 2 — System Information Script:** Created a Bash script to report basic system information.
- **Day 3 — Disk Usage Monitoring:** Added a warning when root filesystem usage reaches 80%.
- **Day 4 — Linux Commands and Bash Automation:** Practiced filesystem commands and built a Bash script to explore directories and count files and folders.
