"""Fast exponentiation: square-and-multiply, three-argument pow, and matrix powers."""
from operator import mul


def power(base, exp, mod=None):
    result = 1
    squarings = 0
    while exp:
        if exp & 1:
            result = result * base if mod is None else result * base % mod
        base = base * base if mod is None else base * base % mod
        exp >>= 1
        squarings += 1
    return result, squarings


def mat_mult(a, b, mod):
    return [[sum(map(mul, row, col)) % mod for col in zip(*b)] for row in a]


def mat_pow(m, exp, mod):
    size = len(m)
    result = [[int(i == j) for j in range(size)] for i in range(size)]
    while exp:
        if exp & 1:
            result = mat_mult(result, m, mod)
        m = mat_mult(m, m, mod)
        exp >>= 1
    return result


def main():
    for base, exp, mod in [(2, 10, None), (3, 200, 1_000_000_007), (7, 2**64, 13), (12345, 6789, 99991)]:
        value, steps = power(base, exp, mod)
        expected = pow(base, exp, mod) if mod else base ** exp
        assert value == expected
        label = f"mod {mod}" if mod else "exact"
        print(f"{base}^{exp} ({label}) = {value}  [{steps} squarings]")
    big, _ = power(2, 521)
    print("2^521 - 1 has", len(str(big - 1)), "digits; last 12:", str(big - 1)[-12:])
    fib = mat_pow([[1, 1], [1, 0]], 10**18, 1_000_000_007)
    print("Fib(10^18) mod 1e9+7 =", fib[0][1])
    tribonacci = mat_pow([[1, 1, 1], [1, 0, 0], [0, 1, 0]], 50, 10**12)
    print("Tribonacci-style term 50 mod 10^12 =", tribonacci[0][0])
    print("Last 10 digits of sum n^n for n=1..1000:",
          sum(pow(n, n, 10**10) for n in range(1, 1001)) % 10**10)


if __name__ == "__main__":
    main()
