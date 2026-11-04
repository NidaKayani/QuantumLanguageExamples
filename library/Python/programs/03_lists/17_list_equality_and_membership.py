"""Compare lists for equality, ordering and membership."""

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a == b:", a == b, "| a is b:", a is b, "| a is c:", a is c)
print("[1, 2] < [1, 3]:", [1, 2] < [1, 3])
print("[1, 2] < [1, 2, 0]:", [1, 2] < [1, 2, 0])
print("[2] > [1, 99]:", [2] > [1, 99])
print("['a', 'b'] < ['a', 'c']:", ["a", "b"] < ["a", "c"])
print("[1, 2] == (1, 2):", [1, 2] == (1, 2), "| list((1, 2)) == [1, 2]:", list((1, 2)) == [1, 2])

nested = [[1, 2], [3, 4]]
print("[3, 4] in nested:", [3, 4] in nested)
print("3 in nested:", 3 in nested)
print("3 in flattened:", 3 in [x for row in nested for x in row])

try:
    [1, 2] < [1, "x"]
except TypeError as e:
    print("TypeError:", e)


def is_sublist(small, big):
    n = len(small)
    return any(big[i:i + n] == small for i in range(len(big) - n + 1))


print("is_sublist([3, 4], [1, 2, 3, 4, 5]):", is_sublist([3, 4], [1, 2, 3, 4, 5]))
print("is_sublist([4, 3], [1, 2, 3, 4, 5]):", is_sublist([4, 3], [1, 2, 3, 4, 5]))

allowed = ["read", "write"]
for perm in ("read", "delete"):
    print(f"{perm!r} allowed: {perm in allowed}, not in: {perm not in allowed}")

print("same elements ignoring order:", sorted([3, 1, 2]) == sorted([2, 3, 1]))
print("float in list:", 1.0 in [1, 2], "| True in [1]:", True in [1])
nan = float("nan")
print("nan in [nan] (identity):", nan in [nan], "| nan == nan:", nan == nan)
