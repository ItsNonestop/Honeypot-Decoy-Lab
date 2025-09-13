"""IP anonymisation helpers."""

from __future__ import annotations

from hashlib import sha256
from ipaddress import IPv4Address, IPv6Address, ip_address


def anonymize_ip(ip: str, mode: str, salt: str | None = None) -> str:
    """Anonymise an IP address using truncate or hash modes."""
    addr = ip_address(ip)
    if mode == "truncate":
        if isinstance(addr, IPv4Address):
            return str(IPv4Address(int(addr) & 0xFFFFFF00))
        if isinstance(addr, IPv6Address):
            return str(IPv6Address(int(addr) >> 80 << 80))
    if mode == "hash":
        digest = sha256((ip + (salt or "demo-salt")).encode()).hexdigest()
        return digest[:12]
    return ip
