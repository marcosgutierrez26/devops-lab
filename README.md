# DevSecOps Lab

**A hands-on lab to build, secure, and automate infrastructure: from a hardened Linux server to a security-scanned CI/CD pipeline and Terraform on AWS.**

This repository documents my practical journey into DevSecOps. It started with Linux administration and scripting and now applies security at every layer: the server, the code, the container, the pipeline, and the cloud infrastructure.

## Project Goals

- Harden and audit Linux servers
- Automate administration and security checks with Bash and Python
- Build secure, minimal container images
- Implement CI/CD pipelines with automated security scanning
- Provision AWS infrastructure with Terraform and scan it as code
- Apply least privilege and secure secrets management
- Learn monitoring, logging, and troubleshooting

## Infrastructure

| Component | Details |
|---|---|
| Host OS | Windows |
| Hypervisor | VMware |
| Server OS | Ubuntu Server |
| Network Mode | NAT |
| Remote Access | SSH (key-based) |
| Version Control | Git and GitHub |

## Technologies

**Current focus:** Linux, Bash, Python, Flask, Git, Docker, and Linux hardening (SSH, ufw, Lynis)

**Planned:** fail2ban, pytest, Bandit, hadolint, Trivy, GitHub Actions, Gitleaks, pip-audit, Terraform, Checkov, AWS, and Kubernetes

##Repository Structure

    devsecops-lab/
    ├── README.md
    ├── app/
    │   ├── .dockerignore
    │   ├── Dockerfile
    │   ├── app.py
    │   └── requirements.txt
    ├── config/
    │   └── ssh/
    │       └── 01-hardening.conf
    ├── docs/
    │   ├── docker.md
    │   ├── entorno.md
    │   ├── hardening.md
    │   └── scripts.md
    └── scripts/
        ├── system-info.sh
        ├── filesystem-explorer.sh
        ├── resource-report.sh
        └── system_report.py

## Scripts

| Script | Description |
|---|---|
| `system-info.sh` | Displays system information and performs basic connectivity checks |
| `filesystem-explorer.sh` | Explores directory contents and counts files and directories |
| `resource-report.sh` | Reports system uptime, memory usage, and top CPU-consuming processes |
| `system_report.py` | Reports system information, RAM usage, and disk usage using Python |

For usage instructions and syntax validation, see the [Scripts Documentation](docs/scripts.md).

## DevSecOps Roadmap

- [x] Ubuntu Server lab environment with SSH and GitHub
- [x] Bash and Python scripting for system monitoring
- [x] Docker fundamentals and a containerized Flask API
- [ ] **Phase 1 — Linux hardening:** SSH, firewall, fail2ban, automatic updates, Lynis audit
- [ ] **Phase 2 — Application security:** tests with pytest and static analysis with Bandit
- [ ] **Phase 3 — Secure containers:** non-root multi-stage image, hadolint, Trivy
- [ ] **Phase 4 — CI/CD security gates:** GitHub Actions with Gitleaks, Bandit, pip-audit, and Trivy
- [ ] **Phase 5 — Secure IaC on AWS:** Terraform, Checkov, OIDC, and Secrets Manager
- [ ] **Phase 6 — Kubernetes security and monitoring**

## Progress Log

- **Day 1 — Environment Setup:** Configured Ubuntu Server in VMware and connected the repository to GitHub
- **Day 2 — System Information Script:** Created a Bash script to report basic system information
- **Day 3 — Disk Usage Monitoring:** Added a warning when root filesystem usage reaches 80%
- **Day 4 — Linux Commands and Bash Automation:** Built a Bash script to explore directories and count files and folders
- **Day 5 — Process and Resource Monitoring:** Created a Bash script to report uptime, memory usage, and the top five CPU-consuming processes
- **Day 6 — Python System Monitoring:** Created a Python script to report system information, memory usage, and disk usage
- **Day 7 — Python Conditionals and Functions:** Added RAM and disk usage level classification (normal, WARNING, CRITICAL)
- **Day 8 — Python Lists and Dictionaries:** Parsed `/proc/meminfo` into a dictionary and learned why `MemAvailable` beats `MemFree`
- **Day 9 — Docker and Flask API:** Built a Flask API with `/` and `/disk` endpoints, switched GitHub authentication to SSH keys, and containerized the API
- **Day 10 — DevSecOps Refocus:** Renamed the repository to `devsecops-lab` and redefined the roadmap around security at every layer
- **Day 11 — SSH Hardening:** Ran a Lynis baseline audit (hardening index 58) and enforced key-only SSH authentication with `config/ssh/01-hardening.conf`, documented in `docs/hardening.md`
- **Day 12 — Firewall with ufw:** Enabled ufw with default deny incoming and only SSH allowed (Lynis 61 → 65), and proved that Docker-published ports bypass ufw (fixed by binding to `127.0.0.1`), documented in `docs/hardening.md`

## Documentation

- [Lab Environment](docs/entorno.md)
- [Scripts Documentation](docs/scripts.md)
- [Docker Notes](docs/docker.md)
- [Linux Hardening](docs/hardening.md)

---

*An ongoing hands-on project to build real-world DevSecOps skills through implementation and documentation.*
