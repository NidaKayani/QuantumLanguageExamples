"""GCD and LCM: Euclid (recursive, iterative, binary) compared against math.gcd and math.lcm."""
import math
from functools import reduce


def gcd_recursive(a, b):
    return a if b == 0 else gcd_recursive(b, a % b)


def gcd_iterative(a, b):
    steps = 0
    while b:
        a, b = b, a % b
        steps += 1
    return abs(a), steps


def gcd_binary(a, b):
    if a == 0 or b == 0:
        return a | b
    shift = ((a | b) & -(a | b)).bit_length() - 1
    a >>= (a & -a).bit_length() - 1
    while b:
        b >>= (b & -b).bit_length() - 1
        if a > b:
            a, b = b, a
        b -= a
    return a << shift


def lcm(a, b):
    return a // gcd_recursive(a, b) * b


def main():
    pairs = [(48, 18), (1071, 462), (270, 192), (17, 31), (0, 9), (2**40, 6**20)]
    print(f"{'a':>14} {'b':>16} {'gcd':>10} {'steps':>5} {'lcm':>20}")
    for a, b in pairs:
        g, steps = gcd_iterative(a, b)
        assert g == gcd_recursive(a, b) == gcd_binary(a, b) == math.gcd(a, b)
        l = lcm(a, b) if a and b else 0
        assert l == math.lcm(a, b)
        print(f"{a:>14} {b:>16} {g:>10} {steps:>5} {l:>20}")
    fib = [1, 1]
    while len(fib) < 30:
        fib.append(fib[-1] + fib[-2])
    _, worst = gcd_iterative(fib[-1], fib[-2])
    print(f"Consecutive Fibonacci {fib[-1]}, {fib[-2]} need {worst} steps (worst case)")
    print("gcd of many:", reduce(math.gcd, [840, 3528, 1176, 2352]), math.gcd(840, 3528, 1176))
    print("lcm of 1..20:", reduce(lcm, range(1, 21)), "==", math.lcm(*range(1, 21)))
    coprime = sum(1 for a in range(1, 101) for b in range(1, 101) if math.gcd(a, b) == 1)
    print(f"Coprime pairs in 1..100: {coprime} / 10000 = {coprime / 10000:.4f} "
          f"(6/pi^2 = {6 / math.pi ** 2:.4f})")


if __name__ == "__main__":
    main()
