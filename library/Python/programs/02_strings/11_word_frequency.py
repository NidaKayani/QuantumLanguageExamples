"""Count word frequencies in a paragraph using string methods and Counter."""

import string
from collections import Counter

text = """
It was the best of times, it was the worst of times, it was the age of
wisdom, it was the age of foolishness, it was the epoch of belief, it was
the epoch of incredulity, it was the season of Light, it was the season of
Darkness, it was the spring of hope, it was the winter of despair.
"""

strip_punct = str.maketrans("", "", string.punctuation)
words = text.lower().translate(strip_punct).split()

print("total words:", len(words))
print("unique words:", len(set(words)))

counts = Counter(words)
print("top 6:")
for word, n in counts.most_common(6):
    print(f"  {word:<8} {n:>3} {'#' * n}")

longest = max(words, key=len)
print("longest word:", longest)

by_length = {}
for w in sorted(set(words)):
    by_length.setdefault(len(w), []).append(w)
for length in sorted(by_length):
    print(f"{length:2d} letters: {', '.join(by_length[length])}")

sentences = [s.strip() for s in text.replace("\n", " ").split(",") if s.strip()]
print("clauses:", len(sentences))
print("first clause:", sentences[0])
print("capitalized words:", sorted({w.strip(string.punctuation) for w in text.split() if w[0].isupper()}))
