"""Group and accumulate data with collections.defaultdict."""

from collections import defaultdict

transactions = [
    ("alice", "food", 12.5), ("bob", "travel", 300.0), ("alice", "travel", 120.0),
    ("carol", "food", 8.25), ("bob", "food", 22.0), ("alice", "food", 7.75),
    ("carol", "books", 45.0),
]

spend_by_person = defaultdict(float)
for person, _, amount in transactions:
    spend_by_person[person] += amount
print("spend by person:", dict(spend_by_person))

categories = defaultdict(set)
for person, cat, _ in transactions:
    categories[person].add(cat)
for person in sorted(categories):
    print(f"  {person}: {sorted(categories[person])}")

nested = defaultdict(lambda: defaultdict(float))
for person, cat, amount in transactions:
    nested[person][cat] += amount
for person, cats in nested.items():
    print(f"  {person}: {dict(cats)}")

# adjacency list for a graph
edges = [("a", "b"), ("a", "c"), ("b", "d"), ("c", "d"), ("d", "e")]
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
print("graph:", dict(graph))

# counting with int
counts = defaultdict(int)
for word in "to be or not to be that is the question".split():
    counts[len(word)] += 1
print("word lengths:", dict(sorted(counts.items())))

# accessing a missing key creates it
d = defaultdict(list)
_ = d["ghost"]
print("ghost key created:", "ghost" in d, d.default_factory.__name__)
print("get() does not create:", d.get("other"), "other" in d)
