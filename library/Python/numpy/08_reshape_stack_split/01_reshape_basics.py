"""Reshaping a flat sequence into grids, including -1 inference and memory order."""
import numpy as np

a = np.arange(12)
print(a)
print(repr(a))

m = a.reshape(3, 4)
print("reshape(3, 4):")
print(m)
print(repr(m))

print("reshape(4, -1):")
print(a.reshape(4, -1))
print("reshape(-1, 6) shape:", a.reshape(-1, 6).shape)
print("reshape((2, 2, 3)):")
print(np.reshape(a, (2, 2, 3)))

col = a.reshape(-1, 1)
print("column vector shape:", col.shape)
print(col[:4])
row = a.reshape(1, -1)
print("row vector:", row, row.shape)

print("Fortran-order reshape(3, 4):")
print(a.reshape(3, 4, order="F"))

# reshape returns a view when possible
v = a.reshape(2, 6)
v[0, 0] = 100
print("after writing through view, a[0] =", a[0])
print("shares memory:", np.shares_memory(a, v))
a[0] = 0

# reshape on a float array keeps the dtype
b = np.arange(6.0)
b = b.reshape(2, 3)
print(repr(b))

# reshape for per-block sums: 12 hourly values -> 4 blocks of 3 hours
hourly = np.array([3, 5, 2, 8, 7, 6, 1, 0, 4, 9, 9, 2])
blocks = hourly.reshape(4, 3)
print("blocks:")
print(blocks)
print("block totals:", blocks.sum(axis=1))

img = np.arange(24).reshape(2, 3, 4)
print("3-D shape:", img.shape, "ndim:", img.ndim, "size:", img.size)
print(img)
print("collapse last two dims:", img.reshape(2, -1).shape)
print(img.reshape(2, -1))
print("size preserved:", img.reshape(-1).size == img.size)
