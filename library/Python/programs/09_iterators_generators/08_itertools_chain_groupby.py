"""Combining and grouping iterables with chain, chain.from_iterable, and groupby."""
from itertools import chain, groupby
from operator import itemgetter

a, b, c = [1, 2], (3, 4), range(5, 8)
print("chain:", list(chain(a, b, c)))
nested = [["x", "y"], [], ["z"], ["w", "v"]]
print("from_iterable:", list(chain.from_iterable(nested)))

text = "aaabccddddde"
runs = [(ch, len(list(group))) for ch, group in groupby(text)]
print("run lengths:", runs)
print("encoded:", "".join(f"{n}{ch}" for ch, n in runs))

sales = [
    {"region": "north", "rep": "Ann", "amount": 120},
    {"region": "south", "rep": "Bob", "amount": 80},
    {"region": "north", "rep": "Cid", "amount": 200},
    {"region": "east", "rep": "Dee", "amount": 50},
    {"region": "south", "rep": "Eve", "amount": 140},
]
sales.sort(key=itemgetter("region"))
for region, rows in groupby(sales, key=itemgetter("region")):
    rows = list(rows)
    total = sum(r["amount"] for r in rows)
    print(f"{region:<6} total={total:>4} reps={[r['rep'] for r in rows]}")

words = ["apple", "avocado", "banana", "blueberry", "cherry", "apricot"]
by_letter = {k: list(g) for k, g in groupby(sorted(words), key=lambda w: w[0])}
print("by first letter:", by_letter)

numbers = [1, 3, 5, 2, 4, 7, 9, 6]
parity_runs = [(k, list(g)) for k, g in groupby(numbers, key=lambda n: n % 2 == 0)]
print("parity runs:", parity_runs)
