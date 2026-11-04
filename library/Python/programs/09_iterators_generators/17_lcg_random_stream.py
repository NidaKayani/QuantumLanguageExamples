"""A deterministic pseudo-random number generator implemented as an infinite generator."""
from itertools import islice
from collections import Counter


def lcg(seed=42, a=1103515245, c=12345, m=2 ** 31):
    state = seed
    while True:
        state = (a * state + c) % m
        yield state


def uniform(seed=42):
    for value in lcg(seed):
        yield value / 2 ** 31


def dice(seed=42, sides=6):
    for u in uniform(seed):
        yield int(u * sides) + 1


def shuffle(items, seed=7):
    items = list(items)
    rng = uniform(seed)
    for i in range(len(items) - 1, 0, -1):
        j = int(next(rng) * (i + 1))
        items[i], items[j] = items[j], items[i]
    return items


print("raw:", list(islice(lcg(), 4)))
print("uniform:", [round(u, 4) for u in islice(uniform(), 5)])
rolls = list(islice(dice(), 600))
counts = Counter(rolls)
print("600 rolls:", dict(sorted(counts.items())))
print("mean roll:", round(sum(rolls) / len(rolls), 3))
print("same seed reproducible:", list(islice(dice(1), 8)) == list(islice(dice(1), 8)))
print("shuffled deck:", shuffle("ABCDEFGHIJ"))
inside = sum(1 for x, y in islice(zip(uniform(1), uniform(2)), 5000) if x * x + y * y <= 1)
print("pi estimate:", 4 * inside / 5000)
