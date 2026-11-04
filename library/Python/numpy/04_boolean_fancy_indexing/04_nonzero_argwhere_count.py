"""Locating True/non-zero entries with np.nonzero, np.argwhere, np.flatnonzero and np.count_nonzero."""
import numpy as np

sparse = np.array([0, 3, 0, 0, 7, 0, 1, 0, 0, 4])
print(repr(sparse))
print("nonzero:", np.nonzero(sparse))
print("flatnonzero:", np.flatnonzero(sparse))
print("count_nonzero:", np.count_nonzero(sparse))
print("values:", sparse[np.nonzero(sparse)])

# 2-D sparse matrix in coordinate form
mat = np.zeros((5, 6), dtype=np.int64)
mat[0, 2] = 5
mat[1, 0] = 3
mat[2, 4] = 8
mat[3, 3] = 1
mat[4, 1] = 9
mat[4, 5] = 2
print("matrix:")
print(mat)

rows, cols = np.nonzero(mat)
print("rows:", rows)
print("cols:", cols)
print("vals:", mat[rows, cols])

coords = np.argwhere(mat)
print("argwhere (one row per hit):")
print(coords)
print(repr(coords))
print("argwhere shape:", coords.shape)

# Counting along axes
print("non-zeros per row:", np.count_nonzero(mat, axis=1))
print("non-zeros per col:", np.count_nonzero(mat, axis=0))
print("density:", np.count_nonzero(mat) / mat.size)

# Method form on boolean arrays
big = mat > 4
print("big.nonzero():", big.nonzero())
print("argwhere(big):")
print(np.argwhere(big))

# Rebuild the dense matrix from coordinates
rebuilt = np.zeros_like(mat)
rebuilt[rows, cols] = mat[rows, cols]
print("rebuilt equals original:", np.array_equal(rebuilt, mat))

# Find run boundaries in a binary signal
signal = np.array([0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1])
edges = np.diff(signal)
starts = np.flatnonzero(edges == 1) + 1
ends = np.flatnonzero(edges == -1) + 1
if signal[-1] == 1:
    ends = np.append(ends, signal.size)
print("signal:", signal)
print("run starts:", starts)
print("run ends:", ends)
print("run lengths:", ends - starts)

# 3-D argwhere
cube = np.arange(27).reshape(3, 3, 3) % 7 == 0
print("multiples of 7 in a 3x3x3 range:")
print(np.argwhere(cube))
