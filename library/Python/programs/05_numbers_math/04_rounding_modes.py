"""Compare round(), banker's rounding, floor, ceil and Decimal rounding modes."""

import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_DOWN, ROUND_CEILING, ROUND_FLOOR

values = [0.5, 1.5, 2.5, 3.5, -0.5, -1.5, 2.675]
print(f"{'x':>7}{'round':>7}{'floor':>7}{'ceil':>7}{'trunc':>7}")
for x in values:
    print(f"{x:>7}{round(x):>7}{math.floor(x):>7}{math.ceil(x):>7}{math.trunc(x):>7}")

print("round(2.675, 2) =", round(2.675, 2), "(binary representation is slightly below)")
print("round(1234.5678, -2) =", round(1234.5678, -2), "| round(1250, -2) =", round(1250, -2))
print("round(3.14159, 3) =", round(3.14159, 3))

modes = {"HALF_UP": ROUND_HALF_UP, "HALF_EVEN": ROUND_HALF_EVEN, "DOWN": ROUND_DOWN,
         "CEILING": ROUND_CEILING, "FLOOR": ROUND_FLOOR}
amounts = ["2.675", "2.665", "-2.675", "1.005"]
print(f"\n{'mode':<10}" + "".join(f"{a:>8}" for a in amounts))
for name, mode in modes.items():
    row = "".join(f"{str(Decimal(a).quantize(Decimal('0.01'), rounding=mode)):>8}" for a in amounts)
    print(f"{name:<10}{row}")


def round_half_up(x, digits=0):
    factor = 10 ** digits
    return math.floor(x * factor + 0.5) / factor


print("\ncustom half-up:", [round_half_up(v) for v in (0.5, 1.5, 2.5)])

# rounding to nearest multiple
for price in (17, 23, 98):
    print(f"{price} -> nearest 5: {5 * round(price / 5)}, up to 10: {10 * math.ceil(price / 10)}")
