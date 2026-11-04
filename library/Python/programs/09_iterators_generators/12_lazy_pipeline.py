"""A lazy data-processing pipeline chained from small generator stages."""
import re


LOG = """\
2024-01-01 10:00:01 INFO  user=ann action=login
2024-01-01 10:00:05 ERROR user=bob action=upload size=512
2024-01-01 10:01:10 INFO  user=ann action=upload size=2048
malformed line here
2024-01-01 10:02:00 WARN  user=cid action=login
2024-01-01 10:03:30 INFO  user=bob action=upload size=1024
2024-01-01 10:04:00 ERROR user=ann action=delete
"""

LINE_RE = re.compile(r"(\S+) (\S+) (\w+)\s+(.*)")


def read_lines(text):
    for line in text.splitlines():
        print(f"    [read] {line[:24]}")
        yield line


def parse(lines):
    for line in lines:
        m = LINE_RE.match(line)
        if m:
            date, time, level, rest = m.groups()
            fields = dict(pair.split("=") for pair in rest.split())
            yield {"time": time, "level": level, **fields}


def where(records, **criteria):
    for r in records:
        if all(r.get(k) == v for k, v in criteria.items()):
            yield r


def take(n, iterable):
    for i, item in enumerate(iterable):
        if i >= n:
            return
        yield item


print("First upload only (watch how little is read):")
pipeline = take(1, where(parse(read_lines(LOG)), action="upload"))
for record in pipeline:
    print("  ->", record)

uploads = where(parse(LOG.splitlines()), action="upload")
total = sum(int(r["size"]) for r in uploads)
print("total uploaded bytes:", total)
errors = [r["user"] for r in where(parse(LOG.splitlines()), level="ERROR")]
print("users with errors:", errors)
