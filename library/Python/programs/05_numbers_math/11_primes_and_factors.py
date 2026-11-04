"""Generate primes with a sieve and factorize integers."""

import math
from collections import Counter


def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, math.isqrt(limit) + 1):
        if is_prime[p]:
            is_prime[p * p::p] = [False] * len(range(p * p, limit + 1, p))
    return [i for i, flag in enumerate(is_prime) if flag]


def factorize(n):
    factors = Counter()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] += 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        factors[n] += 1
    return factors


def format_factors(f):
    return " * ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(f.items()))


primes = sieve(100)
print("primes <= 100:", primes)
print("count below 10000:", len(sieve(10000)))

for n in (360, 1001, 97, 2 ** 10 * 3 ** 4, 600851475143):
    print(f"{n} = {format_factors(factorize(n))}")


def num_divisors(n):
    return math.prod(e + 1 for e in factorize(n).values())


def phi(n):
    result = n
    for p in factorize(n):
        result -= result // p
    return result


print("divisor counts:", {n: num_divisors(n) for n in (12, 28, 36, 100)})
print("totients:", {n: phi(n) for n in (9, 10, 36, 97)})
twins = [(p, p + 2) for p in primes if p + 2 in primes]
print("twin primes:", twins)
perfect = [n for n in range(2, 1000) if sum(d for d in range(1, n // 2 + 1) if n % d == 0) == n]
print("perfect numbers below 1000:", perfect)
