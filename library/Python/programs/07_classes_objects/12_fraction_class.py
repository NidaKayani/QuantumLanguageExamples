"""A rational-number class implementing arithmetic, comparison, and normalization."""
import math
from functools import total_ordering


@total_ordering
class Rational:
    def __init__(self, num, den=1):
        if den == 0:
            raise ZeroDivisionError("denominator cannot be zero")
        g = math.gcd(num, den)
        sign = -1 if den < 0 else 1
        self.num = sign * num // g
        self.den = sign * den // g

    @staticmethod
    def _coerce(other):
        return other if isinstance(other, Rational) else Rational(other)

    def __add__(self, other):
        o = self._coerce(other)
        return Rational(self.num * o.den + o.num * self.den, self.den * o.den)

    __radd__ = __add__

    def __sub__(self, other):
        o = self._coerce(other)
        return Rational(self.num * o.den - o.num * self.den, self.den * o.den)

    def __mul__(self, other):
        o = self._coerce(other)
        return Rational(self.num * o.num, self.den * o.den)

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = self._coerce(other)
        return Rational(self.num * o.den, self.den * o.num)

    def __eq__(self, other):
        o = self._coerce(other)
        return (self.num, self.den) == (o.num, o.den)

    def __lt__(self, other):
        o = self._coerce(other)
        return self.num * o.den < o.num * self.den

    def __hash__(self):
        return hash((self.num, self.den))

    def __float__(self):
        return self.num / self.den

    def __repr__(self):
        return f"{self.num}/{self.den}" if self.den != 1 else f"{self.num}"


half, third = Rational(1, 2), Rational(1, 3)
print("1/2 + 1/3 =", half + third)
print("1/2 - 1/3 =", half - third)
print("1/2 * 1/3 =", half * third)
print("1/2 / 1/3 =", half / third)
print("normalized 6/-8 =", Rational(6, -8))
print("2 + 1/2 =", 2 + half, "| 3 * 1/3 =", 3 * third)
print("float(2/7) =", round(float(Rational(2, 7)), 6))
harmonic = sum((Rational(1, n) for n in range(1, 7)), Rational(0))
print("H(6) =", harmonic)
print("sorted:", sorted([Rational(3, 4), Rational(-1, 2), Rational(2, 3), Rational(5, 8)]))
print("1/2 == 2/4:", half == Rational(2, 4), "| set size:", len({half, Rational(2, 4), third}))
try:
    Rational(1, 0)
except ZeroDivisionError as exc:
    print("error:", exc)
