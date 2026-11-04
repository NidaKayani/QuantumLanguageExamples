"""Outer products and tables via [:, None] broadcasting and np.outer."""
import numpy as np

n = np.arange(1, 10)
table = n[:, None] * n[None, :]
print("9x9 multiplication table:")
print(table)

print("np.outer gives the same:", np.array_equal(table, np.outer(n, n)))

# addition table modulo 7 (a small group table)
z7 = np.arange(7)
add_mod7 = (z7[:, None] + z7) % 7
print("addition mod 7:")
print(add_mod7)

# distance matrix between points on a line
pts = np.array([0.0, 1.5, 4.0, 4.5, 9.0])
dist = np.abs(pts[:, None] - pts[None, :])
print("pairwise distances:")
print(dist)
print(repr(dist[1]))

# 2-D points: squared distances via a third axis
xy = np.array([[0, 0], [3, 4], [6, 8], [1, 1]])
diff = xy[:, None, :] - xy[None, :, :]
print("diff shape:", diff.shape)
sq = (diff ** 2).sum(axis=-1)
print("squared distances:")
print(sq)
print("euclidean:")
print(np.sqrt(sq))

# outer with floats: compound interest table
rates = np.array([0.01, 0.03, 0.05])
years = np.arange(0, 6)
growth = (1 + rates[:, None]) ** years
print("growth factors (rate x year):")
print(np.round(growth, 4))

# outer of a vector with itself is a rank-1 matrix
u = np.array([1.0, -2.0, 0.5])
P = np.outer(u, u)
print("outer(u, u):")
print(P)
print("symmetric:", np.array_equal(P, P.T))

# comparison table
cmp = n[:5, None] < n[None, :5]
print("i < j table:")
print(cmp)
