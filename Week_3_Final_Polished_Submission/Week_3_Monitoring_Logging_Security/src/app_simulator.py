import json, random, time
from datetime import datetime, timezone
from pathlib import Path

LOG = Path(__file__).resolve().parents[1] / "logs" / "application.log"

def write_log(level, event, **extra):
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": level,
        "service": "cloud-demo-app",
        "event": event,
        **extra
    }
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")

def main():
    random.seed(42)
    LOG.parent.mkdir(exist_ok=True)
    for i in range(20):
        latency = random.randint(80, 700)
        error = random.random() < 0.12
        if error:
            write_log("ERROR", "request_failed", request_id=f"REQ-{i+1:04d}",
                      status_code=500, latency_ms=latency)
        else:
            write_log("INFO", "request_completed", request_id=f"REQ-{i+1:04d}",
                      status_code=200, latency_ms=latency)
        time.sleep(0.1)
    write_log("INFO", "health_check", status_code=200, latency_ms=35)
    print(f"Application simulation complete. Log written to {LOG}")

if __name__ == "__main__":
    main()
