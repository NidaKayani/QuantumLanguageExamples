"""Fancy indexing with integer lists and arrays in 1-D and 2-D."""
import numpy as np

letters_codes = np.arange(100, 110)
print(repr(letters_codes))

print("pick [0, 3, 3, 9]:", letters_codes[[0, 3, 3, 9]])
print("negative indices:", letters_codes[[-1, -2, 0]])
idx = np.array([[1, 2], [7, 8]])
print("2-D index array gives 2-D result:")
print(letters_codes[idx])

# Fancy indexing returns a copy, not a view
sel = letters_codes[[1, 2, 3]]
sel[:] = 0
print("original unchanged:", letters_codes)

# Permutation and its inverse
perm = np.array([3, 0, 4, 1, 2])
items = np.array([10.5, 20.5, 30.5, 40.5, 50.5])
shuffled = items[perm]
inv = np.argsort(perm)
print("shuffled:", shuffled)
print("restored:", shuffled[inv])

# 2-D fancy: paired row/col indices pick individual elements
m = np.arange(30).reshape(5, 6)
print("m:")
print(m)
print("m[[0, 2, 4], [1, 3, 5]]:", m[[0, 2, 4], [1, 3, 5]])

# Fancy rows with a slice of columns
print("rows 4, 0 and cols 1:4:")
print(m[[4, 0], 1:4])

# Fancy columns with all rows
print("columns 5, 0:")
print(m[:, [5, 0]])

# Broadcasting index arrays
r = np.array([[0], [2], [4]])
c = np.array([1, 3])
print("broadcast rows x cols:")
print(m[r, c])

# One-hot encoding via fancy indexing
labels = np.array([2, 0, 1, 2, 3])
one_hot = np.eye(4, dtype=np.int64)[labels]
print("one-hot:")
print(one_hot)
print(repr(one_hot))

# Lookup table (palette) mapping
palette = np.array([[0.0, 0.0, 0.0],
                    [1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                    [0.0, 0.0, 1.0]])
image = np.array([[0, 1, 1], [2, 3, 0]])
rgb = palette[image]
print("rgb shape:", rgb.shape)
print(rgb[1])

# Bincount-style histogram via fancy indexing + np.add.at
hist = np.zeros(4, dtype=np.int64)
np.add.at(hist, labels, 1)
print("label histogram:", hist)
