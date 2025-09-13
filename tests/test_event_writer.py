import importlib
import json

from honeypot import logging_utils
from honeypot import config as hp_config


class DummyConfig(hp_config.Config):
    log_dir: str  # type: ignore[assignment]


def test_write_event(tmp_path, monkeypatch) -> None:
    dummy = DummyConfig(log_dir=str(tmp_path))
    monkeypatch.setattr(logging_utils, "load_config", lambda: dummy)
    importlib.reload(logging_utils)
    path = logging_utils.write_event({"event": "test"})
    assert path.exists()
    lines = path.read_text().strip().splitlines()
    data = json.loads(lines[-1])
    assert data["event"] == "test"
    assert "ts" in data
