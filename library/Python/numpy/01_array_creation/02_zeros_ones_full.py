"""Build constant-filled arrays with zeros, ones and full in several shapes."""
import numpy as np

z = np.zeros(5)
print("zeros(5):", z)
print(repr(z))

zi = np.zeros((2, 3), dtype=int)
print("int zeros (2,3):")
print(zi)
print(repr(zi))

o = np.ones((3, 2))
print("ones (3,2):")
print(o)

ob = np.ones(4, dtype=bool)
print("bool ones:", repr(ob))

sevens = np.full((2, 4), 7)
print("full with 7:")
print(sevens)
print(repr(sevens))

pi_grid = np.full((2, 2), 3.14159)
print("full with float:")
print(pi_grid)

# A simple "canvas" initialised with zeros and filled in
canvas = np.zeros((5, 5), dtype=int)
canvas[0, :] = 1
canvas[-1, :] = 1
canvas[:, 0] = 1
canvas[:, -1] = 1
canvas[2, 2] = 9
print("Bordered canvas:")
print(canvas)
print("Border cell count:", int((canvas == 1).sum()))

# Accumulator initialised with zeros
totals = np.zeros(3)
for row in [[1.0, 2.0, 3.0], [0.5, 0.5, 0.5], [2.0, 0.0, 1.0]]:
    totals += np.array(row)
print("Accumulated totals:", totals)

weights = np.ones(4) / 4
print("Uniform weights:", weights, "sum =", weights.sum())

cube = np.zeros((2, 2, 2))
print("zeros 3-D shape:", cube.shape)
print(cube)
