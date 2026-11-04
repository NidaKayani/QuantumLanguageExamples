"""Sieve of Eratosthenes, a segmented sieve, and prime-counting statistics."""
from bisect import bisect_right
from math import isqrt, log


def sieve(limit):
    is_prime = bytearray([1]) * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if is_prime[p]:
            is_prime[p * p::p] = bytearray(len(range(p * p, limit + 1, p)))
    return [i for i, flag in enumerate(is_prime) if flag]


def segmented(lo, hi):
    base = sieve(isqrt(hi) + 1)
    mark = [True] * (hi - lo + 1)
    for p in base:
        start = max(p * p, (lo + p - 1) // p * p)
        for m in range(start, hi + 1, p):
            mark[m - lo] = False
    return [lo + i for i, ok in enumerate(mark) if ok and lo + i > 1]


def main():
    primes = sieve(100_000)
    print("Primes below 60:", [p for p in primes if p < 60])
    print("pi(10^5) =", len(primes))
    print(f"{'x':>7} {'pi(x)':>6} {'x/ln x':>8} {'ratio':>6}")
    for x in (100, 1_000, 10_000, 100_000):
        count = bisect_right(primes, x)
        approx = x / log(x)
        print(f"{x:>7} {count:>6} {approx:>8.1f} {count / approx:>6.3f}")
    window = segmented(1_000_000, 1_000_200)
    print("Primes in [1000000, 1000200]:", window)
    gaps = [b - a for a, b in zip(primes, primes[1:])]
    big = max(gaps)
    where = gaps.index(big)
    print(f"Largest gap below 10^5: {big} between {primes[where]} and {primes[where + 1]}")
    last_digits = {d: sum(1 for p in primes if p % 10 == d) for d in (1, 3, 7, 9)}
    print("Last-digit distribution:", last_digits)


if __name__ == "__main__":
    main()
