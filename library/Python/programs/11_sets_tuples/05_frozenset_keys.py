"""Frozensets as hashable, immutable sets for dict keys and nested sets."""

edges = [("a", "b", 4), ("b", "c", 2), ("c", "a", 7), ("b", "a", 5), ("d", "c", 1)]

weights = {}
for u, v, w in edges:
    key = frozenset((u, v))
    # keep the cheaper edge for an unordered pair
    weights[key] = min(w, weights.get(key, w))

for key in sorted(weights, key=lambda k: sorted(k)):
    print("-".join(sorted(key)), "=>", weights[key])

print("lookup b-a:", weights[frozenset({"b", "a"})])

groups = {frozenset({1, 2}), frozenset({2, 1}), frozenset({3}), frozenset()}
print("distinct groups:", len(groups))

fs = frozenset("mississippi")
print("letters:", sorted(fs))
print("union returns frozenset:", type(fs | {"z"}).__name__)
print("set | frozenset returns:", type({"z"} | fs).__name__)

try:
    fs.add("q")
except AttributeError as exc:
    print("cannot mutate:", exc)

power = {frozenset()}
for item in ["x", "y", "z"]:
    power |= {s | {item} for s in power}
for s in sorted(power, key=lambda s: (len(s), sorted(s))):
    print("  {" + ", ".join(sorted(s)) + "}")
