import json, random, time
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
CFG = json.loads((BASE / "config" / "monitoring.json").read_text(encoding="utf-8"))
OUT = BASE / "logs" / "monitoring.jsonl"

def main():
    random.seed(7)
    t = CFG["thresholds"]
    alerts = []
    for i in range(CFG["samples"]):
        sample = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "cpu_percent": random.randint(35, 94),
            "memory_percent": random.randint(45, 91),
            "disk_percent": random.randint(40, 88),
            "latency_ms": random.randint(100, 750),
            "error_rate_percent": round(random.uniform(0, 9), 2)
        }
        triggered = []
        for key, value in sample.items():
            if key in t and value > t[key]:
                triggered.append(f"{key}>{t[key]}")
        sample["alerts"] = triggered
        alerts.extend(triggered)
        with OUT.open("a", encoding="utf-8") as f:
            f.write(json.dumps(sample) + "\n")
        print(sample)
        time.sleep(0.15)
    print(f"\nMonitoring complete. Samples: {CFG['samples']}; alerts: {len(alerts)}")
    if alerts:
        print("Alert summary:", ", ".join(alerts))

if __name__ == "__main__":
    main()
