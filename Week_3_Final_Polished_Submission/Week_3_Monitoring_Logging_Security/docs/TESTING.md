# Testing

1. Run `python src/app_simulator.py`.
2. Run `python src/monitor.py`.
3. Run `python src/log_analyzer.py`.
4. Run `python src/security_audit.py`.
5. Confirm `logs/application.log` and `logs/monitoring.jsonl` are created.
6. Confirm the monitoring script reports threshold breaches.
7. Confirm the security audit reports all configured controls as PASS.

Expected result: the simulation completes without external cloud credentials and produces monitoring,
logging, analysis, and security-audit output.
