"""A ModInt class with operator overloading, used for modular combinatorics and polynomial evaluation."""
from functools import total_ordering


@total_ordering
class ModInt:
    __slots__ = ("value", "mod")

    def __init__(self, value, mod):
        self.mod = mod
        self.value = value % mod

    def _coerce(self, other):
        if isinstance(other, ModInt):
            if other.mod != self.mod:
                raise ValueError("modulus mismatch")
            return other.value
        return other % self.mod

    def __add__(self, other):
        return ModInt(self.value + self._coerce(other), self.mod)

    __radd__ = __add__

    def __sub__(self, other):
        return ModInt(self.value - self._coerce(other), self.mod)

    def __rsub__(self, other):
        return ModInt(self._coerce(other) - self.value, self.mod)

    def __mul__(self, other):
        return ModInt(self.value * self._coerce(other), self.mod)

    __rmul__ = __mul__

    def __pow__(self, exp):
        return ModInt(pow(self.value, exp, self.mod), self.mod)

    def __truediv__(self, other):
        return self * pow(self._coerce(other), -1, self.mod)

    def __neg__(self):
        return ModInt(-self.value, self.mod)

    def __eq__(self, other):
        return self.value == self._coerce(other)

    def __lt__(self, other):
        return self.value < self._coerce(other)

    def __hash__(self):
        return hash((self.value, self.mod))

    def __int__(self):
        return self.value

    def __repr__(self):
        return f"ModInt({self.value}, {self.mod})"

    def __str__(self):
        return f"{self.value} (mod {self.mod})"


def binomial(n, k, mod):
    num, den = ModInt(1, mod), ModInt(1, mod)
    for i in range(k):
        num *= n - i
        den *= i + 1
    return num / den


def main():
    P = 1_000_000_007
    a, b = ModInt(10**12, P), ModInt(987654321, P)
    print("a =", a, "| b =", b)
    print("a + b =", a + b, "| a - b =", a - b, "| a * b =", a * b)
    print("a / b =", a / b, "| check (a / b) * b == a:", (a / b) * b == a)
    print("2 ** 100 =", ModInt(2, P) ** 100, "| -a =", -a, "| 5 - a =", 5 - a)
    print("repr:", repr(ModInt(17, 5)), "| int():", int(ModInt(-1, 13)))
    print("C(1000, 500) mod p =", binomial(1000, 500, P))
    print("C(10, 3) mod 7 =", binomial(10, 3, 7))
    coeffs = [3, 0, -2, 7, 1]
    x = ModInt(123456, P)
    acc = ModInt(0, P)
    for c in coeffs:
        acc = acc * x + c
    print("Horner p(123456) mod p =", acc)
    residues = sorted({ModInt(k * k, 11) for k in range(11)})
    print("Quadratic residues mod 11:", [int(r) for r in residues])
    try:
        ModInt(1, 7) + ModInt(1, 11)
    except ValueError as exc:
        print("Mixing moduli raises:", exc)


if __name__ == "__main__":
    main()
