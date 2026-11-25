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

### Findings
- ufw was installed but **inactive**: no host firewall filtering incoming traffic.
- Lynis reported a "host based firewall" as active, but it was only detecting Docker's own rules.
- `ss -tulpn` showed SSH (22) as the only service listening on all interfaces.

### Changes
    sudo ufw default deny incoming
    sudo ufw default allow outgoing
    sudo ufw allow 22/tcp
    sudo ufw enable

The SSH rule was added **before** enabling ufw to avoid locking myself out.

### Gotcha: Docker bypasses ufw
Publishing a port with `docker run -p 5000:5000` made the Flask API reachable from the
host machine even though ufw denies all incoming traffic except SSH.

Docker rewrites the destination in `PREROUTING` (DNAT) and the packet goes through the
`FORWARD` chain, where Docker's rules are evaluated before ufw. ufw's rules live in `INPUT`,
so they never see that traffic.

**Fix used:** bind published ports to localhost when they don't need to be public:

    docker run -p 127.0.0.1:5000:5000 devops-api

### Verification
1. `sudo ufw status verbose`: active, default deny incoming, only 22/tcp allowed.
2. SSH from the Windows host still works.
3. With `-p 5000:5000` the API was reachable from Windows; with `-p 127.0.0.1:5000:5000`
   the connection timed out (dropped by ufw), while `curl` from the VM still worked.

## Results

| Stage | Hardening index |
|---|---|
| Baseline | 58 |
| After SSH hardening | 61 |
| After firewall (ufw) | 65 |
| After Phase 1 | pending |
