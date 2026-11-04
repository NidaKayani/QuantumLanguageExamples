"""Evaluate boolean operators, short-circuiting and truth tables."""

from itertools import product

print(f"{'A':6}{'B':6}{'and':6}{'or':6}{'xor':6}{'nand':6}")
for a, b in product([False, True], repeat=2):
    row = [a, b, a and b, a or b, a != b, not (a and b)]
    print("".join(f"{str(v):6}" for v in row))

# and/or return operands, not just bools
print(0 or "default")
print("value" and 42)
print(None or [] or "last")
print(1 and 2 and 3)

# short-circuit avoids evaluating the right side
calls = []


def check(name, result):
    calls.append(name)
    return result


check("a", False) and check("b", True)
check("c", True) or check("d", True)
print("functions actually called:", calls)

# all / any
nums = [2, 4, 6, 9]
print("all even:", all(n % 2 == 0 for n in nums))
print("any odd:", any(n % 2 for n in nums))
print("all([]):", all([]), "any([]):", any([]))

# bools are ints
print("True + True =", True + True, "| sum of flags:", sum([True, False, True, True]))

# De Morgan's laws hold for every combination
ok = all((not (p and q)) == (not p or not q) and (not (p or q)) == (not p and not q)
         for p, q in product([False, True], repeat=2))
print("De Morgan verified:", ok)
