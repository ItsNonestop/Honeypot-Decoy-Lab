# Features

| Feature | Status | Files | Notes |
| --- | --- | --- | --- |
| Repo scaffold + CI + container smoke test | Done | README.md, docs/, config/, samples/, src/, tests/, deploy/, .github/ | Initial skeleton with docs and tests |
| SSH listener (Paramiko) | Complete | src/honeypot/server.py | Basic server with fake shell |
| Credential capture | Complete | src/honeypot/server.py | Logs username and password |
| Command logging (fake shell) | Complete | src/honeypot/server.py | Echoes and logs commands |
| JSONL writer + rotation | Complete | src/honeypot/logging_utils.py | Daily rotated event files |
