"""Joining arrays with concatenate, stack, vstack, hstack, column_stack and dstack."""
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("a:")
print(a)
print("b:")
print(b)

print("concatenate axis=0:")
print(np.concatenate((a, b), axis=0))
print("concatenate axis=1:")
print(np.concatenate([a, b], axis=1))
print("concatenate axis=None:", np.concatenate((a, b), axis=None))

s0 = np.stack([a, b])
print("stack axis=0 shape:", s0.shape)
print(s0)
s2 = np.stack([a, b], axis=-1)
print("stack axis=-1 shape:", s2.shape)
print(repr(s2))

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("vstack 1-D:")
print(np.vstack([x, y]))
print("hstack 1-D:", np.hstack([x, y]))
print("column_stack:")
cs = np.column_stack((x, y))
print(cs)
print(repr(cs))
print("hstack 2-D:")
print(np.hstack([a, b]))
print("vstack 2-D shape:", np.vstack([a, b]).shape)

d = np.dstack((x, y))
print("dstack shape:", d.shape)
print(d)
print("dstack 2-D shape:", np.dstack([a, b]).shape)

# build a design matrix: bias column + features
temps = np.array([20.5, 22.0, 19.0, 25.5])
humid = np.array([0.30, 0.45, 0.50, 0.25])
X = np.column_stack([np.ones_like(temps), temps, humid])
print("design matrix:")
print(X)

# gather per-day rows into a table
days = [np.array([3, 1, 4]), np.array([1, 5, 9]), np.array([2, 6, 5])]
table = np.stack(days)
print("stacked days:")
print(table)
print("column means:", table.mean(axis=0))

mixed = np.concatenate([np.array([1, 2]), np.array([0.5])])
print("mixed concat promotes dtype:", repr(mixed))
flags = np.concatenate([np.array([True]), np.array([False, True])])
print(repr(flags))
