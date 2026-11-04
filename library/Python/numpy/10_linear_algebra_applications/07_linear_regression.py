"""Least-squares linear and polynomial regression via the normal equations and np.linalg.solve."""
import numpy as np

# House size (100 m^2) vs price (k$) with deterministic "noise"
size = np.array([0.6, 0.8, 1.0, 1.1, 1.3, 1.5, 1.7, 2.0, 2.2, 2.5])
noise = np.array([3.0, -2.0, 1.5, -4.0, 2.5, 0.0, -1.5, 3.5, -2.5, 1.0])
price = 50.0 + 120.0 * size + noise
print("size: ", size)
print("price:", price)

# Design matrix with intercept column
X = np.column_stack((np.ones_like(size), size))
print("design matrix (first 4 rows):")
print(X[:4])

XtX = X.T @ X
Xty = X.T @ price
print("X^T X =")
print(np.round(XtX, 6))
beta = np.linalg.solve(XtX, Xty)
print("intercept, slope:", np.round(beta, 6))

pred = X @ beta
resid = price - pred
print("predictions:", np.round(pred, 4))
print("residuals:", np.round(resid, 4))
ss_res = np.sum(resid ** 2)
ss_tot = np.sum((price - price.mean()) ** 2)
print("R^2 =", f"{1 - ss_res / ss_tot:.6f}")
print("residuals orthogonal to X:", bool(np.allclose(X.T @ resid, 0.0, atol=1e-8)))

new_sizes = np.array([1.2, 3.0])
print("forecast:", np.round(np.column_stack((np.ones(2), new_sizes)) @ beta, 4))

# Quadratic fit using a Vandermonde design matrix
t = np.arange(8, dtype=float)
y = 2.0 - 1.5 * t + 0.25 * t ** 2
V = np.vander(t, 3)  # columns: t^2, t, 1
print("Vandermonde matrix:")
print(V)
coeffs = np.linalg.solve(V.T @ V, V.T @ y)
print("recovered coefficients (t^2, t, 1):", np.round(coeffs, 6))
print(repr(np.round(coeffs, 6)))
print("fit evaluated with polyval:", np.round(np.polyval(coeffs, t), 6) + 0.0)

# Multiple regression with two features
x1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
x2 = np.array([2.0, 1.0, 4.0, 3.0, 6.0, 5.0])
target = 1.0 + 2.0 * x1 - 0.5 * x2
X2 = np.column_stack((np.ones(6), x1, x2))
w = np.linalg.solve(X2.T @ X2, X2.T @ target)
print("multi-feature weights:", np.round(w, 6))
print("rank of design:", np.linalg.matrix_rank(X2))
