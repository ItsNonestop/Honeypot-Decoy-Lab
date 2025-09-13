"""Paramiko-based SSH honeypot server."""

from __future__ import annotations

import os
import socket
import threading
from pathlib import Path
from typing import Tuple

import paramiko

from .config import Config, load_config
from .ip_anonymize import anonymize_ip
from .logging_utils import write_event

HOST_KEY_PATH = Path("data/host_key")


def _get_host_key() -> paramiko.RSAKey:
    if HOST_KEY_PATH.exists():
        return paramiko.RSAKey.from_private_key_file(str(HOST_KEY_PATH))
    HOST_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    key = paramiko.RSAKey.generate(2048)
    key.write_private_key_file(str(HOST_KEY_PATH))
    return key


class HoneypotServer(paramiko.ServerInterface):
    """Server interface capturing credentials and commands."""

    def __init__(self, client_ip: str, cfg: Config):
        self.client_ip = client_ip
        self.cfg = cfg
        self.username: str | None = None

    # channel requests
    def check_channel_request(self, kind: str, chanid: int) -> int:
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def get_allowed_auths(self, username: str) -> str:  # type: ignore[override]
        return "password"

    def check_auth_password(self, username: str, password: str) -> int:
        self._log({"event": "auth_attempt", "username": username, "password": password})
        self.username = username
        self._log({"event": "auth_success", "username": username})
        return paramiko.AUTH_SUCCESSFUL

    # helper
    def _log(self, data: dict) -> None:
        salt = os.getenv("ANON_SALT", "demo-salt")
        anon = anonymize_ip(
            self.client_ip,
            self.cfg.ip_anonymization.get("mode", "truncate"),
            salt,
        )
        base = {"src_ip": self.client_ip, "src_ip_anon": anon}
        base.update(data)
        write_event(base)


def _handle_client(client: socket.socket, addr: Tuple[str, int], cfg: Config) -> None:
    server = HoneypotServer(addr[0], cfg)
    server._log({"event": "connection_open"})
    transport = paramiko.Transport(client)
    transport.add_server_key(_get_host_key())
    transport.local_version = cfg.banner_text
    try:
        transport.start_server(server=server)
        channel = transport.accept(20)
        if channel is None:
            return
        channel.settimeout(60)
        channel.send("Welcome to honeypot-ssh (fake shell). Type 'exit' to leave.\n")
        while True:
            channel.send("> ")
            try:
                data = channel.recv(1024)
            except socket.timeout:
                break
            if not data:
                break
            cmd = data.decode().strip()
            if cmd in {"exit", "quit"}:
                break
            server._log({"event": "command", "cmd": cmd})
            channel.send(cmd + "\n")
    finally:
        server._log({"event": "connection_close"})
        transport.close()
        client.close()


def run_server(cfg: Config | None = None) -> None:
    """Run the honeypot server."""
    cfg = cfg or load_config()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((cfg.listen_host, cfg.listen_port))
    sock.listen(100)
    print(f"Listening on {cfg.listen_host}:{cfg.listen_port}")
    while True:
        client, addr = sock.accept()
        threading.Thread(target=_handle_client, args=(client, addr, cfg), daemon=True).start()
