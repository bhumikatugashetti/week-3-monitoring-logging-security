import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
policy = json.loads((BASE / "config" / "security_policy.json").read_text(encoding="utf-8"))

checks = [
    ("SSH restricted", not policy["ssh_open_to_world"], "Restrict SSH to trusted administrative sources."),
    ("Database private", not policy["database_publicly_accessible"], "Database must not be publicly accessible."),
    ("Encryption at rest", policy["encryption_at_rest"], "Enable encryption for stored data."),
    ("Encryption in transit", policy["encryption_in_transit"], "Use TLS for service communication."),
    ("Least privilege IAM", policy["least_privilege_iam"], "Limit IAM permissions to required actions."),
    ("Logging enabled", policy["logging_enabled"], "Enable application and security logging."),
    ("Privileged MFA", policy["mfa_required_for_privileged_users"], "Require MFA for privileged identities."),
    ("Unused ports blocked", policy["unused_ports_blocked"], "Remove unnecessary inbound access.")
]

def main():
    passed = 0
    print("CLOUD SECURITY CONFIGURATION AUDIT")
    print("==================================")
    for name, ok, recommendation in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        if not ok:
            print("      Recommendation:", recommendation)
        passed += int(ok)
    print(f"\nResult: {passed}/{len(checks)} controls passed.")

if __name__ == "__main__":
    main()
