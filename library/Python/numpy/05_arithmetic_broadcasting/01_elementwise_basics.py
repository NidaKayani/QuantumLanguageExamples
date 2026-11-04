"""Elementwise arithmetic between two arrays of the same shape."""
import numpy as np

a = np.array([12, 7, 3, 25, 18, 9])
b = np.array([4, 2, 5, 6, 3, 4])

print("a =", a)
print("b =", b)
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // b =", a // b)
print("a % b  =", a % b)
print("b ** 2 =", b ** 2)
print("a ** b dtype:", (a ** b).dtype)
print(repr(a ** b))

x = np.array([1.5, 2.0, -0.5, 4.25])
y = np.array([0.5, 4.0, 2.0, -1.0])
print("x =", x)
print("y =", y)
print("x + y =", x + y)
print("x * y =", x * y)
print("x / y =", x / y)
print(repr(x - y))

# mixed int/float promotes to float64
mixed = a[:4] + x
print("int + float ->", mixed.dtype, mixed)

# 2-D elementwise
m1 = np.arange(1, 10).reshape(3, 3)
m2 = np.arange(9, 0, -1).reshape(3, 3)
print("m1:")
print(m1)
print("m2:")
print(m2)
print("m1 * m2 (elementwise, not matmul):")
print(m1 * m2)
print("m1 - m2:")
print(repr(m1 - m2))
print("sum of elementwise products:", (m1 * m2).sum())

# unary negation and positive
print("-a =", -a)
print("+x =", +x)
print("abs(-x) =", abs(-x))
