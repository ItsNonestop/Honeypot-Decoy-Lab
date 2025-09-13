from pathlib import Path

import paramiko

from honeypot import server as hp_server
from honeypot.config import Config


def test_server_interface(monkeypatch) -> None:
    events = []

    def fake_writer(event):
        events.append(event)
        return Path("/tmp/dummy")

    monkeypatch.setattr(hp_server, "write_event", fake_writer)

    cfg = Config()
    server = hp_server.HoneypotServer("203.0.113.5", cfg)
    assert server.get_allowed_auths("user") == "password"
    result = server.check_auth_password("user", "pass")
    assert result == paramiko.AUTH_SUCCESSFUL
    assert any(e.get("event") == "auth_attempt" for e in events)
