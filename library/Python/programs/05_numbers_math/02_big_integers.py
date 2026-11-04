"""Compute with arbitrary-precision integers: factorials, powers and digit counts."""

import math

f100 = math.factorial(100)
print("100! has", len(str(f100)), "digits")
print("100! =", f100)
print("trailing zeros:", len(str(f100)) - len(str(f100).rstrip("0")))

big = 2 ** 200
print("2**200 =", big)
print("bit_length:", big.bit_length(), "| digit sum:", sum(map(int, str(big))))

mersenne = 2 ** 127 - 1
print("2**127 - 1 =", mersenne)

fib = [0, 1]
while len(str(fib[-1])) < 50:
    fib.append(fib[-1] + fib[-2])
print(f"first 50-digit Fibonacci is F({len(fib) - 1}) = {fib[-1]}")

a = 123456789012345678901234567890
b = 987654321098765432109876543210
print("a * b =", a * b)
print("b // a =", b // a, "| b % a =", b % a)
print("gcd(a, b) =", math.gcd(a, b))
print("isqrt(a) =", math.isqrt(a), "| check:", math.isqrt(a) ** 2 <= a < (math.isqrt(a) + 1) ** 2)

print("comb(100, 50) =", math.comb(100, 50))
print("perm(20, 10) =", math.perm(20, 10))

n = 3 ** 100
print("3**100 in groups:", f"{n:,}")
print("negative big:", -(10 ** 30) // 7)
print("int <-> bytes:", n.to_bytes(20, "big").hex(), int.from_bytes(n.to_bytes(20, "big"), "big") == n)
print("float(2**1023) =", float(2 ** 1023))
try:
    float(10 ** 400)
except OverflowError as e:
    print("OverflowError:", e)
