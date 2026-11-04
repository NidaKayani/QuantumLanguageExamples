"""Build an inverted index from documents and run simple queries."""

import re
from collections import defaultdict

documents = {
    1: "Python is a popular programming language.",
    2: "The Python standard library is large and useful.",
    3: "Programming in a functional style uses pure functions.",
    4: "A large library of functions makes programming easier.",
}

STOP = {"a", "is", "the", "and", "in", "of"}

index = defaultdict(set)
for doc_id, text in documents.items():
    for word in re.findall(r"[a-z]+", text.lower()):
        if word not in STOP:
            index[word].add(doc_id)

for word in sorted(index):
    print(f"  {word:<12} {sorted(index[word])}")


def search_all(*terms):
    sets = [index.get(t, set()) for t in terms]
    return sorted(set.intersection(*sets)) if sets else []


def search_any(*terms):
    return sorted(set().union(*(index.get(t, set()) for t in terms)))


print("AND python library:", search_all("python", "library"))
print("AND programming functions:", search_all("programming", "functions"))
print("OR python functional:", search_any("python", "functional"))
print("missing term:", search_all("rust"))

doc_freq = {w: len(ids) for w, ids in index.items()}
common = sorted(doc_freq.items(), key=lambda kv: (-kv[1], kv[0]))[:3]
print("most widespread words:", common)
