# Desktop Hardening Checker

Read-only defensive checks for a desktop posture snapshot. It reviews firewall status, disk encryption, updates, screen lock, and endpoint malware protection without changing the device or collecting personal data.

```powershell
python checker.py examples/posture.json
```

Created 2026-10-02. The JSON snapshot can be produced by an approved endpoint-management tool; this project does not query operating-system APIs or transmit results.
