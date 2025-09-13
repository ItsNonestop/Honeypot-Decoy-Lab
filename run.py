"""Convenience runner for the honeypot package."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
try:
    from honeypot.__main__ import main
except Exception:  # pragma: no cover - user guidance
    print("honeypot not installed. Run scripts/unix/setup.sh or scripts/win/setup.ps1, or 'pip install -e .'.")
else:
    main()
