"""Format numbers for display: separators, padding, percentages, scientific and units."""

values = [0, 7, -42, 1234.5678, 1_000_000, 0.000123, 98.6]

for v in values:
    print(f"{v!s:>12} | {v:>14,.2f} | {v:>12.3e} | {v:>10.4g}")

print(f"percent: {0.4567:.1%} {1.25:.0%} {-0.031:+.2%}")
print(f"padded ints: [{42:05d}] [{42:<6d}] [{42:^6d}] [{-42:06d}]")
print(f"sign handling: [{7:+d}] [{-7:+d}] [{7: d}] [{-7: d}]")
print(f"underscores: {123456789:_d} | hex groups: {0xDEADBEEF:_x}")
print(f"locale-free thousands: {9876543.21:,.2f}")


def human_bytes(n):
    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(n)
    for unit in units:
        if size < 1024 or unit == units[-1]:
            return f"{size:.1f} {unit}" if unit != "B" else f"{int(size)} B"
        size /= 1024


for n in (512, 2048, 5_000_000, 3 * 1024 ** 3, 7 * 1024 ** 5):
    print(f"{n:>20,} bytes = {human_bytes(n)}")


def si(n):
    for factor, suffix in ((1e9, "G"), (1e6, "M"), (1e3, "k")):
        if abs(n) >= factor:
            return f"{n / factor:.3g}{suffix}"
    return str(n)


print("SI:", [si(n) for n in (950, 12_500, 3_400_000, 7_200_000_000)])


def ordinal(n):
    suffix = "th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"


print("ordinals:", ", ".join(ordinal(n) for n in (1, 2, 3, 4, 11, 12, 13, 21, 22, 101, 111)))
print("currency:", f"${1234567.891:,.2f}", f"({abs(-50.5):,.2f})")
print("table:")
for name, qty, price in (("apples", 3, 0.5), ("melon", 1, 3.25), ("grapes", 12, 0.125)):
    print(f"  {name:<8}{qty:>4}{price:>8.3f}{qty * price:>9.2f}")
