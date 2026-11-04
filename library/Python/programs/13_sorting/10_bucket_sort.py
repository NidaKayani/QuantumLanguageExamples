"""Bucket sort for uniformly distributed floats and bounded scores."""

from math import floor


def bucket_sort(values, bucket_count=10):
    if not values:
        return []
    lo, hi = min(values), max(values)
    span = (hi - lo) or 1
    buckets = [[] for _ in range(bucket_count)]
    for v in values:
        idx = min(int((v - lo) / span * bucket_count), bucket_count - 1)
        buckets[idx].append(v)
    for i, b in enumerate(buckets):
        b.sort()
    return buckets, [v for b in buckets for v in b]


floats = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434, 0.42, 0.33, 0.78, 0.05, 0.99, 0.5]
buckets, result = bucket_sort(floats, 5)
for i, b in enumerate(buckets):
    print(f"bucket {i}: {b}")
print("sorted:", result)

scores = [72, 95, 64, 88, 79, 91, 55, 83, 70, 99, 61, 87]
by_decade = {}
for s in scores:
    by_decade.setdefault(floor(s / 10) * 10, []).append(s)
for decade in sorted(by_decade):
    bar = " ".join(map(str, sorted(by_decade[decade])))
    print(f"{decade}-{decade + 9}: {bar}")

_, ordered = bucket_sort(scores, 4)
print("scores sorted:", ordered)
print("median:", (ordered[len(ordered) // 2 - 1] + ordered[len(ordered) // 2]) / 2)
