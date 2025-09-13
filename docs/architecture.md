# Architecture

The system is split into clear pieces to keep risk low and analysis easy. A Paramiko SSH server accepts connections and hands control to a fake shell. The shell never executes commands but records them for study. A logger writes each event to JSON Lines. An analyser will parse logs and a dashboard can display trends.

<!-- codex:start:sequence -->
```mermaid
sequenceDiagram
    participant A as Attacker
    participant H as SSH Server
    participant S as Fake Shell
    participant L as Logger
    participant F as JSONL Files
    A->>H: connect
    H->>S: relay input
    S->>L: log event
    L->>F: append
```
<!-- codex:end:sequence -->
