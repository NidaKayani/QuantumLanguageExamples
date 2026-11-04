"""Collatz sequences: memoized stopping times, record holders and peak values."""
from collections import Counter

LIMIT = 30_000
cache = {1: 0}


def steps(n):
    path = []
    while n not in cache:
        path.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    base = cache[n]
    for i, m in enumerate(reversed(path), 1):
        cache[m] = base + i
    return cache[path[0]] if path else base


def sequence(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq


print("Sequence of 27 has", len(sequence(27)) - 1, "steps, peak", max(sequence(27)))
print("Start of 27:", sequence(27)[:16], "...")

records = []
best = -1
for n in range(1, LIMIT + 1):
    s = steps(n)
    if s > best:
        best = s
        records.append((n, s))
print(f"Stopping-time records below {LIMIT}:")
for n, s in records:
    print(f"  n={n:>6} steps={s}")

peak_records = []
peak_best = 0
for n in range(1, 2000):
    p = max(sequence(n))
    if p > peak_best:
        peak_best = p
        peak_records.append((n, p))
print("Peak-value records below 2000:", peak_records[-6:])

histogram = Counter(steps(n) // 25 * 25 for n in range(1, LIMIT + 1))
print("Distribution of stopping times:")
for bucket in sorted(histogram):
    print(f"  {bucket:>3}-{bucket + 24:<3} {histogram[bucket]:>5} {'*' * (histogram[bucket] // 200)}")
print("Cached values:", len(cache))
