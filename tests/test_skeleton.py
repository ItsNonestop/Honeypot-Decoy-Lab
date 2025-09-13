from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))
import honeypot


def test_import() -> None:
    assert honeypot is not None


def test_config_exists() -> None:
    assert Path("config/app.yaml").exists()
