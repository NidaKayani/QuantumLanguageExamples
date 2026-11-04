"""Big Fibonacci numbers: F(200) exactly, Pisano periods, and Fibonacci identities."""
from itertools import count, islice
from math import gcd


def fib_pair(n):
    """Return (F(n), F(n+1)) using fast doubling."""
    if n == 0:
        return 0, 1
    a, b = fib_pair(n // 2)
    c = a * (2 * b - a)
    d = a * a + b * b
    return (d, c + d) if n % 2 else (c, d)


def fib_iter():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def pisano(m):
    a, b = 0, 1
    for i in count(1):
        a, b = b, (a + b) % m
        if (a, b) == (0, 1):
            return i


def main():
    f200 = fib_pair(200)[0]
    print("F(200) =", f200)
    print("  digits:", len(str(f200)), " digit sum:", sum(map(int, str(f200))))
    assert f200 == next(islice(fib_iter(), 200, None))
    first_1000 = next(i for i, f in enumerate(fib_iter()) if len(str(f)) >= 1000)
    print("First Fibonacci with 1000 digits: index", first_1000)
    print("Pisano periods:", {m: pisano(m) for m in (2, 3, 5, 7, 10, 100, 1000)})
    print("F(10^15) mod 1000 via Pisano:", fib_pair(10**15 % pisano(1000))[0] % 1000)
    n = 50
    fn_1, fn = fib_pair(n - 1)
    fn1 = fn_1 + fn
    print(f"Cassini at n={n}: F(n-1)F(n+1) - F(n)^2 = {fn_1 * fn1 - fn * fn}")
    print("gcd(F(60), F(84)) = F(gcd(60, 84)) ->",
          gcd(fib_pair(60)[0], fib_pair(84)[0]) == fib_pair(12)[0])
    ratios = [fib_pair(k + 1)[0] / fib_pair(k)[0] for k in (5, 10, 20, 40)]
    print("Ratios approaching phi:", [f"{r:.12f}" for r in ratios])
    zeckendorf, target = [], 1_000_000
    fibs = list(islice(fib_iter(), 2, 40))
    for f in reversed(fibs):
        if f <= target:
            zeckendorf.append(f)
            target -= f
    print("Zeckendorf representation of 10^6:", " + ".join(map(str, zeckendorf)))


if __name__ == "__main__":
    main()
