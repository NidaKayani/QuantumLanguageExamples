"""Building search indexes with dictionaries: inverted index and prefix lookup."""

import re
from collections import defaultdict

DOCS = {
    1: "Python lists support fast appends and indexing",
    2: "Binary search needs a sorted list",
    3: "Hash tables give average constant time lookup",
    4: "A sorted list allows binary search and bisect",
    5: "Python dicts are hash tables",
}

index: defaultdict[str, set[int]] = defaultdict(set)
for doc_id, text in DOCS.items():
    for word in re.findall(r"\w+", text.lower()):
        index[word].add(doc_id)


def search_all(*terms):
    sets = [index.get(t.lower(), set()) for t in terms]
    return sorted(set.intersection(*sets)) if sets else []


def search_any(*terms):
    return sorted(set().union(*(index.get(t.lower(), set()) for t in terms)))


prefixes = defaultdict(set)
for word in index:
    for i in range(1, len(word) + 1):
        prefixes[word[:i]].add(word)


def complete(prefix):
    return sorted(prefixes.get(prefix.lower(), ()))


print("index size:", len(index), "terms")
for terms in [("binary", "search"), ("python",), ("hash", "python"), ("sorted", "list", "bisect"), ("missing",)]:
    print(f"ALL {terms}: {search_all(*terms)}")
print("ANY ('dicts', 'lists'):", search_any("dicts", "lists"))
for p in ["s", "so", "ha", "b", "xy"]:
    print(f"complete({p!r}): {complete(p)}")

rank = sorted(((len(index[w]), w) for w in index), key=lambda t: (-t[0], t[1]))[:5]
print("most common terms:", rank)
