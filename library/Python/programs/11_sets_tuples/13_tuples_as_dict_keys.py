"""Tuples as composite dict keys: sparse matrices and multi-part lookups."""

from collections import defaultdict

sparse = {}
entries = [(0, 0, 5), (2, 3, -1), (1, 1, 7), (3, 0, 2), (2, 3, 4)]
for r, c, v in entries:
    sparse[(r, c)] = sparse.get((r, c), 0) + v

rows = 1 + max(r for r, _ in sparse)
cols = 1 + max(c for _, c in sparse)
for r in range(rows):
    print(" ".join(f"{sparse.get((r, c), 0):3d}" for c in range(cols)))

print("non-zero cells:", sorted(sparse.items()))

flights = {
    ("NYC", "LON"): 7.0,
    ("LON", "NYC"): 8.0,
    ("NYC", "PAR"): 7.5,
    ("PAR", "ROM"): 2.1,
}
for (src, dst), hours in sorted(flights.items()):
    print(f"{src} -> {dst}: {hours:.1f}h")

route = ["NYC", "PAR", "ROM"]
legs = list(zip(route, route[1:]))
print("route legs:", legs, "total:", sum(flights[leg] for leg in legs), "hours")

sales = defaultdict(int)
transactions = [("2024", "Q1", 100), ("2024", "Q2", 150), ("2023", "Q4", 80), ("2024", "Q1", 20)]
for year, quarter, amount in transactions:
    sales[year, quarter] += amount
for key in sorted(sales):
    print(key, sales[key])

try:
    bad = {[1, 2]: "list key"}
except TypeError as exc:
    print("lists are unhashable:", exc)
