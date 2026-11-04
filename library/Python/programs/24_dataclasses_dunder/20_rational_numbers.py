"""A Rational number class with full arithmetic, reflected operators, conversions and hashing."""
import math
from functools import total_ordering


@total_ordering
class Rational:
    __slots__ = ("num", "den")

    def __init__(self, num, den=1):
        if den == 0:
            raise ZeroDivisionError("denominator is zero")
        if den < 0:
            num, den = -num, -den
        g = math.gcd(num, den)
        self.num, self.den = num // g, den // g

    @staticmethod
    def _coerce(other):
        if isinstance(other, Rational):
            return other
        if isinstance(other, int):
            return Rational(other)
        return NotImplemented

    def __add__(self, other):
        o = self._coerce(other)
        if o is NotImplemented:
            return o
        return Rational(self.num * o.den + o.num * self.den, self.den * o.den)

    __radd__ = __add__

    def __sub__(self, other):
        return self + -self._coerce(other)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        o = self._coerce(other)
        return Rational(self.num * o.num, self.den * o.den)

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = self._coerce(other)
        return Rational(self.num * o.den, self.den * o.num)

    def __rtruediv__(self, other):
        return self._coerce(other) / self

    def __pow__(self, k):
        return Rational(self.num ** k, self.den ** k) if k >= 0 else Rational(self.den ** -k, self.num ** -k)

    def __neg__(self):
        return Rational(-self.num, self.den)

    def __abs__(self):
        return Rational(abs(self.num), self.den)

    def __eq__(self, other):
        o = self._coerce(other)
        return o is not NotImplemented and (self.num, self.den) == (o.num, o.den)

    def __lt__(self, other):
        o = self._coerce(other)
        return self.num * o.den < o.num * self.den

    def __hash__(self):
        return hash(self.num) if self.den == 1 else hash((self.num, self.den))

    def __float__(self):
        return self.num / self.den

    def __int__(self):
        return int(self.num / self.den)

    def __round__(self, ndigits=None):
        return round(float(self), ndigits) if ndigits is not None else round(float(self))

    def __bool__(self):
        return self.num != 0

    def __repr__(self):
        return f"{self.num}/{self.den}" if self.den != 1 else str(self.num)


half, third = Rational(1, 2), Rational(1, 3)
print("1/2 + 1/3 =", half + third, "| 1/2 - 1/3 =", half - third)
print("1/2 * 1/3 =", half * third, "| (1/2) / (1/3) =", half / third)
print("2 + 1/3 =", 2 + third, "| 1 - 1/2 =", 1 - half, "| 3 / (1/2) =", 3 / half)
print("powers:", half ** 3, third ** -2, "| normalized:", Rational(6, -8))
print("compare:", half > third, third <= third, sorted([half, Rational(-2, 5), third, Rational(3)]))
print("conversions:", float(Rational(22, 7)), int(Rational(-7, 2)), round(Rational(22, 7), 3))
print("equality with int:", Rational(4, 2) == 2, "| hash match:", hash(Rational(4, 2)) == hash(2))
print("set of equal values:", len({Rational(1, 2), Rational(2, 4), Rational(3, 6)}))
harmonic = sum((Rational(1, k) for k in range(1, 11)), Rational(0))
print("H(10) =", harmonic, f"~ {float(harmonic):.6f}")
print("bool:", bool(Rational(0, 5)), bool(third), "| abs:", abs(Rational(-3, 4)))
egyptian, rest = [], Rational(5, 7)
while rest:
    unit = Rational(1, -(-rest.den // rest.num))
    egyptian.append(unit)
    rest = rest - unit
print("5/7 as Egyptian fractions:", " + ".join(map(repr, egyptian)))
