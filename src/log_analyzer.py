import json
from pathlib import Path
from collections import Counter

BASE = Path(__file__).resolve().parents[1]
LOG = BASE / "logs" / "application.log"

def main():
    if not LOG.exists():
        print("No application log found. Run app_simulator.py first.")
        return
    levels = Counter()
    status = Counter()
    latencies = []
    for line in LOG.read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        levels[r["level"]] += 1
        status[str(r.get("status_code", "unknown"))] += 1
        if "latency_ms" in r:
            latencies.append(r["latency_ms"])
    avg = sum(latencies) / len(latencies) if latencies else 0
    print("LOG ANALYSIS")
    print("============")
    print("Total events:", sum(levels.values()))
    print("Levels:", dict(levels))
    print("Status codes:", dict(status))
    print("Average latency (ms):", round(avg, 2))
    print("Errors:", levels.get("ERROR", 0))

if __name__ == "__main__":
    main()
