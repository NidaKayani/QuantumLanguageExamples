"""In-place operators (+=, -=, *=, /=, //=, %=, **=) and aliasing effects."""
import numpy as np

balance = np.array([100.0, 250.0, 75.5, 1000.0])
print("start:", balance)
balance += 50
print("after += 50:", balance)
balance *= 1.02
print("after *= 1.02:", balance)
balance -= np.array([10.0, 0.0, 5.5, 200.0])
print("after -= fees:", balance)
balance /= 2
print("after /= 2:", balance)
print(repr(balance))

counter = np.arange(10)
counter += 3
print("ints += 3:", counter)
counter *= 2
print("ints *= 2:", counter)
counter //= 3
print("ints //= 3:", counter)
counter %= 4
print("ints %= 4:", counter)
counter **= 2
print("ints **= 2:", counter)
print("dtype still:", counter.dtype)

# in-place on a view modifies the original
grid = np.zeros((4, 5))
row = grid[1]
row += 7
grid[:, 3] += 1.5
grid[2:, :2] *= 0  # no-op on zeros, still valid
grid[3, :] -= np.arange(5)
print("grid after view updates:")
print(grid)

# a copy is independent
c = grid.copy()
c += 100
print("original unchanged max:", grid.max(), " copy max:", c.max())

# in-place with broadcasting
mat = np.ones((3, 4), dtype=np.int64)
mat += np.array([0, 10, 20, 30])
mat *= np.array([[1], [2], [3]])
print("broadcast in-place:")
print(mat)

# int array cannot store float result in place; cast explicitly instead
vals = np.array([5, 9, 14])
try:
    vals /= 2
except TypeError as exc:
    print("int array /= 2 raised a TypeError:", isinstance(exc, TypeError))
half = vals / 2
print("vals:", vals, "half:", half)

# accumulate in a loop
acc = np.zeros(4)
for k in range(1, 6):
    acc += np.array([k, k * k, 1.0 / k, -k])
print("accumulated:", acc)
