"""Boolean masks: building them from comparisons and using them to filter arrays."""
import numpy as np

readings = np.array([21.5, 19.0, 25.25, 30.0, 17.75, 22.0, 28.5, 15.0, 24.0, 26.5])
print(repr(readings))

hot = readings > 25.0
print("hot mask:", hot)
print(repr(hot))
print("hot readings:", readings[hot])
print("number hot:", hot.sum(), "fraction:", hot.mean())

# Inline masks
print("below 20:", readings[readings < 20])
print("exactly 22.0:", readings[readings == 22.0])
print("not 22.0 count:", readings[readings != 22.0].size)

# Mask from one array used on another
days = np.arange(1, 11)
print("days that were hot:", days[hot])

# Masks on 2-D arrays give a flattened 1-D result
grid = np.arange(1, 21).reshape(4, 5)
print("grid:")
print(grid)
mult3 = grid % 3 == 0
print("multiple-of-3 mask:")
print(mult3)
print("selected:", grid[mult3])

# Row selection with a 1-D mask
row_has_big = grid.max(axis=1) > 12
print("rows with max > 12:", row_has_big)
print(grid[row_has_big])

# Column selection with a 1-D mask
even_cols = np.array([True, False, True, False, True])
print("even columns:")
print(grid[:, even_cols])

# Deviation from mean
mean = readings.mean()
std = readings.std()
outliers = np.abs(readings - mean) > 1.2 * std
print(f"mean={mean:.3f} std={std:.3f}")
print("outliers:", readings[outliers])

# Mask dtype and conversions
print("mask dtype:", hot.dtype)
print("mask as int:", hot.astype(np.int64))
print("mask as float:", hot.astype(np.float64))

# Empty selection
nothing = readings[readings > 100]
print("empty result:", repr(nothing), nothing.shape)

# Boolean array built by hand
manual = np.array([True, False] * 5)
print("alternating picks:", readings[manual])
