# DevOps Lab

**A hands-on laboratory to learn, build, automate, and document DevOps practices.**

This repository documents my practical journey into DevOps, starting with Linux administration and Bash scripting and progressing towards containers, CI/CD, Infrastructure as Code, cloud platforms, and Kubernetes

## Project Goals

- Strengthen Linux administration and networking fundamentals
- Automate repetitive tasks with Bash and Python
- Build and manage containerized applications with Docker
- Implement CI/CD pipelines
- Practice Infrastructure as Code using Terraform
- Automate configuration management with Ansible
- Deploy and manage workloads with Kubernetes
- Learn monitoring, logging, and troubleshooting

## Infrastructure

| Component | Details |
|---|---|
| Host OS | Windows |
| Hypervisor | VMware |
| Server OS | Ubuntu Server |
| Network Mode | NAT |
| Remote Access | SSH |
| Version Control | Git and GitHub |

## Technologies

**Current focus:** Linux, Bash, networking, and Git

**Planned learning path:** Python, Docker, CI/CD, Ansible, Terraform, cloud platforms, Kubernetes, monitoring, and logging

## Repository Structure

    devops-lab/
    ├── README.md
    ├── docs/
    │   ├── entorno.md
    │   └── scripts.md
    └── scripts/
        ├── system-info.sh
        ├── filesystem-explorer.sh
        └── resource-report.sh

## Scripts

| Script | Description |
|---|---|
| `system-info.sh` | Displays system information and performs basic connectivity checks |
| `filesystem-explorer.sh` | Explores directory contents and counts files and directories |
| `resource-report.sh` | Reports system uptime, memory usage, and top CPU-consuming processes |
| `system_report.py` | Reports system information, RAM usage, and disk usage using Python |

For detailed descriptions, usage instructions, and syntax validation, see the [Scripts Documentation](docs/scripts.md)

For detailed descriptions, usage instructions, and syntax validation, see the [Scripts Documentation](docs/scripts.md)

## Learning Roadmap

- [x] Set up the Ubuntu Server lab environment
- [x] Configure SSH access and connect the repository to GitHub
- [x] Create Bash scripts for system information and filesystem exploration
- [x] Create a resource report for monitoring processes and memory
- [ ] Strengthen Linux and networking fundamentals
- [ ] Develop Python automation scripts
- [ ] Containerize applications with Docker
- [ ] Build CI/CD pipelines
- [ ] Automate infrastructure and configuration
- [ ] Explore cloud platforms and Kubernetes
- [ ] Implement monitoring and logging

## Current Status

The project is currently focused on Linux fundamentals and Bash scripting

- **Day 1 — Environment Setup:** Configured Ubuntu Server in VMware and connected the repository to GitHub
- **Day 2 — System Information Script:** Created a Bash script to report basic system information
- **Day 3 — Disk Usage Monitoring:** Added a warning when root filesystem usage reaches 80%
- **Day 4 — Linux Commands and Bash Automation:** Practiced filesystem commands and built a Bash script to explore directories and count files and folders
- **Day 5 — Process and Resource Monitoring:** Practiced Linux process management and resource monitoring commands. Created a Bash script to report system uptime, memory usage, and the top five CPU-consuming processes. Documented all three scripts in `docs/scripts.md` and improved the project README
- **Day 6 — Python System Monitoring:** Created a Python script to report system information, memory usage, and disk usage. Validated the script and configured Git to ignore Python cache files

## Documentation

- [Lab Environment](docs/entorno.md)
- [Scripts Documentation](docs/scripts.md)

---

*This repository is an ongoing practical learning project focused on building real-world DevOps skills through hands-on implementation and documentation*
