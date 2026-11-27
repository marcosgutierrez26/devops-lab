#!/usr/bin/env bash
# security-check.sh - Checks the Phase 1 hardening of the server
# Usage: sudo ./scripts/security-check.sh

export LC_ALL=C

if [ "$EUID" -ne 0 ]; then
    echo "Run it with sudo: sudo $0"
    exit 1
fi

fails=0
ok()   { echo "  [OK]   $1"; }
fail() { echo "  [FAIL] $1"; fails=$((fails + 1)); }

echo "=== Security check: $(hostname) ==="

echo "SSH"
if sshd -T | grep -q "^passwordauthentication no"; then
    ok "Password login disabled"
else
    fail "Password login enabled"
fi
if sshd -T | grep -q "^permitrootlogin no"; then
    ok "Root login disabled"
else
    fail "Root login allowed"
fi

echo "Firewall"
if ufw status | grep -q "Status: active"; then
    ok "ufw active"
else
    fail "ufw inactive"
fi

echo "fail2ban"
if systemctl is-active --quiet fail2ban; then
    ok "fail2ban running"
else
    fail "fail2ban not running"
fi

echo "Updates"
pending=$(apt list --upgradable 2>/dev/null | grep -ci security)
if [ "$pending" -eq 0 ]; then
    ok "No pending security updates"
else
    fail "$pending pending security updates"
fi
if [ -f /var/run/reboot-required ]; then
    fail "Reboot required"
else
    ok "No reboot required"
fi

echo "=== Result: $fails failed check(s) ==="
exit "$fails"
