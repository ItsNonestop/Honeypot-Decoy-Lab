"""Logging helpers for JSONL event writing."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict

from .config import load_config


def write_event(event: Dict[str, object]) -> Path:
    """Write an event to today's JSONL file and return its path."""
    cfg = load_config()
    log_dir = Path(cfg.log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)
    filename = f"events-{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.jsonl"
    path = log_dir / filename
    event_with_ts = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        **event,
    }
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(event_with_ts) + "\n")
    return path
