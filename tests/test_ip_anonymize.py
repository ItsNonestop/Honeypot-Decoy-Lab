from honeypot.ip_anonymize import anonymize_ip


def test_truncate_ipv4() -> None:
    assert anonymize_ip("203.0.113.5", "truncate") == "203.0.113.0"


def test_truncate_ipv6() -> None:
    assert anonymize_ip("2001:db8:1:2:3:4:5:6", "truncate") == "2001:db8:1::"


def test_hash() -> None:
    assert (
        anonymize_ip("203.0.113.5", "hash", "salt")
        == "a49469c16ea6"
    )
