"""Find, extract and substitute text with regular expressions."""

import re

log = """2024-01-15 10:23:01 ERROR db: connection refused (code=111)
2024-01-15 10:23:05 INFO web: request /home took 35ms
2024-01-15 10:24:12 WARNING web: slow request /search took 1250ms
2024-01-16 08:00:00 ERROR auth: invalid token for user=alice
2024-01-16 08:01:30 INFO web: request /about took 12ms"""

pattern = re.compile(r"^(\d{4}-\d{2}-\d{2}) (\S+) (\w+) (\w+): (.*)$", re.MULTILINE)
for date, time, level, component, message in pattern.findall(log):
    if level != "INFO":
        print(f"{date} {level:<7} [{component}] {message}")

durations = [int(ms) for ms in re.findall(r"took (\d+)ms", log)]
print("durations:", durations, "avg:", sum(durations) / len(durations))

m = re.search(r"user=(?P<user>\w+)", log)
print("user found:", m.group("user"), "at span", m.span())

print(re.sub(r"\d{2}:\d{2}:\d{2}", "HH:MM:SS", log.splitlines()[0]))
print(re.sub(r"(\d+)ms", lambda mm: f"{int(mm.group(1)) / 1000:.3f}s", log.splitlines()[2]))

print(re.split(r"[,;\s]+", "a, b;c  d,,e"))

phone_re = re.compile(r"\(?(\d{3})\)?[-. ]?(\d{3})[-. ]?(\d{4})")
for phone in ("(555) 123-4567", "555.987.6543", "5551112222", "12-34"):
    if mm := phone_re.fullmatch(phone):
        print(f"{phone:16} -> {'-'.join(mm.groups())}")
    else:
        print(f"{phone:16} -> invalid")

words = re.findall(r"\b[A-Z]+\b", log)
print("uppercase words:", sorted(set(words)))
print("case-insensitive count of 'request':", len(re.findall("REQUEST", log, re.IGNORECASE)))
