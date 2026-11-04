"""Work with triangular matrices using np.tri, np.tril and np.triu."""
import numpy as np

T = np.tri(4)
print("tri(4):")
print(T)
print(repr(T))

Ti = np.tri(3, 5, k=1, dtype=int)
print("tri(3, 5, k=1, int):")
print(Ti)

m = np.arange(1, 17).reshape(4, 4)
print("Matrix:")
print(m)

print("tril:")
print(np.tril(m))
print("triu:")
print(np.triu(m))
print("triu k=1 (strict upper):")
print(np.triu(m, k=1))
print("tril k=-1 (strict lower):")
print(np.tril(m, k=-1))

# Split a matrix into lower + strict upper
L = np.tril(m)
U = np.triu(m, k=1)
print("L + U reconstructs m:", np.array_equal(L + U, m))

# Symmetrize from the upper triangle
sym = np.triu(m) + np.triu(m, k=1).T
print("Symmetric from upper triangle:")
print(sym)
print("Is symmetric:", np.array_equal(sym, sym.T))

# Pairwise "distance" matrix, keep unique pairs only
pts = np.array([0.0, 1.5, 4.0, 4.5])
d = np.abs(pts[:, None] - pts[None, :])
upper = np.triu(d, k=1)
print("Pair distances (upper):")
print(upper)
print("Sum of unique pair distances:", upper.sum())

# Number of lower-triangle entries
mask = np.tri(5, dtype=bool)
print("Lower-triangle mask:")
print(mask)
print("Count:", int(mask.sum()))
