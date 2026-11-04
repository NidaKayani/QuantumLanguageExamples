"""Explore for loops over ranges with different starts, stops and steps."""

print("range(5):", list(range(5)))
print("range(2, 10):", list(range(2, 10)))
print("range(0, 20, 3):", list(range(0, 20, 3)))
print("range(10, 0, -2):", list(range(10, 0, -2)))

# sum of squares
total = 0
for i in range(1, 11):
    total += i * i
print("sum of squares 1..10:", total)

# multiplication table
print("\n    " + "".join(f"{j:4d}" for j in range(1, 7)))
for i in range(1, 7):
    row = f"{i:2d} |"
    for j in range(1, 7):
        row += f"{i * j:4d}"
    print(row)

# triangle pattern
print()
for n in range(1, 6):
    print(" " * (5 - n) + "*" * (2 * n - 1))

# iterating over a string and a tuple
for ch in "loop":
    print(ch, end="-")
print()
for animal in ("cat", "dog", "owl"):
    print(f"{animal} has {len(animal)} letters")

# range objects are lazy and support len/indexing
r = range(100, 1000, 7)
print("len:", len(r), "first:", r[0], "last:", r[-1], "contains 107:", 107 in r)
