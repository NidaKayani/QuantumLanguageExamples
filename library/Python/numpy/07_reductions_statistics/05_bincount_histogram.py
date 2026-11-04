"""Counting with np.bincount and binning with np.histogram on dice-like data."""
import numpy as np


def lcg(seed, n, mod):
    out = []
    state = seed
    for _ in range(n):
        state = (1103515245 * state + 12345) % (2 ** 31)
        out.append((state >> 16) % mod)
    return np.array(out)


rolls = lcg(7, 60, 6) + 1
print("first 20 rolls:", rolls[:20])
counts = np.bincount(rolls)
print("bincount:", counts)
print(repr(counts))
print("faces 1..6:", counts[1:])
print("most common face:", int(np.argmax(counts)))
print("minlength=10:", np.bincount(rolls, minlength=10))

# weighted bincount: total amount per category
category = np.array([0, 2, 1, 2, 0, 3, 1, 2])
amount = np.array([5.0, 2.5, 4.0, 1.5, 3.0, 10.0, 6.0, 2.0])
totals = np.bincount(category, weights=amount)
print("totals per category:", totals)
per_cat_mean = totals / np.bincount(category)
print("mean per category:", per_cat_mean)

# histogram with an integer number of bins
heights = np.array([152.0, 160.5, 171.2, 158.3, 180.1, 165.4, 175.0, 169.9, 162.2, 155.5, 178.8, 167.0])
hist, edges = np.histogram(heights, bins=4)
print("hist (4 bins):", hist)
print("edges:", edges)
print(repr(edges))

# histogram with explicit bin edges
bins = np.array([150, 160, 170, 180, 190])
hist2, edges2 = np.histogram(heights, bins=bins)
print("explicit bins:", hist2, "edges:", edges2)
for lo, hi, c in zip(edges2[:-1], edges2[1:], hist2):
    print(f"  [{lo}, {hi}) {'#' * int(c)} {c}")
print("total counted:", hist2.sum(), "of", heights.size)

hist3, _ = np.histogram(rolls, bins=np.arange(0.5, 7.5, 1.0))
print("rolls via histogram:", hist3)
print("matches bincount:", np.array_equal(hist3, counts[1:]))
hist4, e4 = np.histogram(heights, bins=3, range=(150, 180))
print("bins=3 range=(150,180):", hist4, e4)
