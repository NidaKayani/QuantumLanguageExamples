"""Goldbach partitions, twin/cousin/sexy prime pairs, and primes in arithmetic progression."""
from bisect import bisect_left
from itertools import takewhile


def primes_upto(n):
    flags = [True] * (n + 1)
    flags[0] = flags[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if flags[i]:
            flags[i * i::i] = [False] * len(flags[i * i::i])
    return flags


def goldbach(n, flags, primes):
    return [(p, n - p) for p in takewhile(lambda q: q <= n // 2, primes) if flags[n - p]]


def prime_pairs(primes, flags, gap):
    return [(p, p + gap) for p in primes if p + gap < len(flags) and flags[p + gap]]


def main():
    LIMIT = 20_000
    flags = primes_upto(LIMIT)
    primes = [i for i, f in enumerate(flags) if f]
    for n in (28, 100, 1000):
        parts = goldbach(n, flags, primes)
        print(f"{n}: {len(parts)} partitions, e.g. {parts[:4]}")
    assert all(any(flags[n - p] for p in takewhile(lambda q: q <= n // 2, primes))
               for n in range(4, LIMIT + 1, 2))
    print(f"Goldbach verified for even numbers 4..{LIMIT}")
    counts = {n: len(goldbach(n, flags, primes)) for n in range(4, 2001, 2)}
    record = max(counts, key=lambda n: (counts[n], -n))
    print(f"Most partitions below 2000: {record} with {counts[record]}")
    for name, gap in (("twin", 2), ("cousin", 4), ("sexy", 6)):
        pairs = prime_pairs(primes, flags, gap)
        print(f"{name:>6} pairs below {LIMIT}: {len(pairs):4d}, last {pairs[-1]}")
    idx = bisect_left(primes, 10_000)
    print("First primes above 10000:", primes[idx:idx + 6])
    progression = next((p, d) for d in range(2, 500, 2) for p in primes[:200]
                       if all(p + k * d < len(flags) and flags[p + k * d] for k in range(6)))
    p, d = progression
    print("Six primes in arithmetic progression:", [p + k * d for k in range(6)])


if __name__ == "__main__":
    main()
