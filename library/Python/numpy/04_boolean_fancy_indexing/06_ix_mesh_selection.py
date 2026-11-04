"""Cross-product selection of rows and columns with np.ix_."""
import numpy as np

# Distance table between 6 cities (symmetric)
coords = np.array([[0.0, 0.0], [3.0, 4.0], [6.0, 0.0],
                   [1.0, 7.0], [8.0, 6.0], [5.0, 2.0]])
diff = coords[:, None, :] - coords[None, :, :]
dist = np.sqrt((diff ** 2).sum(axis=-1)).round(2)
print("distance table:")
print(dist)

# Sub-table for cities 0, 2, 5
pick = [0, 2, 5]
ix = np.ix_(pick, pick)
print("np.ix_ output:", ix)
print("sub-table for", pick)
print(dist[ix])

# Compare with plain fancy indexing (gives only the diagonal pairs)
print("dist[pick, pick] (paired):", dist[pick, pick])

# Different rows and columns
origins = np.array([1, 3])
dests = np.array([0, 2, 4, 5])
sub = dist[np.ix_(origins, dests)]
print("origins x destinations:")
print(repr(sub))
nearest = dests[np.argmin(sub, axis=1)]
print("nearest destination for each origin:", nearest)

# np.ix_ with boolean masks
m = np.arange(1, 26).reshape(5, 5)
row_mask = np.array([True, False, True, False, True])
col_mask = m[0] % 2 == 0
print("m:")
print(m)
print("rows 0,2,4 x even-valued first-row columns:")
print(m[np.ix_(row_mask, col_mask)])

# Assignment through np.ix_
m2 = np.zeros((5, 5), dtype=np.int64)
m2[np.ix_([1, 3], [0, 2, 4])] = 7
print("assigned via ix_:")
print(m2)

# Three-dimensional ix_
cube = np.arange(64).reshape(4, 4, 4)
block = cube[np.ix_([0, 3], [1, 2], [0, 3])]
print("3-D ix_ block shape:", block.shape)
print(block)

# Using ix_ to build an outer-operation grid
a, b = np.ix_(np.arange(1, 5), np.arange(1, 6))
print("multiplication table via ix_ broadcasting:")
print(a * b)
