"""Extended iterable unpacking with starred targets."""

first, *rest = [1, 2, 3, 4, 5]
print("first:", first, "rest:", rest)

*init, last = "python"
print("init:", init, "last:", last)

head, *middle, tail = range(10)
print("head:", head, "middle:", middle, "tail:", tail)

a, *b = [99]
print("a:", a, "b (empty):", b)

records = [
    ("login", "alice", "2024-01-01"),
    ("purchase", "bob", "book", 12.5, "2024-01-02"),
    ("logout", "alice", "2024-01-03"),
    ("purchase", "carol", "pen", 1.25, "2024-01-04"),
]
for kind, user, *details, date in records:
    extra = f" details={details}" if details else ""
    print(f"{date} {kind:<8} {user}{extra}")

combined = [*range(3), *"ab", *(10, 20)]
print("splat into list:", combined)

merged_set = {*[1, 2], *(2, 3), *{3, 4}}
print("splat into set:", sorted(merged_set))

def total(*nums):
    return sum(nums)

values = (1, 2, 3)
print("call with *values:", total(*values, 4))

(x, *ys), z = [1, 2, 3], 4
print("nested star:", x, ys, z)

matrix = [[1, 2, 3], [4, 5, 6]]
transposed = list(zip(*matrix))
print("transposed via zip(*m):", transposed)
