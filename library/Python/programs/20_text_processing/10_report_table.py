"""Render sales data as aligned text tables with computed column widths, totals, and subtotals."""
from itertools import groupby
from operator import itemgetter

SALES = [
    ("North", "Widgets", 1240, 3.75),
    ("North", "Gadgets", 310, 12.40),
    ("North", "Gizmos", 95, 48.00),
    ("South", "Widgets", 860, 3.75),
    ("South", "Gizmos", 140, 46.50),
    ("East", "Widgets", 2010, 3.60),
    ("East", "Gadgets", 455, 12.10),
    ("East", "Doohickeys", 38, 99.99),
]


def render(headers, rows, aligns):
    cells = [[str(h) for h in headers]] + [[str(c) for c in r] for r in rows]
    widths = [max(len(row[i]) for row in cells) for i in range(len(headers))]
    sep = "+" + "+".join("-" * (w + 2) for w in widths) + "+"

    def fmt(row):
        parts = []
        for text, width, align in zip(row, widths, aligns):
            parts.append(f" {text:{align}{width}} ")
        return "|" + "|".join(parts) + "|"

    lines = [sep, fmt(cells[0]), sep.replace("-", "=")]
    lines += [fmt(r) for r in cells[1:-1]]
    lines += [sep, fmt(cells[-1]), sep]
    return "\n".join(lines)


def main():
    rows = []
    for region, product, units, price in SALES:
        rows.append([region, product, f"{units:,}", f"{price:,.2f}", f"{units * price:,.2f}"])
    total_units = sum(s[2] for s in SALES)
    total_rev = sum(s[2] * s[3] for s in SALES)
    rows.append(["TOTAL", "", f"{total_units:,}", "", f"{total_rev:,.2f}"])
    print(render(["Region", "Product", "Units", "Price", "Revenue"], rows,
                 ["<", "<", ">", ">", ">"]))
    print()
    print("Subtotals by region:")
    for region, group in groupby(sorted(SALES, key=itemgetter(0)), key=itemgetter(0)):
        items = list(group)
        revenue = sum(u * p for _, _, u, p in items)
        share = revenue / total_rev
        bar = "#" * round(share * 40)
        print(f"  {region:<6} {len(items)} lines {revenue:>11,.2f}  {share:6.1%} {bar}")
    best = max(SALES, key=lambda s: s[2] * s[3])
    print(f"Best line: {best[1]} in {best[0]} ({best[2] * best[3]:,.2f})")
    print(f"{'Sci':>8}: {total_rev:.3e}   {'Hex units':>9}: {total_units:#x}   "
          f"{'Padded':>6}: {total_units:08d}")


if __name__ == "__main__":
    main()
