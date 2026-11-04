"""Do exact rational arithmetic with fractions.Fraction."""

from fractions import Fraction
import math

a = Fraction(1, 3)
b = Fraction(1, 6)
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} ** 2 = {a ** 2}")

print("auto-reduced:", Fraction(42, 56), "| from string:", Fraction("3/4"), Fraction("1.25"))
print("from float 0.1:", Fraction(0.1))
print("limit_denominator:", Fraction(0.1).limit_denominator(), Fraction(math.pi).limit_denominator(1000))
print("numerator/denominator:", Fraction(10, 4).numerator, Fraction(10, 4).denominator)

# harmonic numbers exactly
h = sum(Fraction(1, k) for k in range(1, 11))
print("H(10) =", h, "~", float(h))

# exact vs float accumulation
f_total = sum([0.1] * 10)
q_total = sum([Fraction(1, 10)] * 10)
print("float sum:", f_total, "| fraction sum:", q_total, q_total == 1)

# continued fraction approximations of sqrt(2)
approx = Fraction(1)
for _ in range(8):
    approx = 1 + 1 / (1 + approx)
    print(f"  {str(approx):>10} = {float(approx):.10f}")

print("comparisons:", Fraction(2, 3) > Fraction(3, 5), Fraction(1, 2) == 0.5)
print("mixed with int:", Fraction(3, 4) + 1, "| floor:", math.floor(Fraction(7, 2)), "| round:", round(Fraction(5, 2)))
print("format:", f"{Fraction(22, 7):.5f}")

# egyptian fraction decomposition
def egyptian(fr):
    parts = []
    while fr.numerator:
        unit = Fraction(1, math.ceil(fr.denominator / fr.numerator))
        parts.append(unit)
        fr -= unit
    return parts

print("4/13 =", " + ".join(map(str, egyptian(Fraction(4, 13)))))
