"""Construct identity matrices and diagonal arrays with eye, identity and diag."""
import numpy as np

I3 = np.identity(3)
print("identity(3):")
print(I3)
print(repr(I3))

E = np.eye(4, dtype=int)
print("eye(4, int):")
print(E)

rect = np.eye(3, 5)
print("Rectangular eye(3, 5):")
print(rect)

upper = np.eye(4, k=1, dtype=int)
lower = np.eye(4, k=-1, dtype=int)
print("Super-diagonal:")
print(upper)
print("Sub-diagonal:")
print(lower)

# Tridiagonal matrix: 2 on the diagonal, -1 off-diagonal
tri = 2 * np.eye(5, dtype=int) - np.eye(5, k=1, dtype=int) - np.eye(5, k=-1, dtype=int)
print("Tridiagonal:")
print(tri)
print(repr(tri))

d = np.diag([1, 2, 3])
print("diag from list:")
print(d)
print(repr(d))

m = np.arange(1, 10).reshape(3, 3)
print("Matrix:")
print(m)
print("Main diagonal:", np.diag(m))
print("k=1 diagonal:", np.diag(m, k=1))
print("k=-1 diagonal:", np.diag(m, k=-1))
print("Trace:", np.trace(m))

offset = np.diag([7, 8], k=1)
print("diag with k=1 builds a 3x3:")
print(offset)

scaled = np.diag([0.5, 2.0]) @ np.array([[4.0, 4.0], [1.0, 1.0]])
print("Row scaling via diag:")
print(scaled)

print("I @ m equals m:", np.array_equal(np.eye(3) @ m, m))
