"""Big-integer factorials: exact values, trailing zeros, Legendre's formula and binomials."""
import math
from functools import reduce
from operator import mul


def factorial_product(n):
    return reduce(mul, range(1, n + 1), 1)


def trailing_zeros(n):
    count, power = 0, 5
    while power <= n:
        count += n // power
        power *= 5
    return count


def legendre(n, p):
    exponent = 0
    while n:
        n //= p
        exponent += n
    return exponent


def last_nonzero_digit(n):
    f = math.factorial(n)
    while f % 10 == 0:
        f //= 10
    return f % 10


def main():
    f100 = factorial_product(100)
    assert f100 == math.factorial(100)
    text = str(f100)
    print(f"100! has {len(text)} digits:")
    for i in range(0, len(text), 50):
        print("  " + text[i:i + 50])
    print("Digit sum of 100!:", sum(map(int, text)))
    actual = len(text) - len(text.rstrip("0"))
    print(f"Trailing zeros of 100!: {trailing_zeros(100)} (counted in string: {actual})")
    for n in (1000, 10**6, 10**12):
        print(f"Trailing zeros of {n}!: {trailing_zeros(n)}")
    print("Exponent of primes in 50!:", {p: legendre(50, p) for p in (2, 3, 5, 7, 11, 13, 47)})
    print("Last nonzero digit of n! for n=1..15:", [last_nonzero_digit(n) for n in range(1, 16)])
    print("C(100, 50) =", math.comb(100, 50))
    print("P(20, 5) =", math.perm(20, 5))
    stirling = math.sqrt(2 * math.pi * 100) * (100 / math.e) ** 100
    print(f"Stirling estimate / exact for 100!: {stirling / f100:.6f}")
    print("1000! digit count:", len(str(math.factorial(1000))))


if __name__ == "__main__":
    main()
