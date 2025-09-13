# Safety Notes

This lab is deliberately low interaction. The fake shell never runs commands, so attackers cannot pivot. Outbound connections are blocked and the container should live on a segmented VLAN. IP addresses must be anonymised either by hashing or by truncating to /24 before storage. Operators should abide by legal and ethical guidelines when deploying research honeypots.

## Operator checklist
- review listening ports
- verify VLAN and firewall egress rules
- rotate and secure any secrets
