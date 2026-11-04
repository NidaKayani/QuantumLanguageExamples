"""Deduplicating and counting values with np.unique and its return_* options."""
import numpy as np

rolls = np.array([3, 6, 1, 3, 3, 2, 6, 5, 1, 4, 6, 6, 2, 3, 5, 1])
print("dice rolls:", rolls)

faces = np.unique(rolls)
print("distinct faces:", faces)
print(repr(faces))

faces, counts = np.unique(rolls, return_counts=True)
print("counts:", counts)
for f, c in zip(faces, counts):
    print(f"  face {f}: {'#' * int(c)} ({c})")
print("mode:", faces[np.argmax(counts)])

# First occurrence indices and reconstruction via inverse
vals, first_idx, inverse = np.unique(rolls, return_index=True, return_inverse=True)
print("first index of each face:", first_idx)
print("inverse:", inverse)
print("reconstructed equals original:", bool(np.array_equal(vals[inverse], rolls)))

# Order-preserving unique (first appearance order)
order_kept = rolls[np.sort(first_idx)]
print("unique in order of appearance:", order_kept)

# Unique rows of a 2-D array
pairs = np.array([[1, 2],
                  [3, 4],
                  [1, 2],
                  [0, 9],
                  [3, 4],
                  [1, 3]])
upairs, pcounts = np.unique(pairs, axis=0, return_counts=True)
print("unique rows:")
print(upairs)
print("row counts:", pcounts)

# Floats and booleans
readings = np.array([0.5, 1.25, 0.5, -2.0, 1.25, 3.75])
print("unique readings:", np.unique(readings))
flags = np.array([True, True, False, True])
print("unique flags:", np.unique(flags))

# Group-by sum using inverse indices with np.bincount
stores = np.array([12, 7, 12, 30, 7, 12, 30])
sales = np.array([100.0, 50.5, 20.0, 75.25, 9.5, 30.0, 4.75])
ids, inv = np.unique(stores, return_inverse=True)
totals = np.bincount(inv, weights=sales)
print("store ids:", ids)
print("total sales:", totals)
print("duplicates present:", rolls.size != faces.size)
