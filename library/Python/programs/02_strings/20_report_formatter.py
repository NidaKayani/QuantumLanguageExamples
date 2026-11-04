"""Generate a formatted sales report combining many string techniques."""

sales = [
    ("north", "widgets", 1520.5),
    ("south", "gadgets", 980.0),
    ("north", "gadgets", 410.25),
    ("east", "widgets", 2200.0),
    ("south", "widgets", 75.75),
    ("east", "doohickeys", 640.0),
]

title = "Quarterly Sales Report"
width = 44
print("=" * width)
print(title.upper().center(width))
print("=" * width)

regions = sorted({r for r, _, _ in sales})
grand_total = 0.0
for region in regions:
    rows = [(p, amt) for r, p, amt in sales if r == region]
    subtotal = sum(a for _, a in rows)
    grand_total += subtotal
    print(f"{region.title()} region".ljust(width, "."))
    for product, amount in sorted(rows, key=lambda t: -t[1]):
        print(f"  {product:<20}{amount:>18,.2f}")
    print(f"  {'subtotal':<20}{subtotal:>18,.2f}")

print("-" * width)
print(f"{'GRAND TOTAL':<22}{grand_total:>18,.2f}")
print("=" * width)

best = max(sales, key=lambda t: t[2])
print(f"Best line: {best[1]} in the {best[0]} ({best[2]:,.0f})")
share = {r: sum(a for rr, _, a in sales if rr == r) / grand_total for r in regions}
print("Share: " + "; ".join(f"{r}={pct:.1%}" for r, pct in share.items()))
bars = "\n".join(f"{r:>6} |{'#' * round(pct * 30)}" for r, pct in share.items())
print(bars)
