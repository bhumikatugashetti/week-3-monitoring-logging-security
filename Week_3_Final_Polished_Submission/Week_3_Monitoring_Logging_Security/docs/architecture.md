# Architecture – Week 3 Simulation

```text
                 +----------------------+
                 |   Simulated Users     |
                 +----------+-----------+
                            |
                            v
                 +----------------------+
                 | Application Simulator |
                 +----------+-----------+
                            |
                            v
                 +----------------------+
                 | Structured JSON Logs  |
                 +----------+-----------+
                            |
              +-------------+-------------+
              |                           |
              v                           v
     +-------------------+      +-------------------+
     | Monitoring Engine |      | Log Analyzer      |
     | Metrics/Alerts    |      | Errors/Latency    |
     +---------+---------+      +-------------------+
               |
               v
       +-------------------+
       | Security Audit    |
       | Policy Controls   |
       +-------------------+
```

The design represents a cloud operations workflow: application activity produces structured logs;
monitoring evaluates operational metrics against thresholds; log analysis summarizes application
events; and security auditing checks configuration controls.
