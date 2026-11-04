"""Parse web-server access logs with a verbose regex and summarise traffic."""
import re
from collections import Counter, defaultdict
from statistics import median

LOG = """\
192.168.1.10 - - [12/Mar/2024:10:15:32 +0000] "GET /index.html HTTP/1.1" 200 5120 0.012
192.168.1.11 - - [12/Mar/2024:10:15:40 +0000] "GET /api/users HTTP/1.1" 200 830 0.087
10.0.0.5 - admin [12/Mar/2024:10:16:01 +0000] "POST /api/login HTTP/1.1" 401 112 0.034
10.0.0.5 - admin [12/Mar/2024:10:16:09 +0000] "POST /api/login HTTP/1.1" 200 240 0.041
192.168.1.10 - - [12/Mar/2024:10:17:22 +0000] "GET /images/logo.png HTTP/1.1" 304 0 0.002
172.16.0.2 - - [12/Mar/2024:10:18:45 +0000] "GET /api/orders?page=2 HTTP/1.1" 500 98 1.250
192.168.1.11 - - [12/Mar/2024:11:02:13 +0000] "DELETE /api/users/42 HTTP/1.1" 204 0 0.120
this line is garbage and should be skipped
172.16.0.2 - - [12/Mar/2024:11:05:51 +0000] "GET /api/orders?page=3 HTTP/1.1" 200 4410 0.310
192.168.1.12 - - [12/Mar/2024:11:06:30 +0000] "GET /missing HTTP/1.1" 404 210 0.004
10.0.0.5 - admin [12/Mar/2024:11:30:00 +0000] "GET /api/users HTTP/1.1" 200 812 0.079
"""

LINE_RE = re.compile(r"""
    (?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+-\s+(?P<user>\S+)\s+
    \[(?P<day>\d{2})/(?P<month>\w{3})/(?P<year>\d{4}):(?P<hour>\d{2}):(?P<minute>\d{2}):\d{2}\s[+-]\d{4}\]\s+
    "(?P<method>[A-Z]+)\s(?P<path>[^\s?]+)(?:\?(?P<query>\S*))?\s[^"]+"\s+
    (?P<status>\d{3})\s+(?P<size>\d+)\s+(?P<seconds>[\d.]+)
""", re.VERBOSE)


def parse(log):
    good, bad = [], []
    for number, line in enumerate(log.splitlines(), 1):
        m = LINE_RE.match(line)
        if m:
            rec = m.groupdict()
            rec["status"] = int(rec["status"])
            rec["size"] = int(rec["size"])
            rec["seconds"] = float(rec["seconds"])
            good.append(rec)
        else:
            bad.append(number)
    return good, bad


def main():
    records, bad = parse(LOG)
    print(f"Parsed {len(records)} requests, skipped lines {bad}")
    status = Counter(r["status"] // 100 * 100 for r in records)
    print("Status classes:", {f"{k // 100}xx": v for k, v in sorted(status.items())})
    print("Requests per IP:", dict(Counter(r["ip"] for r in records).most_common()))
    by_path = defaultdict(list)
    for r in records:
        by_path[r["path"]].append(r["seconds"])
    print(f"{'path':<18}{'hits':>5}{'median s':>10}{'max s':>8}")
    for path, times in sorted(by_path.items(), key=lambda kv: -len(kv[1])):
        print(f"{path:<18}{len(times):>5}{median(times):>10.3f}{max(times):>8.3f}")
    errors = [f"{r['method']} {r['path']} -> {r['status']}" for r in records if r["status"] >= 400]
    print("Errors:", errors)
    per_hour = Counter(f"{r['hour']}:00" for r in records)
    print("Per hour:", dict(sorted(per_hour.items())))
    print("Total bytes:", sum(r["size"] for r in records))
    print("Authenticated users:", sorted({r["user"] for r in records if r["user"] != "-"}))


if __name__ == "__main__":
    main()
