"""Vector and matrix norms, matrix rank and trace."""
import numpy as np

v = np.array([3.0, -4.0, 12.0])
print("v =", v)
print("L2 norm:", f"{np.linalg.norm(v):.6f}")
print("L1 norm:", f"{np.linalg.norm(v, 1):.6f}")
print("max norm:", f"{np.linalg.norm(v, np.inf):.6f}")
unit = v / np.linalg.norm(v)
print("unit vector:", np.round(unit, 6))
print("unit length:", f"{np.linalg.norm(unit):.6f}")

M = np.array([[1.0, 2.0, 2.0],
              [-3.0, 0.0, 4.0],
              [0.0, 5.0, -1.0]])
print("M =")
print(M)
print("Frobenius norm:", f"{np.linalg.norm(M):.6f}", f"{np.linalg.norm(M, 'fro'):.6f}")
print("manual Frobenius:", f"{np.sqrt(np.sum(M ** 2)):.6f}")
print("max column sum (ord=1):", f"{np.linalg.norm(M, 1):.6f}")
print("max row sum (ord=inf):", f"{np.linalg.norm(M, np.inf):.6f}")

# Row-wise norms with axis
points = np.array([[0.0, 0.0], [3.0, 4.0], [1.0, 1.0], [-6.0, 8.0]])
print("row norms:", np.round(np.linalg.norm(points, axis=1), 6))
print("column norms:", np.round(np.linalg.norm(points, axis=0), 6))

# Pairwise distance matrix via broadcasting
diff = points[:, None, :] - points[None, :, :]
dist = np.linalg.norm(diff, axis=2)
print("pairwise distances:")
print(np.round(dist, 6))

# Rank
full = np.array([[1, 2], [3, 4]])
deficient = np.array([[1, 2, 3], [2, 4, 6], [1, 0, 1]])
zero = np.zeros((3, 3))
print("rank full:", np.linalg.matrix_rank(full))
print("rank deficient:", np.linalg.matrix_rank(deficient))
print("rank zero:", np.linalg.matrix_rank(zero))
print("rank identity(4):", np.linalg.matrix_rank(np.eye(4)))
print("rank outer product:", np.linalg.matrix_rank(np.outer([1, 2, 3], [4, 5, 6])))

# Trace
T = np.arange(1, 10).reshape(3, 3)
print("T =")
print(T)
print("trace:", np.trace(T), "diag:", np.diagonal(T), "sum of diag:", T.diagonal().sum())
print("offset trace (k=1):", np.trace(T, offset=1))
print("trace(T @ T.T) = ||T||_F^2:", np.trace(T @ T.T), np.sum(T ** 2))
print(repr(np.diag(np.diag(T))))
