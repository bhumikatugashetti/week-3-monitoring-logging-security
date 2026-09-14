# Week 3 – Monitoring, Logging, and Cloud Security Setup Simulation

## Overview
This project simulates a practical cloud operations environment without requiring an AWS account.
It demonstrates monitoring, centralized-style application logging, health checks, threshold alerts,
log analysis, and basic cloud security configuration review.

## Features
- Application health simulation
- Structured JSON application logs
- CPU, memory, disk, request-latency and error-rate monitoring
- Threshold-based alert generation
- Log analysis and summary report
- Security configuration simulation
- Checks for public database exposure, unrestricted SSH, weak password settings, and encryption
- Human-readable security findings
- No cloud credentials or secrets required

## Project Structure
```text
src/
  app_simulator.py
  monitor.py
  log_analyzer.py
  security_audit.py
config/
  monitoring.json
  security_policy.json
logs/
  .gitkeep
docs/
  architecture.md
  TESTING.md
  SECURITY.md
scripts/
  run_simulation.ps1
  run_simulation.bat
Week_3_Final_Report.docx
README.md
.gitignore
```

## Run
From the project directory:

```powershell
python src/app_simulator.py
python src/monitor.py
python src/log_analyzer.py
python src/security_audit.py
```

Or on Windows:

```powershell
.\scriptsun_simulation.ps1
```

The scripts use only Python's standard library.

## Important
This is a simulation and does not claim that live AWS resources were deployed. No AWS account is required.
