# honeypot-ssh

A honeypot is a decoy service that lures attackers so their methods can be studied.
This project provides a fake SSH server that records login attempts and commands.
Captured events are stored as JSON Lines for later analysis.
A notebook and dashboard will eventually explore the collected data.
All input is ignored and never executed, keeping the host safe.
Source IPs are anonymised and only loopback is bound by default.
Use Docker or Python to run the skeleton locally.
No outbound connections are made.
This repo aims to stay small, clear and easy to extend.
Cross-platform helper scripts are provided for Windows, macOS, and Linux.

```
[attacker] -> [ssh server] -> [fake shell] -> [logger] -> [JSONL files]
```

## Quick demo in 60 seconds
1. `git clone <repo> && cd honeypot-ssh`
2. `docker compose -f deploy/docker-compose.yml up --build`
3. In another terminal: `ssh -p 2222 test@localhost` (enter any password)
4. Type `uname -a`, `whoami`, `exit`
5. View logs: `tail -n 10 data/logs/events-*.jsonl`

## Local (no Docker)
```
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
python -m honeypot --host 127.0.0.1 --port 2222
```

## Troubleshooting
- Windows users: run under WSL.
- If port 2222 is busy, choose another with `--port`.
- The first SSH connect will prompt to trust the host key.

See [docs/architecture.md](docs/architecture.md) for component details and [docs/safety-notes.md](docs/safety-notes.md) before exposing any service.
This is a **decoy**; commands are **not executed**.

## Quickstart for Everyone (copy-paste)

### Windows (PowerShell)
1) `python -V`  # expect 3.11–3.13
2) `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
3) `.\scripts\win\setup.ps1`
4) `.\scripts\win\run.ps1`    # or: `python run.py`
5) `.\scripts\win\test.ps1`   # optional: lint + tests

### macOS / Linux (bash)
1) `python3 -V`
2) `bash scripts/unix/setup.sh`
3) `bash scripts/unix/run.sh`
4) `bash scripts/unix/test.sh`  # optional

## Troubleshooting
- No module named honeypot → activate venv or use `python run.py`.
- Package requires a different Python → pull latest; should now allow 3.13. If not, open an issue.
- pytest not recognised → use `.\venv\Scripts\pytest.exe` on Windows or run `scripts/*/test`.
- docker compose not found → local runs are supported; Docker is optional.
