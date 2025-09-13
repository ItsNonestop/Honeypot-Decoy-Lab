"""Configuration loader for honeypot-ssh."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict

import yaml


@dataclass
class Config:
    """Runtime configuration values."""

    listen_host: str = "127.0.0.1"
    listen_port: int = 2222
    log_dir: str = "data/logs"
    log_rotation_days: int = 7
    banner_text: str = "SSH-2.0-OpenSSH_8.9"
    ip_anonymization: Dict[str, str] = field(
        default_factory=lambda: {"mode": "truncate"}
    )


def load_config(path: str = "config/app.yaml") -> Config:
    """Load configuration from YAML file, applying defaults."""
    cfg = Config()
    cfg_path = Path(path)
    if cfg_path.exists():
        with cfg_path.open("r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh) or {}
        for key, value in data.items():
            if hasattr(cfg, key):
                setattr(cfg, key, value)
    # ensure directories
    Path(cfg.log_dir).mkdir(parents=True, exist_ok=True)
    Path("data").mkdir(parents=True, exist_ok=True)
    return cfg
