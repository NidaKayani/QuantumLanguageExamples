"""Streaming word-frequency analysis with generators, Counter, and heapq.nlargest."""
import re
import heapq
from collections import Counter
from itertools import islice

TEXT = """
It was the best of times, it was the worst of times, it was the age of wisdom,
it was the age of foolishness, it was the epoch of belief, it was the epoch of
incredulity, it was the season of Light, it was the season of Darkness, it was
the spring of hope, it was the winter of despair.
"""

STOP = {"it", "was", "the", "of"}


def lines(text):
    yield from (line for line in text.splitlines() if line.strip())


def words(line_iter):
    for line in line_iter:
        yield from (w.lower() for w in re.findall(r"[A-Za-z']+", line))


def without_stopwords(word_iter):
    return (w for w in word_iter if w not in STOP)


all_words = list(words(lines(TEXT)))
print("total words:", len(all_words), "| distinct:", len(set(all_words)))

counts = Counter(without_stopwords(words(lines(TEXT))))
print("most common:", counts.most_common(4))
print("nlargest by length:", heapq.nlargest(3, counts, key=len))
print("first five content words:", list(islice(without_stopwords(all_words), 5)))

pair_counts = Counter(zip(all_words, all_words[1:]))
print("top bigrams:", [" ".join(p) for p, _ in pair_counts.most_common(3)])
print("words seen once:", sorted(w for w, c in counts.items() if c == 1)[:6])
