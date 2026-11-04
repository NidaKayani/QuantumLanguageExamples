"""Radix conversion to any base, balanced ternary, factoradic, and multi-base palindromes."""
from math import factorial
from string import digits, ascii_uppercase

ALPHABET = digits + ascii_uppercase


def to_base(n, base):
    if n == 0:
        return "0"
    sign = "-" if n < 0 else ""
    n = abs(n)
    out = []
    while n:
        n, r = divmod(n, base)
        out.append(ALPHABET[r])
    return sign + "".join(reversed(out))


def balanced_ternary(n):
    out = []
    while n:
        r = n % 3
        if r == 2:
            out.append("-")
            n = n // 3 + 1
        else:
            out.append(str(r) if r == 0 else "+")
            n //= 3
    return "".join(reversed(out)) or "0"


def factoradic(n):
    radix, out = 2, [0]
    while n:
        n, r = divmod(n, radix)
        out.append(r)
        radix += 1
    return out[::-1]


def nth_permutation(items, k):
    items, out = list(items), []
    for i in range(len(items) - 1, -1, -1):
        idx, k = divmod(k, factorial(i))
        out.append(items.pop(idx))
    return "".join(out)


def main():
    n = 2024
    for base in (2, 3, 8, 12, 16, 36):
        s = to_base(n, base)
        assert int(s, base) == n
        print(f"{n} in base {base:>2}: {s}")
    print("Negative:", to_base(-255, 16), "| Python builtins:", bin(n), oct(n), hex(n))
    for k in (5, 8, -7, 100):
        print(f"Balanced ternary of {k}: {balanced_ternary(k)}")
    print("Factoradic of 463:", factoradic(463))
    print("Permutation #999999 of 0..9:", nth_permutation("0123456789", 999_999))
    decimal_palindromes = set(range(1, 10))
    for half in range(1, 1000):
        s = str(half)
        decimal_palindromes.add(int(s + s[::-1]))
        decimal_palindromes.update(int(s + d + s[::-1]) for d in "0123456789")
    double = sorted(k for k in decimal_palindromes
                    if k < 1_000_000 and (b := to_base(k, 2)) == b[::-1])
    print("Palindromic in base 10 and 2 below 10^6:", double)
    print("Sum:", sum(double))


if __name__ == "__main__":
    main()
