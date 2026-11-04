"""Rounding ufuncs: floor, ceil, trunc, rint and round (banker's rounding)."""
import numpy as np

v = np.array([-2.5, -1.7, -1.5, -0.5, -0.2, 0.0, 0.2, 0.5, 1.5, 1.7, 2.5, 3.5])
print("values:", v)
print("floor: ", np.floor(v))
print("ceil:  ", np.ceil(v))
print("trunc: ", np.trunc(v))
print("rint:  ", np.rint(v))
print("round: ", np.round(v))
print(repr(np.floor(v)))

# half-to-even rounding vs half-away-from-zero
away = np.sign(v) * np.floor(np.abs(v) + 0.5)
print("half away from zero:", away)
print("differs from np.round at:", v[np.round(v) != away])

# rounding to decimals
prices = np.array([3.14159, 2.71828, 1.41421, 12.34567, 0.005])
print("round 2: ", np.round(prices, 2))
print("round 0: ", np.round(prices, 0))
print("around 3:", np.around(prices, 3))
print("round -1 on ints:", np.round(np.array([14, 15, 25, 149, 151]), -1))

# results stay float; cast for integer indices
idx = np.floor(np.array([0.2, 1.9, 3.5]))
print("floor dtype:", idx.dtype, " as int:", idx.astype(np.int64))

# binning a measurement into buckets of width 0.25
readings = np.array([0.1, 0.26, 0.49, 0.5, 0.74, 0.99, 1.13])
buckets = np.floor(readings / 0.25).astype(np.int64)
print("bucket ids:", buckets)
print("bucket lower edges:", buckets * 0.25)

# ceil for pagination
items = np.array([0, 1, 9, 10, 11, 99, 100])
pages = np.ceil(items / 10).astype(np.int64)
print("items:", items, " pages:", pages)

# fractional and integer parts
frac, whole = np.modf(np.array([3.75, -2.25, 10.5]))
print("modf whole:", whole, " frac:", frac)

# rounding a 2-D grid
grid = np.linspace(-1, 1, 12).reshape(3, 4) * 3.3
print("grid:")
print(grid)
print("rint(grid):")
print(np.rint(grid))
print("trunc(grid):")
print(np.trunc(grid))
