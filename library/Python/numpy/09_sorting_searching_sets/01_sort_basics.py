"""Basic np.sort usage: 1-D, 2-D along each axis, descending order and in-place sorting."""
import numpy as np

scores = np.array([72, 95, 58, 88, 95, 61, 79, 84, 58, 90])
print("original:", scores)

ascending = np.sort(scores)
print("ascending:", ascending)
print("descending:", np.sort(scores)[::-1])
print(repr(ascending))

# Original is untouched by np.sort; ndarray.sort works in place
copy = scores.copy()
copy.sort()
print("in-place sorted copy:", copy)
print("original still:", scores)

# 2-D sorting along different axes
grid = np.array([[9, 2, 7, 4],
                 [3, 8, 1, 6],
                 [5, 0, 11, 10]])
print("grid:")
print(grid)
print("sorted along rows (axis=1):")
print(np.sort(grid, axis=1))
print("sorted along columns (axis=0):")
print(np.sort(grid, axis=0))
print("flattened sort (axis=None):")
print(np.sort(grid, axis=None))
print("each row descending:")
print(np.sort(grid, axis=1)[:, ::-1])

# Floats, including negative values
temps = np.array([12.5, -3.25, 0.0, 7.75, -10.5, 3.125])
sorted_temps = np.sort(temps)
print("temps sorted:", sorted_temps)
print(repr(sorted_temps))
print("coldest:", sorted_temps[0], "warmest:", sorted_temps[-1])

# Booleans sort False before True
flags = np.array([True, False, True, True, False])
print("flags sorted:", np.sort(flags))

# Check sortedness
is_sorted = np.all(ascending[:-1] <= ascending[1:])
print("ascending is sorted:", bool(is_sorted))
print("original is sorted:", bool(np.all(scores[:-1] <= scores[1:])))

# Median from sorted data
n = ascending.size
median = (ascending[n // 2 - 1] + ascending[n // 2]) / 2
print("median via sort:", median, "np.median:", np.median(scores))
