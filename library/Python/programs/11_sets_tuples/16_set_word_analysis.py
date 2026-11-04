"""Vocabulary comparison between short texts using set operations."""

import re
from itertools import combinations

TEXTS = {
    "alpha": "The cat sat on the mat while the dog slept by the door.",
    "beta": "A dog and a cat played on the mat near the open door.",
    "gamma": "Quantum computers use qubits to explore many states at once.",
    "delta": "The dog chased the cat out the door and across the yard.",
}
STOPWORDS = frozenset("the a an and on by to at of while near out".split())

def vocabulary(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]+", text.lower()) if w not in STOPWORDS}

vocab = {name: vocabulary(text) for name, text in TEXTS.items()}
for name, words in vocab.items():
    print(f"{name:<6} ({len(words):2d}): {' '.join(sorted(words))}")

def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a | b else 1.0

print()
scores = []
for x, y in combinations(vocab, 2):
    score = jaccard(vocab[x], vocab[y])
    scores.append((score, x, y))
    print(f"jaccard({x}, {y}) = {score:.3f}")

best = max(scores)
print(f"\nmost similar pair: {best[1]} & {best[2]}")

common = set.intersection(*(v for k, v in vocab.items() if k != "gamma"))
print("shared by all animal texts:", sorted(common))

unique_words = {
    name: words - set().union(*(v for k, v in vocab.items() if k != name))
    for name, words in vocab.items()
}
for name, words in unique_words.items():
    print(f"unique to {name}: {sorted(words)}")
