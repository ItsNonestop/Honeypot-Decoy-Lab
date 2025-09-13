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
