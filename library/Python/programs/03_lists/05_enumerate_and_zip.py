"""Iterate with enumerate and zip, including strict and unequal lengths."""

from itertools import zip_longest

colors = ["red", "green", "blue"]
for i, color in enumerate(colors):
    print(i, color)
for i, color in enumerate(colors, start=1):
    print(f"{i}. {color}")

names = ["Ann", "Ben", "Cid", "Dee"]
scores = [91, 78, 85]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
print("zip stops at shortest:", list(zip(names, scores)))
print("zip_longest:", list(zip_longest(names, scores, fillvalue=0)))

try:
    list(zip(names, scores, strict=True))
except ValueError as e:
    print("strict zip error:", e)

# unzip with zip(*...)
pairs = [("x", 1), ("y", 2), ("z", 3)]
letters, numbers = zip(*pairs)
print("unzipped:", letters, numbers)

# build a dict from two lists
lookup = dict(zip(names, scores))
print("lookup:", lookup)

# parallel iteration over three sequences
xs, ys, zs = [1, 2, 3], [4, 5, 6], [7, 8, 9]
print("column sums:", [a + b + c for a, b, c in zip(xs, ys, zs)])

# pairwise differences with zip on offsets
temps = [12, 15, 11, 18, 21, 19]
diffs = [b - a for a, b in zip(temps, temps[1:])]
print("daily changes:", diffs)

# find indices of maximum values
values = [3, 9, 2, 9, 5]
peak = max(values)
print("peak positions:", [i for i, v in enumerate(values) if v == peak])
