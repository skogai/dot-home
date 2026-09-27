# dot health probe

`health-check.py` is a local command-line probe for the generated Linux systemd
user service. It does **not** start an HTTP server.

```bash
./health-check.py
```

The command prints JSON and exits 0 only while `dot.service` is active. It
exits 1 for inactive, failed, missing, timed-out, or unreachable user managers,
which makes it suitable for local monitoring and cron checks.

Useful companion commands:

```bash
systemctl --user status dot.service
journalctl --user -u dot.service -n 50
systemctl --user start dot.service
```

The probe is generated only for `--platform linux`. launchd users can inspect
`launchctl print gui/$(id -u)/com.gptme.dot` instead.
