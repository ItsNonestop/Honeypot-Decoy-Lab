"""Temporary entrypoint."""

# <!-- codex:start:entrypoint -->
import argparse

from .config import load_config
from .server import run_server


def main() -> None:
    """CLI entrypoint for running the honeypot server."""
    cfg = load_config()
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default=cfg.listen_host)
    parser.add_argument("--port", type=int, default=cfg.listen_port)
    args = parser.parse_args()
    cfg.listen_host = args.host
    cfg.listen_port = args.port
    run_server(cfg)


if __name__ == "__main__":
    main()
# <!-- codex:end:entrypoint -->
