"""Unpack lists with starred expressions and splat lists into calls."""

values = [10, 20, 30, 40, 50]

first, second, *rest = values
print(first, second, rest)

*front, last = values
print(front, last)

a, *mid, z = values
print(a, mid, z)

head, *tail = [1]
print("single element:", head, tail)

combined = [*values[:2], 99, *values[-2:]]
print("combined:", combined)

matrix_rows = [[1, 2], [3, 4], [5, 6]]
print("columns via zip(*rows):", list(zip(*matrix_rows)))


def describe(x, y, z):
    return f"x={x}, y={y}, z={z}"


print(describe(*[1, 2, 3]))
print(describe(*"abc"))


def average(*nums):
    return sum(nums) / len(nums) if nums else 0.0


print("average:", average(*values), "| empty:", average())

print("max of list:", max(*values), "| print with sep:", end=" ")
print(*values, sep=" | ")

# swapping elements in a list
items = ["a", "b", "c", "d"]
items[0], items[-1] = items[-1], items[0]
print("swapped:", items)

# rotate using unpacking
first_item, *others = items
items = [*others, first_item]
print("rotated:", items)

nested = [("ann", [90, 85, 77]), ("bob", [60, 75])]
for name, (best, *others) in nested:
    print(f"{name}: best={best} others={others}")
