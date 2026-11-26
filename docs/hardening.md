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

## Firewall (ufw)

## Brute-force protection (fail2ban)

### Findings
- No mechanism to block hosts that repeatedly fail authentication (Lynis DEB-0880).
- After installation, Ubuntu enables the `sshd` jail by default: 5 failures in 10 minutes, 10-minute ban.

### Changes
Added [`config/fail2ban/sshd.local`](../config/fail2ban/sshd.local) to `/etc/fail2ban/jail.d/`:

| Setting | Value | Reason |
|---|---|---|
| `maxretry` | 3 | Matches `MaxAuthTries 3` in SSH; key-only auth means legitimate users don't fail |
| `findtime` | 10m | Window in which failures are counted |
| `bantime` | 1h | Makes repeated attempts more costly |

### Verification
1. `sudo fail2ban-client -t`: configuration OK.
2. `fail2ban-client get sshd maxretry / bantime`: `3` and `3600`.
3. Three SSH attempts from the Windows host with a non-existent user banned its IP
   (`192.168.78.1`); further connections timed out. Unbanned from the VM console with
   `fail2ban-client set sshd unbanip`.

##Results

| Stage | Hardening index |
|---|---|
| Baseline | 58 |
| After SSH hardening | 61 |
| After firewall (ufw) | 65 |
| After Phase 1 | pending |
| After brute-force protection (fail2ban) | 68 |
