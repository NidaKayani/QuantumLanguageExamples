"""Pass dtype= to constructors like array, zeros, ones, arange and full."""
import numpy as np

a = np.array([1, 2, 3], dtype=np.float64)
print("array dtype=float64:", repr(a))

b = np.array([1.9, 2.1, -3.7], dtype=np.int64)
print("array of floats with dtype=int64:", repr(b))

c = np.zeros(4, dtype=np.int32)
print("zeros int32:", repr(c))
print("itemsize:", c.itemsize)

d = np.ones((2, 3), dtype=np.int16)
print("ones int16:")
print(d)
print(repr(d))

e = np.arange(0, 10, 3, dtype=np.float64)
print("arange float64:", repr(e))

f = np.full(3, 255, dtype=np.uint8)
print("full uint8:", repr(f))

g = np.eye(3, dtype=bool)
print("eye bool:")
print(g)

h = np.array([0, 1, 1, 0], dtype=bool)
print("bool from ints:", repr(h))

# The dtype objects themselves
for dt in [np.int8, np.int16, np.int32, np.int64, np.uint8, np.float32, np.float64, np.bool_]:
    t = np.dtype(dt)
    print(f"{t.name:>8}: kind={t.kind} itemsize={t.itemsize}")

print("np.dtype('int64') == np.int64:", np.dtype("int64") == np.int64)
print("Default int dtype:", np.array([1]).dtype)
print("Default float dtype:", np.array([1.0]).dtype)

# Memory saving with a smaller dtype
big = np.zeros(1000, dtype=np.int64)
small = np.zeros(1000, dtype=np.int8)
print("int64 bytes:", big.nbytes, "int8 bytes:", small.nbytes)

# Sum of int8 data is promoted to the platform integer
vals = np.array([100, 100, 100], dtype=np.int8)
print("int8 values:", repr(vals))
print("sum:", vals.sum(), "dtype of sum:", vals.sum().dtype)
