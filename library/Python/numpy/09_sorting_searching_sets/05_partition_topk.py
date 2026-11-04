"""Top-k and k-th order statistics with np.partition and np.argpartition."""
import numpy as np


def lcg(seed, n, mod=1000):
    out = []
    state = seed
    for _ in range(n):
        state = (1103515245 * state + 12345) % (2 ** 31)
        out.append(state % mod)
    return np.array(out)


values = lcg(42, 20)
print("values:", values)
print(repr(values))

# k-th smallest element: partition guarantees position k holds it
k = 4
part = np.partition(values, k)
print(f"{k}-th smallest (0-based):", part[k], "check:", np.sort(values)[k])
print("all left of k are <= it:", bool(np.all(part[:k] <= part[k])))
print("all right of k are >= it:", bool(np.all(part[k + 1:] >= part[k])))
print("smallest five (sorted):", np.sort(part[:k + 1]))

# Top-k largest via negative kth index
top = 5
part_hi = np.partition(values, -top)
largest = np.sort(part_hi[-top:])[::-1]
print(f"top {top} largest:", largest)
print("matches full sort:", bool(np.array_equal(largest, np.sort(values)[::-1][:top])))

# argpartition gives indices of the top-k; sort them by value for display
idx = np.argpartition(values, -top)[-top:]
idx = idx[np.argsort(values[idx])[::-1]]
print("top-k indices by value:", idx)
print("top-k values:", values[idx])

# Median through partition
n = values.size
mid = np.partition(values, [n // 2 - 1, n // 2])
median = (mid[n // 2 - 1] + mid[n // 2]) / 2
print("median via partition:", median, "np.median:", np.median(values))

# Row-wise top-2 in a 2-D score table
table = lcg(7, 24, 100).reshape(4, 6)
print("score table:")
print(table)
row_top2 = np.sort(np.partition(table, -2, axis=1)[:, -2:], axis=1)[:, ::-1]
print("top-2 per row:")
print(row_top2)
print("row maxima:", table.max(axis=1))

# Smallest-3 per column
col_small = np.sort(np.partition(table, 2, axis=0)[:3], axis=0)
print("3 smallest per column:")
print(col_small)
