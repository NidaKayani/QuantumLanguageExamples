"""Basic whole-array and per-axis reductions on a small sales table."""
import numpy as np

# rows = stores, columns = months
sales = np.array([
    [12, 15, 9, 20],
    [7, 11, 14, 6],
    [18, 3, 10, 13],
])
print("sales:")
print(sales)
print(repr(sales))

print("total sales:", sales.sum())
print("per store (axis=1):", sales.sum(axis=1))
print("per month (axis=0):", sales.sum(axis=0))
print("product of first row:", np.prod(sales[0]))
print("product per column:", sales.prod(axis=0))

print("min:", sales.min(), "max:", sales.max())
print("min per month:", np.min(sales, axis=0))
print("max per store:", np.max(sales, axis=1))

print("argmin (flat):", sales.argmin(), "argmax (flat):", sales.argmax())
best = np.unravel_index(sales.argmax(), sales.shape)
print("best store/month:", tuple(int(i) for i in best))
print("best month per store:", sales.argmax(axis=1))
print("worst store per month:", np.argmin(sales, axis=0))

kept = sales.sum(axis=1, keepdims=True)
print("keepdims sum shape:", kept.shape)
print(kept)
share = sales / kept
print("monthly share per store:")
print(np.round(share, 3))
print("shares sum to one:", np.allclose(share.sum(axis=1), 1.0))

print("any month above 18?", np.any(sales > 18))
print("all stores sold > 2 every month?", np.all(sales > 2, axis=1))
print("count above 10 per store:", np.count_nonzero(sales > 10, axis=1))

floats = sales.astype(float) / 4
print(repr(floats.sum(axis=0)))
print(repr(floats.max(axis=1)))
