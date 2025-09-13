# honeypot-ssh

A honeypot is a decoy service that lures attackers so their methods can be studied.
This project sets up a fake SSH endpoint that never executes commands.
Events will be written to JSON Lines for later analysis.
A notebook and dashboard will eventually explore the collected data.
Connections are isolated and source IPs are anonymised for privacy.
No attacker input is executed, keeping hosts safe.
The code aims to stay simple, safe, and easy to extend.
Run the container to see the scaffolded message below.
Use this skeleton to verify the container and tests.
Further components arrive in future iterations.

```
[attacker] -> [listener] -> [fake shell] -> [logger] -> [analysis]
                        \______________________________/
```

## Quickstart (skeleton)
1. `git clone <repo>`
2. `docker compose up`
3. `pytest -q`
4. Logs would appear under `samples/` once implemented.

See [docs/architecture.md](docs/architecture.md) and [docs/safety-notes.md](docs/safety-notes.md) for more.
