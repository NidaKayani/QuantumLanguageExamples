"""Create arrays from Python lists, tuples and nested lists with np.array and np.asarray."""
import numpy as np

temps = [21.5, 23.0, 19.75, 25.25, 22.0]
a = np.array(temps)
print("1-D from list:")
print(a)
print(repr(a))

counts = np.array((3, 1, 4, 1, 5, 9, 2, 6))
print("From tuple:", counts)
print(repr(counts))

grid = np.array([[1, 2, 3], [4, 5, 6]])
print("Nested list -> 2-D:")
print(grid)
print(repr(grid))
print("shape:", grid.shape)

cube = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3-D array:")
print(cube)
print("shape:", cube.shape)

mixed = np.array([1, 2.5, 3])
print("Mixed int/float upcasts:", repr(mixed))

flags = np.array([True, False, True, True])
print("Booleans:", repr(flags))

as_float = np.array([1, 2, 3], dtype=float)
print("Explicit float dtype:", repr(as_float))

# np.asarray does not copy an existing ndarray
b = np.asarray(a)
print("asarray returns same object:", b is a)
c = np.asarray([[0, 1], [1, 0]])
print("asarray from list:")
print(c)

# Back to Python lists
print("tolist:", grid.tolist())
print("sum of rows:", grid.sum(axis=1))
print("Empty array:", repr(np.array([])))
