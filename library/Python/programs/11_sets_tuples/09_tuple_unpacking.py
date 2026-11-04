"""Tuple unpacking in assignment, swapping, loops and nested structures."""

x, y = 10, 20
print("x, y =", x, y)
x, y = y, x
print("swapped:", x, y)

a = b = c = 0
a, b, c = "XYZ"
print("unpack string:", a, b, c)

(name, (lat, lon)), elevation = ("Everest", (27.9881, 86.9250)), 8849
print(f"{name}: lat={lat}, lon={lon}, elevation={elevation} m")

pairs = [(1, "one"), (2, "two"), (3, "three")]
for number, word in pairs:
    print(f"  {number} -> {word}")

for index, (number, word) in enumerate(pairs, start=1):
    print(f"  #{index}: {word.upper()} ({number})")

def min_max_mean(values):
    return min(values), max(values), sum(values) / len(values)

lo, hi, mean = min_max_mean([4, 8, 15, 16, 23, 42])
print(f"lo={lo} hi={hi} mean={mean:.2f}")

table = {"alice": (30, "Paris"), "bob": (25, "Rome")}
for person, (age, city) in sorted(table.items()):
    print(f"{person} is {age} and lives in {city}")

try:
    p, q = (1, 2, 3)
except ValueError as exc:
    print("unpack error:", exc)

# Fibonacci via simultaneous assignment
f0, f1 = 0, 1
seq = []
for _ in range(12):
    seq.append(f0)
    f0, f1 = f1, f0 + f1
print("fibonacci:", seq)
