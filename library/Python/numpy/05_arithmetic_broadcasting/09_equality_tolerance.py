"""Exact vs approximate equality: np.array_equal, np.allclose, np.isclose."""
import numpy as np

a = np.array([0.1, 0.2, 0.3])
b = np.array([0.1 + 0.2 - 0.2, 0.2, 0.1 + 0.2])
print("a =", a)
print("b =", b)
print("a == b:", a == b)
print("array_equal:", np.array_equal(a, b))
print("allclose:", np.allclose(a, b))
print("isclose:", np.isclose(a, b))
print(repr(b - a))

# shape matters for array_equal
x = np.arange(6)
print("equal to reshaped?", np.array_equal(x, x.reshape(2, 3)))
print("equal to list?", np.array_equal(x, [0, 1, 2, 3, 4, 5]))
print("int vs float equal?", np.array_equal(np.array([1, 2]), np.array([1.0, 2.0])))

# tolerances
measured = np.array([100.0, 99.95, 100.2, 101.0])
target = 100.0
print("measured:", measured)
print("isclose default:", np.isclose(measured, target))
print("isclose atol=0.1:", np.isclose(measured, target, atol=0.1))
print("isclose rtol=0.005:", np.isclose(measured, target, rtol=0.005, atol=0.0))
print("allclose rtol=0.02:", np.allclose(measured, target, rtol=0.02))

# NaN handling
with_nan = np.array([1.0, np.nan, 3.0])
print("array_equal with nan:", np.array_equal(with_nan, with_nan))
print("array_equal equal_nan:", np.array_equal(with_nan, with_nan, equal_nan=True))
print("isclose equal_nan:", np.isclose(with_nan, with_nan, equal_nan=True))

# verifying an algebraic identity numerically
t = np.linspace(0, 1, 11)
lhs = (t + 1) ** 2
rhs = t ** 2 + 2 * t + 1
print("(t+1)^2 == t^2+2t+1 exactly?", np.array_equal(lhs, rhs))
print("allclose?", np.allclose(lhs, rhs))

# accumulated rounding error in repeated addition
total = np.zeros(3)
for _ in range(10):
    total += np.array([0.1, 0.2, 0.7])
print("total:", total)
print("total == [1, 2, 7]:", total == np.array([1.0, 2.0, 7.0]))
print("isclose:", np.isclose(total, [1.0, 2.0, 7.0]))

# broadcasting in isclose
grid = np.array([[0.0, 0.5, 1.0], [1.0000001, 2.0, 0.4999999]])
print("isclose(grid, [1.0, 0.5, 1.0]):")
print(np.isclose(grid, [1.0, 0.5, 1.0]))
print("array_equiv broadcasts:", np.array_equiv(np.array([1, 2]), np.array([[1, 2], [1, 2]])))
