"""Parallel iteration with zip/enumerate producing tuples."""

from itertools import zip_longest

names = ["ann", "ben", "cid", "dee"]
scores = [88, 92, 79, 95]
grades = ["B", "A", "C", "A"]

for rank, (name, score, grade) in enumerate(zip(names, scores, grades), start=1):
    print(f"{rank}. {name:<4} {score:>3} {grade}")

pairs = list(zip(names, scores))
print("pairs:", pairs)

unzipped_names, unzipped_scores = zip(*pairs)
print("unzipped:", unzipped_names, unzipped_scores)

lookup = dict(zip(names, scores))
best = max(lookup.items(), key=lambda kv: kv[1])
print("best:", best)

short = [1, 2]
long = ["a", "b", "c", "d"]
print("zip truncates:", list(zip(short, long)))
print("zip_longest:", list(zip_longest(short, long, fillvalue=0)))

try:
    list(zip(short, long, strict=True))
except ValueError as exc:
    print("strict zip:", exc)

readings = [12, 15, 11, 18, 21, 19]
deltas = [b - a for a, b in zip(readings, readings[1:])]
print("deltas:", deltas)

windows = list(zip(readings, readings[1:], readings[2:]))
print("3-wide windows:", windows)
print("window averages:", [round(sum(w) / 3, 2) for w in windows])
