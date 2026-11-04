"""Classic number-theory recursions: gcd, extended gcd, fast power, digit sums."""

import math


def gcd(a: int, b: int) -> int:
    return a if b == 0 else gcd(b, a % b)


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y


def power(base: int, exp: int, mod: int | None = None) -> int:
    if exp == 0:
        return 1 if mod is None else 1 % mod
    half = power(base, exp // 2, mod)
    result = half * half
    if exp % 2:
        result *= base
    return result if mod is None else result % mod


def digital_root(n: int) -> int:
    return n if n < 10 else digital_root(sum(map(int, str(n))))


def to_base(n: int, b: int) -> str:
    digits = "0123456789ABCDEF"
    return digits[n] if n < b else to_base(n // b, b) + digits[n % b]


for a, b in [(48, 18), (1071, 462), (17, 5), (100, 75)]:
    g, x, y = extended_gcd(a, b)
    assert g == gcd(a, b) == math.gcd(a, b)
    print(f"gcd({a}, {b}) = {g} = {a}*{x} + {b}*{y}")

g, inv, _ = extended_gcd(17, 3120)
print("modular inverse of 17 mod 3120:", inv % 3120)

print("2^64 =", power(2, 64))
print("3^200 mod 1000 =", power(3, 200, 1000), "| builtin:", pow(3, 200, 1000))
print("digital roots:", [digital_root(n) for n in [0, 9, 38, 12345, 999999999]])
for n in [255, 1000, 4096]:
    print(f"{n} -> bin {to_base(n, 2)}, hex {to_base(n, 16)}, base7 {to_base(n, 7)}")
