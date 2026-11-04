"""Expressing common linear algebra with np.einsum subscripts."""
import numpy as np

A = np.arange(1, 7).reshape(2, 3)
B = np.arange(1, 13).reshape(3, 4)
S = np.array([[2, 1, 0], [1, 3, 1], [0, 1, 4]])
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

print("A =")
print(A)
print("B =")
print(B)

prod = np.einsum("ij,jk->ik", A, B)
print("einsum('ij,jk->ik') =")
print(prod)
print("equals A @ B:", bool(np.array_equal(prod, A @ B)))
print(repr(prod))

print("trace 'ii':", np.einsum("ii", S), "np.trace:", np.trace(S))
print("diagonal 'ii->i':", np.einsum("ii->i", S))
print("column sums 'ij->j':", np.einsum("ij->j", A))
print("row sums 'ij->i':", np.einsum("ij->i", A))
print("total 'ij->':", np.einsum("ij->", A))
print("transpose 'ij->ji':")
print(np.einsum("ij->ji", A))

print("dot 'i,i->':", np.einsum("i,i->", u, v), np.dot(u, v))
print("outer 'i,j->ij':")
print(np.einsum("i,j->ij", u, v))
print("matrix-vector 'ij,j->i':", np.einsum("ij,j->i", S, u), S @ u)
print("elementwise 'ij,ij->ij':")
print(np.einsum("ij,ij->ij", A, A))

# Quadratic form u^T S u
print("quadratic form 'i,ij,j->':", np.einsum("i,ij,j->", u, S, u), u @ S @ u)

# Batched matrix multiply
batch = np.arange(12).reshape(3, 2, 2)
M = np.array([[1, 1], [0, 1]])
out = np.einsum("bij,jk->bik", batch, M)
print("batched 'bij,jk->bik':")
print(out)
print("matches batch @ M:", bool(np.array_equal(out, batch @ M)))

# Row-wise dot products of two point sets
P = np.array([[1.0, 2.0], [3.0, -1.0], [0.5, 0.5]])
Q = np.array([[2.0, 0.0], [1.0, 1.0], [-2.0, 4.0]])
print("row dots 'ij,ij->i':", np.einsum("ij,ij->i", P, Q))
print("Gram matrix 'ik,jk->ij':")
print(np.einsum("ik,jk->ij", P, P))
