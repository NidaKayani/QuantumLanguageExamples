"""Print geometric text patterns using nested loops."""

size = 5

print("Right triangle:")
for i in range(1, size + 1):
    print("*" * i)

print("\nNumber pyramid:")
for i in range(1, size + 1):
    left = "".join(str(j) for j in range(1, i + 1))
    right = left[-2::-1]
    print(" " * (size - i) + left + right)

print("\nHollow square:")
for r in range(size):
    line = ""
    for c in range(size):
        edge = r in (0, size - 1) or c in (0, size - 1)
        line += "#" if edge else " "
    print(line)

print("\nDiamond:")
for i in list(range(1, size + 1)) + list(range(size - 1, 0, -1)):
    print(" " * (size - i) + "*" * (2 * i - 1))

print("\nCheckerboard:")
for r in range(4):
    print("".join("X" if (r + c) % 2 == 0 else "." for c in range(8)))

print("\nPascal's triangle:")
row = [1]
for _ in range(7):
    print(" ".join(map(str, row)).center(30))
    row = [1] + [row[k] + row[k + 1] for k in range(len(row) - 1)] + [1]
