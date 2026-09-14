# Security Design

The simulation models common cloud-security controls:

- No public database exposure.
- SSH access is restricted rather than open to the world.
- Encryption at rest and in transit is enabled.
- Least-privilege IAM is required.
- Logging is enabled.
- MFA is required for privileged users.
- Unused ports are blocked.

The security audit intentionally reads these controls from `config/security_policy.json`, allowing the
configuration to be changed and re-tested.
