"""Unpack tuples with starred targets, nested patterns and in loops."""

point = (3, 4)
x, y = point
print(f"x={x}, y={y}")

first, *middle, last = [1, 2, 3, 4, 5, 6]
print("first:", first, "middle:", middle, "last:", last)

head, *tail = "hello"
print("head:", head, "tail:", tail)

*init, final = range(4)
print("init:", init, "final:", final)

# nested unpacking
record = ("Ada", (1815, 12, 10), ["math", "computing"])
name, (year, month, day), (field1, field2) = record
print(f"{name} born {year}-{month:02d}-{day:02d}, fields: {field1}, {field2}")

# unpacking in for loops
pairs = [("a", 1), ("b", 2), ("c", 3)]
for letter, number in pairs:
    print(letter * number)

for i, (letter, number) in enumerate(pairs, start=1):
    print(f"{i}. {letter}={number}")

# returning multiple values
def min_max_mean(values):
    return min(values), max(values), sum(values) / len(values)

lo, hi, mean = min_max_mean([4, 8, 15, 16, 23, 42])
print(f"min={lo} max={hi} mean={mean:.2f}")

# ignoring values with underscore
_, important, _ = ("skip", "keep", "skip")
print("important:", important)

# unpacking into function calls
def area(w, h):
    return w * h

dims = (7, 6)
print("area:", area(*dims))
merged = [*range(3), *"ab", *(9,)]
print("merged:", merged)
