"""Repeating decimal periods of 1/n by long division, and high-precision constants with decimal."""
from decimal import Decimal, getcontext, localcontext
from fractions import Fraction


def decimal_expansion(num, den):
    whole, rem = divmod(num, den)
    seen, digits = {}, []
    while rem and rem not in seen:
        seen[rem] = len(digits)
        rem *= 10
        digits.append(str(rem // den))
        rem %= den
    if not rem:
        return f"{whole}." + ("".join(digits) or "0"), 0
    start = seen[rem]
    body = "".join(digits[:start]) + "(" + "".join(digits[start:]) + ")"
    return f"{whole}.{body}", len(digits) - start


def sqrt_newton(n, places):
    with localcontext() as ctx:
        ctx.prec = places + 5
        x = Decimal(n)
        guess = Decimal(1)
        for _ in range(200):
            nxt = (guess + x / guess) / 2
            if nxt == guess:
                break
            guess = nxt
        return +guess


def euler_e(places):
    getcontext().prec = places + 5
    total, term, k = Decimal(1), Decimal(1), 1
    while term > Decimal(10) ** -(places + 3):
        term /= k
        total += term
        k += 1
    return total


def main():
    for n in (3, 6, 7, 11, 12, 13, 17, 28, 81):
        text, period = decimal_expansion(1, n)
        print(f"1/{n:<3} = {text:<30} period {period}")
    longest = max(range(2, 1000), key=lambda d: decimal_expansion(1, d)[1])
    print("Longest period for d < 1000:", longest, decimal_expansion(1, longest)[1])
    print("22/7 =", decimal_expansion(22, 7)[0])
    print("sqrt(2) to 50 places:", str(sqrt_newton(2, 50))[:52])
    print("e to 50 places:      ", str(euler_e(50))[:52])
    getcontext().prec = 28
    print("0.1 + 0.2 as float:  ", 0.1 + 0.2)
    print("0.1 + 0.2 as Decimal:", Decimal("0.1") + Decimal("0.2"))
    print("Fraction from 0.75 Decimal:", Fraction(Decimal("0.75")))
    print("Rounded:", Decimal("2.675").quantize(Decimal("0.01")), round(2.675, 2))


if __name__ == "__main__":
    main()
