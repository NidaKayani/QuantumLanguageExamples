"""Sliding windows, pairwise, and batching over iterators using deque and itertools."""
from collections import deque
from itertools import islice, pairwise, batched


def sliding_window(iterable, n):
    it = iter(iterable)
    window = deque(islice(it, n - 1), maxlen=n)
    for x in it:
        window.append(x)
        yield tuple(window)


def moving_average(values, n):
    for window in sliding_window(values, n):
        yield sum(window) / n


prices = [10, 12, 11, 15, 18, 17, 21, 25]
print("windows of 3:", list(sliding_window(prices, 3)))
print("3-day moving average:", [round(a, 2) for a in moving_average(prices, 3)])

changes = [b - a for a, b in pairwise(prices)]
print("day-over-day changes:", changes)
print("biggest jump:", max(changes), "on day", changes.index(max(changes)) + 1)

print("batched(7 items, 3):", list(batched(range(1, 8), 3)))
text = "the quick brown fox jumps over the lazy dog"
print("word trigrams:", [" ".join(w) for w in sliding_window(text.split(), 3)][:4])
print("letter bigrams in 'banana':", ["".join(p) for p in pairwise("banana")])
increasing = all(a < b for a, b in pairwise([1, 3, 7, 9]))
print("strictly increasing [1,3,7,9]:", increasing)
