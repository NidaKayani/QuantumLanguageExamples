"""Lazy generator pipelines that parse, filter and aggregate web-server log lines."""
import re
from collections import Counter
from itertools import islice

LOG = """\
10.0.0.1 GET /index.html 200 512
10.0.0.2 GET /about.html 200 1024
10.0.0.1 POST /login 302 64
10.0.0.3 GET /missing 404 0
# comment line
10.0.0.2 GET /index.html 200 512
10.0.0.4 GET /api/items 500 128

10.0.0.1 GET /api/items 200 2048
10.0.0.3 GET /index.html 304 0
10.0.0.5 DELETE /api/items/7 403 32
"""

LINE = re.compile(r"(?P<ip>\S+) (?P<method>[A-Z]+) (?P<path>\S+) (?P<status>\d{3}) (?P<size>\d+)")


def lines(text):
    yield from text.splitlines()


def non_blank(rows):
    return (r for r in rows if r.strip() and not r.startswith("#"))


def parse(rows):
    for r in rows:
        m = LINE.fullmatch(r)
        if m:
            rec = m.groupdict()
            rec["status"] = int(rec["status"])
            rec["size"] = int(rec["size"])
            yield rec


def where(records, **conditions):
    return (r for r in records if all(pred(r[k]) for k, pred in conditions.items()))


def records():
    return parse(non_blank(lines(LOG)))


print("First two records:")
for rec in islice(records(), 2):
    print("  ", rec)

errors = where(records(), status=lambda s: s >= 400)
print("Errors:", [(r["path"], r["status"]) for r in errors])

total_bytes = sum(r["size"] for r in where(records(), method=lambda m: m == "GET"))
print("Bytes served by GET:", total_bytes)

hits = Counter(r["path"] for r in records())
print("Top paths:", hits.most_common(2))

by_ip = Counter(r["ip"] for r in where(records(), status=lambda s: s < 400))
print("Successful requests per IP:", sorted(by_ip.items()))


def trace(name, it):
    for item in it:
        print(f"    {name} yields {item!r}")
        yield item


print("Laziness demo (only pulls what is needed):")
pipeline = trace("square", (x * x for x in trace("source", range(100))))
print("  first square above 10:", next(x for x in pipeline if x > 10))
