"""Polynomial evaluation and interpolation with np.polyval, np.vander and np.linalg.solve."""
import numpy as np

# p(x) = 2x^3 - 3x^2 + 0x + 5 (highest power first)
p = np.array([2, -3, 0, 5])
xs = np.arange(-2, 4)
print("coefficients:", p)
print("x:", xs)
vals = np.polyval(p, xs)
print("p(x):", vals)
print(repr(vals))

# Same thing with a Vandermonde matrix-vector product
V = np.vander(xs, len(p))
print("Vandermonde matrix:")
print(V)
print("V @ p:", V @ p, "matches:", bool(np.array_equal(V @ p, vals)))

# Increasing-power Vandermonde
print("increasing=True:")
print(np.vander(np.array([1, 2, 3]), 4, increasing=True))

# Horner's method by hand
def horner(coeffs, x):
    acc = np.zeros_like(x, dtype=float)
    for c in coeffs:
        acc = acc * x + c
    return acc

print("Horner:", horner(p, xs.astype(float)))

# Interpolate a cubic through 4 points by solving V c = y
px = np.array([0.0, 1.0, 2.0, 4.0])
py = np.array([1.0, 3.0, 2.0, 5.0])
Vi = np.vander(px)
coef = np.linalg.solve(Vi, py)
print("interpolating cubic coefficients:", np.round(coef, 6))
print("reproduces data:", np.round(np.polyval(coef, px), 6))
grid = np.linspace(0.0, 4.0, 9)
print("grid:", grid)
print("interpolant on grid:", np.round(np.polyval(coef, grid), 6))
print("det of Vandermonde:", f"{np.linalg.det(Vi):.6f}")

# Polynomial arithmetic helpers
q = np.array([1, -1])  # x - 1
prod = np.polymul(p, q)
print("p * (x - 1):", prod)
quot, rem = np.polydiv(prod.astype(float), q.astype(float))
print("divided back:", quot, "remainder:", rem)
print("sum p + q:", np.polyadd(p, q))
print("derivative of p:", np.polyder(p))
print("antiderivative of p:", np.polyint(p))

# Evaluate a polynomial on a matrix of inputs
M = np.array([[0.5, 1.5], [-1.0, 2.5]])
print("p evaluated elementwise on matrix:")
print(np.polyval(p, M))

# Polynomial with roots 1, 2, 3 via np.poly, checked with polyval
coeffs_from_roots = np.poly([1.0, 2.0, 3.0])
print("poly from roots:", coeffs_from_roots)
print("values at roots:", np.polyval(coeffs_from_roots, np.array([1.0, 2.0, 3.0])))
