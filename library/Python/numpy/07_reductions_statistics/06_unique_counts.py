"""np.unique with return_counts, return_index and return_inverse for label encoding."""
import numpy as np

# product ids seen in a transaction log
ids = np.array([104, 101, 104, 107, 101, 101, 110, 107, 104, 101, 112])
print("ids:", ids)

uniq = np.unique(ids)
print("unique:", uniq)
print(repr(uniq))

values, counts = np.unique(ids, return_counts=True)
print("values:", values)
print("counts:", counts)
for v, c in zip(values, counts):
    print(f"  product {v}: {c} sale(s)")
print("best seller:", values[np.argmax(counts)])

values, first_idx = np.unique(ids, return_index=True)
print("first occurrence index:", first_idx)
order = np.argsort(first_idx)
print("unique in order of appearance:", values[order])

values, inverse = np.unique(ids, return_inverse=True)
print("inverse (label codes):", inverse)
print("reconstructed equals original:", np.array_equal(values[inverse], ids))

prices = np.array([2.5, 4.0, 2.5, 7.25, 4.0, 4.0, 1.0, 7.25, 2.5, 4.0, 9.5])
revenue = np.bincount(inverse, weights=prices)
print("revenue per product:", revenue)

v, i, inv, c = np.unique(ids, return_index=True, return_inverse=True, return_counts=True)
print("all at once:", v, i, inv, c, sep="\n  ")

# unique on a 2-D array (flattened) and unique rows
grid = np.array([[1, 2, 2], [3, 1, 2], [1, 2, 2]])
print(grid)
print("unique of grid:", np.unique(grid))
rows, row_counts = np.unique(grid, axis=0, return_counts=True)
print("unique rows:")
print(rows)
print("row counts:", row_counts)

flags = np.array([True, False, True, True])
print("unique bools:", np.unique(flags, return_counts=True))
floats = np.array([0.5, 0.25, 0.5, 1.0])
print(repr(np.unique(floats)))
