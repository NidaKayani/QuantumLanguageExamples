"""Continued fractions: expansions of rationals and square roots, convergents, and Pell equations."""
from fractions import Fraction
from math import isqrt


def expand_rational(frac):
    terms = []
    num, den = frac.numerator, frac.denominator
    while den:
        q, r = divmod(num, den)
        terms.append(q)
        num, den = den, r
    return terms


def sqrt_expansion(n):
    a0 = isqrt(n)
    if a0 * a0 == n:
        return a0, []
    m, d, a = 0, 1, a0
    period = []
    while a != 2 * a0:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period.append(a)
    return a0, period


def convergents(terms):
    h_prev, h = 1, terms[0]
    k_prev, k = 0, 1
    yield Fraction(h, k)
    for a in terms[1:]:
        h_prev, h = h, a * h + h_prev
        k_prev, k = k, a * k + k_prev
        yield Fraction(h, k)


def pell(n):
    a0, period = sqrt_expansion(n)
    terms = [a0] + period * 2
    for c in convergents(terms):
        x, y = c.numerator, c.denominator
        if x * x - n * y * y == 1:
            return x, y


def main():
    for frac in (Fraction(415, 93), Fraction(649, 200), Fraction(355, 113)):
        print(f"{frac} = {expand_rational(frac)}")
    pi_approx = Fraction(3141592653589793, 10**15)
    terms = expand_rational(pi_approx)[:6]
    print("pi terms:", terms)
    print("pi convergents:", [str(c) for c in convergents(terms)])
    for n in (2, 3, 7, 13, 19, 23):
        a0, period = sqrt_expansion(n)
        print(f"sqrt({n}) = [{a0}; ({', '.join(map(str, period))})]")
    sqrt2 = [str(c) for c, _ in zip(convergents([1] + [2] * 10), range(8))]
    print("sqrt(2) convergents:", ", ".join(sqrt2))
    for n in (2, 7, 13, 61, 109):
        x, y = pell(n)
        print(f"Pell x^2 - {n}y^2 = 1: x={x}, y={y}")


if __name__ == "__main__":
    main()
