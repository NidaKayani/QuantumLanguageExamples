"""Handle money calculations precisely with decimal.Decimal and quantize."""

from decimal import Decimal, ROUND_HALF_UP, getcontext, localcontext

CENT = Decimal("0.01")

items = [("notebook", Decimal("3.99"), 3), ("pen", Decimal("1.25"), 10), ("bag", Decimal("24.50"), 1)]
tax_rate = Decimal("0.0825")

subtotal = sum((price * qty for _, price, qty in items), Decimal("0"))
tax = (subtotal * tax_rate).quantize(CENT, rounding=ROUND_HALF_UP)
total = subtotal + tax

for name, price, qty in items:
    print(f"{name:<10}{qty:>3} x {price:>6} = {price * qty:>7}")
print(f"{'subtotal':<23}{subtotal:>7}")
print(f"{'tax 8.25%':<23}{tax:>7}")
print(f"{'total':<23}{total:>7}")

print("float vs decimal:", 0.1 + 0.2, "vs", Decimal("0.1") + Decimal("0.2"))
print("Decimal from float:", Decimal(0.1))

# splitting a bill so the cents add up
def split(amount, ways):
    base = (amount / ways).quantize(CENT, rounding="ROUND_DOWN")
    remainder = amount - base * ways
    extra = int(remainder / CENT)
    return [base + CENT if i < extra else base for i in range(ways)]

shares = split(Decimal("100.00"), 3)
print("split 100 three ways:", [str(s) for s in shares], "sum:", sum(shares))

# compound interest
balance = Decimal("1000.00")
for year in range(1, 6):
    balance = (balance * Decimal("1.035")).quantize(CENT, rounding=ROUND_HALF_UP)
    print(f"  year {year}: {balance}")

print("precision:", getcontext().prec)
with localcontext() as ctx:
    ctx.prec = 50
    print("1/7 at 50 digits:", Decimal(1) / Decimal(7))
print("1/7 default:", Decimal(1) / Decimal(7))
print("sqrt(2):", Decimal(2).sqrt(), "| exponent of 1.500:", Decimal("1.500").as_tuple().exponent)
print("normalize:", Decimal("1.500").normalize(), "| compare:", Decimal("1.5") == Decimal("1.500"))
