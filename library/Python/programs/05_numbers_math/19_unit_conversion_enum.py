"""Convert between measurement units using Enum members carrying factors."""

from enum import Enum
from decimal import Decimal


class Length(Enum):
    MM = 0.001
    CM = 0.01
    M = 1.0
    KM = 1000.0
    INCH = 0.0254
    FOOT = 0.3048
    MILE = 1609.344

    def to(self, other, value):
        return value * self.value / other.value


class Weight(Enum):
    GRAM = Decimal("1")
    KILOGRAM = Decimal("1000")
    POUND = Decimal("453.59237")
    OUNCE = Decimal("28.349523125")


print("1 mile in km:", Length.MILE.to(Length.KM, 1))
print("6 feet in cm:", round(Length.FOOT.to(Length.CM, 6), 2))
print("marathon in miles:", round(Length.KM.to(Length.MILE, 42.195), 3))
print("100 m in inches:", round(Length.M.to(Length.INCH, 100), 2))

print("\nconversion table for 1 unit:")
units = list(Length)
print(f"{'':>6}" + "".join(f"{u.name:>11}" for u in units[2:]))
for src in units[2:]:
    print(f"{src.name:>6}" + "".join(f"{src.to(dst, 1):>11.4g}" for dst in units[2:]))

print("\nexact weights:")
for qty, unit in ((1, Weight.POUND), (16, Weight.OUNCE), (2, Weight.KILOGRAM)):
    grams = qty * unit.value
    pounds = (grams / Weight.POUND.value).quantize(Decimal("0.0001"))
    print(f"  {qty} {unit.name.lower()} = {grams.normalize()} g = {pounds} lb")

print("lookup by name:", Length["FOOT"], "| by value:", Length(1000.0))
print("member count:", len(Length), "| names:", [u.name for u in Length if u.value < 1])
