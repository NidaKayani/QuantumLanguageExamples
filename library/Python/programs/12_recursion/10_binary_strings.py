"""Recursive generation of binary strings and Gray codes."""


def binary_strings(n: int) -> list[str]:
    if n == 0:
        return [""]
    shorter = binary_strings(n - 1)
    return ["0" + s for s in shorter] + ["1" + s for s in shorter]


def gray_code(n: int) -> list[str]:
    if n == 0:
        return [""]
    prev = gray_code(n - 1)
    return ["0" + s for s in prev] + ["1" + s for s in reversed(prev)]


def no_adjacent_ones(n: int, last: str = "0") -> list[str]:
    if n == 0:
        return [""]
    result = ["0" + s for s in no_adjacent_ones(n - 1, "0")]
    if last != "1":
        result += ["1" + s for s in no_adjacent_ones(n - 1, "1")]
    return result


print("binary strings of length 3:", binary_strings(3))

codes = gray_code(4)
print("4-bit Gray code:")
for i, code in enumerate(codes):
    print(f"  {i:2d} {code} ({int(code, 2):2d})")

diffs = [sum(a != b for a, b in zip(x, y)) for x, y in zip(codes, codes[1:] + codes[:1])]
print("each neighbour differs by one bit:", set(diffs) == {1})

for n in range(1, 9):
    print(f"n={n}: {len(no_adjacent_ones(n)):3d} strings with no '11'")
print("examples for n=4:", no_adjacent_ones(4))
