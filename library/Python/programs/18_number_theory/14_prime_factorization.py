"""Prime factorisation with trial division and Pollard's rho (deterministic starting points)."""
from collections import Counter
from math import gcd


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d, s = d // 2, s + 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def trial_division(n):
    factors = Counter()
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors[p] += 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        factors[n] += 1
    return factors


def pollard_rho(n):
    if n % 2 == 0:
        return 2
    for c in range(1, 50):
        x = y = 2
        d = 1
        f = lambda v: (v * v + c) % n
        while d == 1:
            x, y = f(x), f(f(y))
            d = gcd(abs(x - y), n)
        if d != n:
            return d
    raise ArithmeticError(f"rho failed for {n}")


def factorize(n, acc=None):
    acc = Counter() if acc is None else acc
    if n == 1:
        return acc
    if is_prime(n):
        acc[n] += 1
        return acc
    d = pollard_rho(n)
    factorize(d, acc)
    factorize(n // d, acc)
    return acc


def pretty(factors):
    return " * ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(factors.items()))


def main():
    for n in (360, 97, 1001, 2**10 * 3**5, 600851475143):
        assert trial_division(n) == factorize(n)
        print(f"{n} = {pretty(factorize(n))}")
    for n in (10**18 + 9, 2**64 + 1, 1_000_000_016_000_000_063, 123456789 * 987654321):
        print(f"{n} = {pretty(factorize(n))}")
    smooth = [n for n in range(2, 200) if max(trial_division(n)) <= 5]
    print("5-smooth numbers below 200:", smooth)
    omega = Counter(sum(trial_division(n).values()) for n in range(2, 5_001))
    print("Distribution of Omega(n) for n <= 5000:", dict(sorted(omega.items())))


if __name__ == "__main__":
    main()
