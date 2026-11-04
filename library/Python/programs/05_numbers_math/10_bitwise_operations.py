"""Manipulate integers with bitwise operators, masks and flags."""

a, b = 0b1100, 0b1010
print(f"a={a:04b} b={b:04b}")
print(f"a & b = {a & b:04b}")
print(f"a | b = {a | b:04b}")
print(f"a ^ b = {a ^ b:04b}")
print(f"~a = {~a} (two's complement)")
print(f"a << 2 = {a << 2:b}, a >> 2 = {a >> 2:b}")
print("-16 >> 2 =", -16 >> 2)

READ, WRITE, EXEC = 4, 2, 1
perms = READ | WRITE
print("has write:", bool(perms & WRITE), "| has exec:", bool(perms & EXEC))
perms |= EXEC
perms &= ~WRITE
print("after toggles:", f"{perms:03b}")


def octal_perms(mode):
    out = ""
    for shift in (6, 3, 0):
        bits = (mode >> shift) & 7
        out += ("r" if bits & 4 else "-") + ("w" if bits & 2 else "-") + ("x" if bits & 1 else "-")
    return out


for mode in (0o755, 0o644, 0o600, 0o777):
    print(f"{mode:o} -> {octal_perms(mode)}")

n = 0b10110100
print("lowest set bit:", n & -n, "| clear lowest:", f"{n & (n - 1):b}")
print("is power of two:", [x for x in range(1, 70) if x & (x - 1) == 0])
print("popcount:", bin(n).count("1"), n.bit_count())

# subsets via bitmasks
items = ["a", "b", "c"]
subsets = [[items[i] for i in range(3) if mask >> i & 1] for mask in range(1 << 3)]
print("subsets:", subsets)

# xor tricks
x, y = 17, 42
x ^= y
y ^= x
x ^= y
print("xor swap:", x, y)
nums = [4, 7, 2, 7, 4, 9, 2]
single = 0
for v in nums:
    single ^= v
print("unpaired element:", single)

gray = [i ^ (i >> 1) for i in range(8)]
print("gray codes:", [f"{g:03b}" for g in gray])
