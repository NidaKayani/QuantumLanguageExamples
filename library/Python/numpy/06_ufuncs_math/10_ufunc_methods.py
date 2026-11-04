"""Ufunc methods .reduce, .accumulate and .outer on np.add, np.multiply and np.maximum."""
import numpy as np

v = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print("v:", v)
print("np.add.reduce:       ", np.add.reduce(v))
print("np.multiply.reduce:  ", np.multiply.reduce(v))
print("np.maximum.reduce:   ", np.maximum.reduce(v))
print("np.add.accumulate:     ", np.add.accumulate(v))
print("np.multiply.accumulate:", np.multiply.accumulate(v))
print("np.maximum.accumulate: ", np.maximum.accumulate(v))
print("np.minimum.accumulate: ", np.minimum.accumulate(v))
print(repr(np.add.accumulate(v)))

print("reduce matches sum/prod/max:",
      np.add.reduce(v) == v.sum(),
      np.multiply.reduce(v) == v.prod(),
      np.maximum.reduce(v) == v.max())

# reduce along axes of a 2-D array
m = np.array([[2, 7, 1], [8, 2, 8], [1, 8, 2], [8, 4, 5]])
print("m:")
print(m)
print("add.reduce axis=0:", np.add.reduce(m, axis=0))
print("add.reduce axis=1:", np.add.reduce(m, axis=1))
print("maximum.reduce axis=1:", np.maximum.reduce(m, axis=1))
print("multiply.reduce axis=None:", np.multiply.reduce(m, axis=None))
print("add.accumulate axis=1:")
print(np.add.accumulate(m, axis=1))
print("maximum.accumulate axis=0:")
print(np.maximum.accumulate(m, axis=0))

# outer methods build tables
a = np.arange(1, 6)
b = np.array([10, 20, 30])
print("np.add.outer(a, b):")
print(np.add.outer(a, b))
print("np.multiply.outer(a, a):")
print(np.multiply.outer(a, a))
print("np.maximum.outer(a, a):")
print(np.maximum.outer(a, a))

# float version: running product of probabilities and running max of a curve
p = np.array([0.9, 0.95, 0.8, 0.99, 0.85])
print("survival probability:", np.multiply.accumulate(p))
curve = np.sin(np.linspace(0, 3 * np.pi, 10)) * np.linspace(1, 2, 10)
print("curve:", np.round(curve, 3))
print("running max:", np.round(np.maximum.accumulate(curve), 3))

# reduce with an initial value and keepdims
print("add.reduce initial=100:", np.add.reduce(v, initial=100))
print("maximum.reduce empty with initial:", np.maximum.reduce(np.array([], dtype=np.int64), initial=-1))
print("add.reduce keepdims:")
print(np.add.reduce(m, axis=1, keepdims=True))

# reduceat: sums of consecutive segments
print("add.reduceat segments [0:3],[3:5],[5:]:", np.add.reduceat(v, [0, 3, 5]))
