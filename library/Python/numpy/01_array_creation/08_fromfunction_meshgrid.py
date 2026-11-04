"""Build arrays from index formulas using np.fromfunction and np.meshgrid."""
import numpy as np

dist = np.fromfunction(lambda i, j: abs(i - j), (5, 5), dtype=int)
print("|i - j| matrix:")
print(dist)
print(repr(dist))

hilbert = np.fromfunction(lambda i, j: 1.0 / (i + j + 1), (4, 4))
print("Hilbert matrix:")
print(np.round(hilbert, 4))

times = np.fromfunction(lambda i, j: (i + 1) * (j + 1), (3, 6), dtype=int)
print("Times table:")
print(times)

xs = np.array([0, 1, 2, 3])
ys = np.array([10, 20, 30])
X, Y = np.meshgrid(xs, ys)
print("X grid:")
print(X)
print("Y grid:")
print(Y)
print("X + Y:")
print(X + Y)

Xi, Yi = np.meshgrid(xs, ys, indexing="ij")
print("ij indexing shapes:", Xi.shape, Yi.shape)
print(Xi)

# Evaluate a function over a grid
gx = np.linspace(-1, 1, 5)
GX, GY = np.meshgrid(gx, gx)
r2 = GX ** 2 + GY ** 2
print("x^2 + y^2 over grid:")
print(r2)
inside = r2 <= 1.0
print("Inside unit circle:")
print(inside.astype(int))
print("Points inside:", int(inside.sum()))

eq = np.fromfunction(lambda i, j: i == j, (3, 3), dtype=int)
print("Boolean identity:", repr(eq))
