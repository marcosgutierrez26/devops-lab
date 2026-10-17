# devops-lab

Hands-on DevOps learning lab covering Linux, networking, Docker, CI/CD, Terraform, Ansible and Kubernetes.

## Infrastructure

- **Hypervisor:** VMware
- **Operating System:** Ubuntu Server
- **Network mode:** NAT

## Scripts

### System Information

The `scripts/system-info.sh` script collects basic information about the Ubuntu Server environment.

It reports:

- Hostname and operating system
- System uptime
- Memory usage
- Root filesystem disk usage
- Number of available CPUs
- Internet connectivity
- DNS resolution

### Usage

Run the script from the repository root:

```bash
chmod +x scripts/system-info.sh
./scripts/system-info.sh
```

### Validation

Check the script syntax before running it:

```bash
bash -n scripts/system-info.sh
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
