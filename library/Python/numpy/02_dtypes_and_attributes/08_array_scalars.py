"""Work with NumPy array scalars such as np.int64 and np.float64 and look at their repr."""
import numpy as np

data = np.array([3, 1, 4, 1, 5, 9, 2, 6])
total = data.sum()
print("sum:", total)
print("repr(sum):", repr(total))
print("type:", type(total).__name__)

first = data[0]
print("data[0]:", first, repr(first), type(first).__name__)

avg = data.mean()
print("mean:", avg, repr(avg), type(avg).__name__)

biggest = data.max()
print("max repr:", repr(biggest))

x = np.float64(2.5)
y = np.int64(7)
print("np.float64(2.5):", x, repr(x))
print("np.int64(7):", y, repr(y))
print("y * x:", repr(y * x))
print("y // 2:", repr(y // 2))
print("y + 1 (Python int):", repr(y + 1))
print("x + 1.0:", repr(x + 1.0))

b = data[0] > data[1]
print("comparison scalar:", b, repr(b), type(b).__name__)

# Array scalars behave like Python numbers
print("isinstance float64 of float:", isinstance(x, float))
print("isinstance int64 of int:", isinstance(y, int))
print("int(y) + float(x):", int(y) + float(x))
print("dtype of scalar:", y.dtype, x.dtype)
print("np.int8(100):", repr(np.int8(100)))
print("np.uint8(250):", repr(np.uint8(250)))
print("np.float32(0.1):", repr(np.float32(0.1)))
print("np.bool_(True):", repr(np.bool_(True)))

# Scalars inside containers show their repr
stats = [data.min(), data.max(), data.mean()]
print("list of scalars:", stats)
print("as Python values:", [s.item() for s in stats])

# Zero-dimensional array vs scalar
zero_d = np.array(5)
print("0-d array:", repr(zero_d), "ndim", zero_d.ndim)
print("indexed with ():", repr(zero_d[()]))

print("np.float64(1/3):", repr(np.float64(1 / 3)))
print("std:", repr(np.array([1.0, 2.0, 3.0, 4.0]).std()))
