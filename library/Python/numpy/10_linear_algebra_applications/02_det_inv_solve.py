"""Determinants, inverses and solving linear systems with np.linalg."""
import numpy as np

A = np.array([[4.0, -2.0, 1.0],
              [-2.0, 4.0, -2.0],
              [1.0, -2.0, 4.0]])
b = np.array([11.0, -16.0, 17.0])

print("A =")
print(A)
print("b =", b)

det = np.linalg.det(A)
print("det(A) =", f"{det:.6f}")

A_inv = np.linalg.inv(A)
print("inv(A) =")
print(np.round(A_inv, 6))
print("A @ inv(A) ~ I:")
print(np.round(A @ A_inv, 6) + 0.0)
print("allclose to identity:", bool(np.allclose(A @ A_inv, np.eye(3))))

x = np.linalg.solve(A, b)
print("solution x =", np.round(x, 6))
print(repr(np.round(x, 6)))
print("residual small:", bool(np.allclose(A @ x, b)))
print("solve matches inv @ b:", bool(np.allclose(x, A_inv @ b)))

# Solve for several right-hand sides at once
Bm = np.array([[1.0, 0.0],
               [0.0, 1.0],
               [1.0, 1.0]])
X = np.linalg.solve(A, Bm)
print("multiple RHS solution:")
print(np.round(X, 6))

# Simple 2x2 example with an exact rational answer
P = np.array([[2.0, 1.0], [1.0, 3.0]])
q = np.array([3.0, 5.0])
print("2x2 det:", f"{np.linalg.det(P):.6f}", "solution:", np.round(np.linalg.solve(P, q), 6))

# Determinant properties
Q = np.array([[1.0, 2.0], [3.0, 4.0]])
R = np.array([[0.0, 1.0], [5.0, 2.0]])
dQ, dR = np.linalg.det(Q), np.linalg.det(R)
print(f"det(Q)={dQ:.6f} det(R)={dR:.6f} det(QR)={np.linalg.det(Q @ R):.6f} product={dQ * dR:.6f}")
print(f"det(Q.T)={np.linalg.det(Q.T):.6f} det(2Q)={np.linalg.det(2 * Q):.6f}")

# Singular matrix detection
S = np.array([[1.0, 2.0], [2.0, 4.0]])
print("singular det:", f"{abs(np.linalg.det(S)):.6f}")
try:
    np.linalg.inv(S)
    print("inverted?!")
except np.linalg.LinAlgError as exc:
    print("LinAlgError:", exc)

# Integer matrix determinant rounded to int
M = np.array([[2, 0, 1], [1, 3, 2], [1, 1, 2]])
print("integer det:", int(round(np.linalg.det(M))))
