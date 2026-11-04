"""Function forms of arithmetic: np.add, np.subtract, np.multiply, np.divide, np.power, np.mod, np.negative."""
import numpy as np

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

print("np.add:     ", np.add(x, y))
print("np.subtract:", np.subtract(x, y))
print("np.multiply:", np.multiply(x, y))
print("np.divide:  ", np.divide(x, y))
print("np.power:   ", np.power(y, 2))
print("np.mod:     ", np.mod(x, 4))
print("np.negative:", np.negative(x))
print(repr(np.divide(x, y)))

# operators and functions agree
pairs = [
    ("add", np.add, x + y),
    ("subtract", np.subtract, x - y),
    ("multiply", np.multiply, x * y),
    ("mod", np.mod, x % y),
]
for name, fn, expected in pairs:
    print(name, "matches operator:", np.array_equal(fn(x, y), expected))

# out= writes into a preallocated buffer
buf = np.empty(5)
np.multiply(x, 0.5, out=buf)
print("out buffer:", buf)
np.add(buf, 1.0, out=buf)
print("out buffer after add:", buf)

# where= applies only to selected positions
res = np.zeros(5)
np.divide(x, y, out=res, where=y > 3)
print("divide where y>3:", res)

# power with negative float exponent and fractional exponent
f = np.array([1.0, 4.0, 9.0, 16.0])
print("np.power(f, 0.5): ", np.power(f, 0.5))
print("np.power(f, -1.0):", np.power(f, -1.0))
print("np.power(2, arange(6)):", np.power(2, np.arange(6)))

# broadcasting through the function forms
m = np.arange(6).reshape(2, 3)
print("np.add(m, [10, 20, 30]):")
print(np.add(m, [10, 20, 30]))
print("np.multiply(m, [[2], [-1]]):")
print(np.multiply(m, [[2], [-1]]))
print("np.negative(m):")
print(np.negative(m))

# chaining: polynomial 3x^2 - 2x + 1 evaluated with ufuncs
t = np.linspace(-2, 2, 9)
poly = np.add(np.subtract(np.multiply(3, np.power(t, 2)), np.multiply(2, t)), 1)
print("t:   ", t)
print("poly:", poly)
print("matches direct:", np.allclose(poly, 3 * t ** 2 - 2 * t + 1))
