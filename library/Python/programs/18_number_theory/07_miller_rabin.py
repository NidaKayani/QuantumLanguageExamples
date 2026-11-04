"""Deterministic Miller-Rabin primality test for 64-bit integers, with strong-pseudoprime demos."""

BASES_64 = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def decompose(n):
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    return d, s


def strong_probable_prime(n, a):
    d, s = decompose(n)
    x = pow(a, d, n)
    if x in (1, n - 1):
        return True
    for _ in range(s - 1):
        x = x * x % n
        if x == n - 1:
            return True
    return False


def is_prime(n, bases=BASES_64):
    if n < 2:
        return False
    for p in bases:
        if n % p == 0:
            return n == p
    return all(strong_probable_prime(n, a) for a in bases)


def trial_is_prime(n):
    return n > 1 and all(n % k for k in range(2, int(n ** 0.5) + 1))


def main():
    assert all(is_prime(n) == trial_is_prime(n) for n in range(10_000))
    print("Agrees with trial division for n < 10000")
    carmichael = [561, 1105, 1729, 2465, 2821, 6601, 8911]
    for n in carmichael:
        fermat = pow(2, n - 1, n) == 1
        print(f"  {n}: Fermat base 2 says {'prime' if fermat else 'composite'}, "
              f"Miller-Rabin says {'prime' if is_prime(n) else 'composite'}")
    spsp = [n for n in range(3, 10_000, 2) if strong_probable_prime(n, 2) and not trial_is_prime(n)]
    print("Strong pseudoprimes to base 2 below 10000:", spsp)
    big = [2**61 - 1, 2**62 - 1, 1_000_000_007, 999_999_999_989, 18446744073709551557,
           3825123056546413051, 341550071728321]
    for n in big:
        print(f"  {n:>22}: {'prime' if is_prime(n) else 'composite'}")
    next_prime = next(n for n in range(10**15, 10**15 + 1000) if is_prime(n))
    print("First prime after 10^15:", next_prime)


if __name__ == "__main__":
    main()
