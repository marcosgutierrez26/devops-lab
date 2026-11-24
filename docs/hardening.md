# Linux Hardening

Hardening of the `ubuntu-devops` VM (Ubuntu Server 26.04 LTS, kernel 7.0.0), audited with Lynis.

## Baseline (Lynis)

| Metric | Value |
|---|---|
| Lynis version | 3.1.6 |
| Hardening index | **58** |
| Tests performed | 261 |
| Warnings | 1 (PKGS-7392: vulnerable packages) |
| Suggestions | 47 (10 of them SSH-related, SSH-7408) |

## SSH

### Findings
- `PasswordAuthentication yes`: password logins were allowed.
- `~/.ssh/authorized_keys` was empty, so every login used a password.

### Changes
- Authorized the Windows host's ed25519 public key in `~/.ssh/authorized_keys`.
- Added [`config/ssh/01-hardening.conf`](../config/ssh/01-hardening.conf) to `/etc/ssh/sshd_config.d/`:

| Setting | Reason |
|---|---|
| `PasswordAuthentication no` | Key-based authentication only |
| `KbdInteractiveAuthentication no` | Closes the other password prompt path |
| `PermitRootLogin no` | No root login over SSH |
| `MaxAuthTries 3` | Limits attempts per connection |
| `X11Forwarding no` | No GUI on the server |
| `AllowAgentForwarding no` | Prevents agent hijacking on the server |
| `LogLevel VERBOSE` | Logs the key fingerprint used for each login |

### Gotcha: `50-cloud-init.conf`
Ubuntu ships `/etc/ssh/sshd_config.d/50-cloud-init.conf` with `PasswordAuthentication yes`.
sshd loads `*.conf` files alphabetically and **the first value wins**, so the hardening
file is named `01-` to be read first.

### Verification
1. `sudo sshd -t`: configuration syntax OK.
2. `sudo sshd -T`: effective values match the hardening file.
3. Login from Windows with the key works; forcing password auth
   (`ssh -o PubkeyAuthentication=no`) returns `Permission denied (publickey)`.

## Results
- Pending: Lynis audit after completing Phase 1.
