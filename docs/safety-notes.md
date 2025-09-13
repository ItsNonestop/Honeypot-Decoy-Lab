# Safety Notes

This lab is deliberately low interaction. The fake shell never runs commands, so attackers cannot pivot. Outbound connections are blocked and the container should live on a segmented VLAN. IP addresses must be anonymised either by hashing or by truncating to /24 before storage. Operators should abide by legal and ethical guidelines when deploying research honeypots.

## Local test vs. Internet exposure
The default configuration binds to the loopback address for safety. The Docker example exposes port 2222 only for local testing. Do not expose the service to the public Internet unless it is isolated on a VLAN with strict egress controls and you understand the legal implications.

## Operator checklist
- review listening ports
- verify VLAN and firewall egress rules
- rotate and secure any secrets
