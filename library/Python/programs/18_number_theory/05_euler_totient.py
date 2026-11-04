"""Euler's totient via factorisation and via a sieve, with Euler's theorem checks."""
from math import gcd


def totient(n):
    result, p, m = n, 2, n
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            result -= result // p
        p += 1
    if m > 1:
        result -= result // m
    return result


def totient_sieve(limit):
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:
            for k in range(p, limit + 1, p):
                phi[k] -= phi[k] // p
    return phi


def main():
    phi = totient_sieve(1000)
    print("phi(1..20):", phi[1:21])
    assert all(phi[n] == totient(n) for n in range(1, 1001))
    assert all(phi[n] == sum(1 for k in range(1, n + 1) if gcd(k, n) == 1) for n in range(1, 60))
    print("Sieve, factor formula and brute force agree.")
    divisor_sum = {n: sum(phi[d] for d in range(1, n + 1) if n % d == 0) for n in (12, 30, 97, 360)}
    print("Sum of phi(d) over d|n equals n:", divisor_sum)
    for a, n in [(3, 10), (7, 20), (2, 99), (5, 1000)]:
        print(f"{a}^phi({n}) = {a}^{phi[n]} = {pow(a, phi[n], n)} (mod {n})")
    print("phi(999999999999) =", totient(999_999_999_999))
    best = max(range(2, 1001), key=lambda n: (n / phi[n], -n))
    print(f"Maximum n/phi(n) for n <= 1000: n={best}, ratio={best / phi[best]:.4f}")
    print("Farey sequence F_100 length:", 1 + sum(phi[1:101]))


if __name__ == "__main__":
    main()
