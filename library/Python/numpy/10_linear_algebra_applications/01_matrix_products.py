"""Matrix and vector products: np.dot, np.matmul, the @ operator, inner and outer."""
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])
v = np.array([1, 0, -1])
w = np.array([2, 3, 4])

print("A =")
print(A)
print("B =")
print(B)

print("A @ B =")
print(A @ B)
print("np.matmul(A, B) equal:", bool(np.array_equal(np.matmul(A, B), A @ B)))
print("np.dot(A, B) equal:", bool(np.array_equal(np.dot(A, B), A @ B)))
print("B @ A =")
print(B @ A)
print(repr(B @ A))

print("A @ v =", A @ v)
print("v . w =", np.dot(v, w), "inner:", np.inner(v, w))

outer = np.outer(v, w)
print("outer(v, w) =")
print(outer)

# Multiplication table with outer
table = np.outer(np.arange(1, 6), np.arange(1, 6))
print("multiplication table:")
print(table)

# Batched matmul: stack of 2x2 matrices times a single 2x2
stack = np.array([[[1, 0], [0, 1]],
                  [[0, 1], [1, 0]],
                  [[2, 0], [0, 3]]])
M = np.array([[1, 2], [3, 4]])
print("batched stack @ M:")
print(stack @ M)
print("shape:", (stack @ M).shape)

# Elementwise vs matrix product
S = np.array([[1.5, -2.0], [0.5, 4.0]])
print("S * S (elementwise):")
print(S * S)
print("S @ S (matrix):")
print(S @ S)

# Associativity check and transpose rule (AB)^T = B^T A^T
print("(A @ B).T == B.T @ A.T:", bool(np.array_equal((A @ B).T, B.T @ A.T)))
C = np.array([[1, -1], [2, 0]])
print("(A @ B) @ C == A @ (B @ C):", bool(np.array_equal((A @ B) @ C, A @ (B @ C))))

# Inner of 2-D arrays: rows against rows
print("inner(A, A) (Gram matrix):")
print(np.inner(A, A))
print("A @ A.T same:", bool(np.array_equal(np.inner(A, A), A @ A.T)))
