"""Classic map, filter and reduce over a small sales dataset."""
from functools import reduce

sales = [
    ("north", "widget", 12, 2.50),
    ("south", "gadget", 3, 10.00),
    ("north", "gadget", 7, 10.00),
    ("east", "widget", 20, 2.25),
    ("south", "widget", 5, 2.50),
    ("east", "doohickey", 1, 99.99),
    ("north", "doohickey", 2, 95.00),
]

revenues = list(map(lambda row: row[2] * row[3], sales))
print("Revenue per line:", [round(r, 2) for r in revenues])

big = list(filter(lambda row: row[2] * row[3] > 50, sales))
print("Lines over $50:", [(region, item) for region, item, *_ in big])

total = reduce(lambda acc, r: acc + r, revenues, 0.0)
print(f"Total revenue: {total:.2f}")

by_region = reduce(
    lambda acc, row: {**acc, row[0]: acc.get(row[0], 0) + row[2] * row[3]},
    sales,
    {},
)
for region, amount in sorted(by_region.items(), key=lambda kv: -kv[1]):
    print(f"  {region:<6} {amount:8.2f}")

largest = reduce(lambda a, b: a if a[2] >= b[2] else b, sales)
print("Largest quantity line:", largest)

words = "the quick brown fox jumps over the lazy dog".split()
print("Lengths:", list(map(len, words)))
print("Upper long words:", list(map(str.upper, filter(lambda w: len(w) > 4, words))))
print("Pairwise sums:", list(map(lambda a, b: a + b, [1, 2, 3], [10, 20, 30])))
print("Product 1..10:", reduce(int.__mul__, range(1, 11)))
print("Flattened:", reduce(lambda a, b: a + b, [[1, 2], [3], [4, 5, 6]], []))
print("Truthy only:", list(filter(None, [0, 1, "", "a", None, [], [0], False, 3.5])))
