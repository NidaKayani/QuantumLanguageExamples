"""Divisor functions tau and sigma, highly composite numbers, and multiplicativity checks."""
from itertools import product
from math import gcd, prod


def factor(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors(n):
    f = factor(n)
    powers = [[p**k for k in range(e + 1)] for p, e in f.items()]
    return sorted(prod(combo) for combo in product(*powers))


def tau(n):
    return prod(e + 1 for e in factor(n).values())


def sigma(n, k=1):
    return prod((p ** (k * (e + 1)) - 1) // (p**k - 1) for p, e in factor(n).items())


def main():
    for n in (12, 28, 60, 97, 360, 1001):
        ds = divisors(n)
        assert len(ds) == tau(n) and sum(ds) == sigma(n)
        print(f"{n:>5}: tau={tau(n):>3} sigma={sigma(n):>5} sigma2={sigma(n, 2):>8} divisors={ds}")
    record, champions = 0, []
    for n in range(1, 10_001):
        t = tau(n)
        if t > record:
            record = t
            champions.append((n, t))
    print("Highly composite numbers up to 10000:")
    print("  " + ", ".join(f"{n}({t})" for n, t in champions))
    pairs = [(a, b) for a in range(2, 40) for b in range(2, 40) if gcd(a, b) == 1]
    mult = all(tau(a * b) == tau(a) * tau(b) and sigma(a * b) == sigma(a) * sigma(b)
               for a, b in pairs)
    print(f"Multiplicative on {len(pairs)} coprime pairs:", mult)
    print("tau(12*18) vs tau(12)*tau(18):", tau(12 * 18), tau(12) * tau(18))
    triangle = next(t for t in (k * (k + 1) // 2 for k in range(1, 20_000)) if tau(t) > 100)
    print("First triangular number with over 100 divisors:", triangle)


if __name__ == "__main__":
    main()
