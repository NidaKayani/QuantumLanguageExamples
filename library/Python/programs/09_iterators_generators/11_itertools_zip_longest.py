"""Pairing uneven iterables with zip, zip(strict=True), and itertools.zip_longest."""
from itertools import zip_longest

names = ["Ann", "Bob", "Cid", "Dee"]
scores = [88, 92]
print("zip:", list(zip(names, scores)))
print("zip_longest:", list(zip_longest(names, scores)))
print("fillvalue:", list(zip_longest(names, scores, fillvalue=0)))

try:
    list(zip(names, scores, strict=True))
except ValueError as exc:
    print("strict zip error:", exc)

col1 = ["id", "1", "2", "3"]
col2 = ["name", "alpha", "beta"]
col3 = ["score", "9.5"]
for row in zip_longest(col1, col2, col3, fillvalue="-"):
    print(" | ".join(f"{cell:<5}" for cell in row))


def grouper(iterable, n, fill=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fill)


print("grouper:", list(grouper("ABCDEFG", 3, "x")))

a = [1, 2, 3, 4, 5]
b = [10, 20, 30]
print("elementwise sum:", [x + y for x, y in zip_longest(a, b, fillvalue=0)])
v1, v2 = "kitten", "sitting"
diff = sum(1 for x, y in zip_longest(v1, v2) if x != y)
print(f"positional differences {v1!r} vs {v2!r}:", diff)
