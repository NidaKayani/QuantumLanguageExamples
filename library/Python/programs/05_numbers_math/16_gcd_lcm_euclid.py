"""Compute GCD and LCM with Euclid's algorithm and the extended variant."""

import math
from functools import reduce


def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def gcd_recursive(a, b):
    return a if b == 0 else gcd_recursive(b, a % b)


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


pairs = [(48, 18), (1071, 462), (17, 5), (0, 9), (270, 192)]
for a, b in pairs:
    g, x, y = extended_gcd(a, b)
    print(f"gcd({a}, {b}) = {gcd(a, b)} (recursive {gcd_recursive(a, b)}, math {math.gcd(a, b)});"
          f" {a}*{x} + {b}*{y} = {a * x + b * y}")

for a, b in ((4, 6), (21, 6), (7, 13)):
    print(f"lcm({a}, {b}) = {lcm(a, b)} (math {math.lcm(a, b)})")

nums = [12, 18, 30, 42]
print("gcd of list:", reduce(gcd, nums), "| lcm of list:", reduce(lcm, nums))
print("smallest number divisible by 1..20:", reduce(lcm, range(1, 21)))


def simplify(num, den):
    g = gcd(num, den)
    return num // g, den // g


for frac in ((84, 126), (100, 75), (17, 51)):
    print(f"{frac[0]}/{frac[1]} -> {'/'.join(map(str, simplify(*frac)))}")

# coprime counting
coprime = sum(1 for k in range(1, 37) if gcd(k, 36) == 1)
print("numbers coprime to 36 below 36:", coprime)

# solve a linear diophantine equation 35x + 15y = 5
g, x, y = extended_gcd(35, 15)
print(f"35x + 15y = {g}: x={x}, y={y}")
