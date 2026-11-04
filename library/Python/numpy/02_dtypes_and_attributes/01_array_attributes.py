"""Inspect shape, ndim, size, dtype, itemsize, nbytes and T on arrays of various ranks."""
import numpy as np


def describe(name, arr):
    print(f"{name}: shape={arr.shape} ndim={arr.ndim} size={arr.size} "
          f"dtype={arr.dtype} itemsize={arr.itemsize} nbytes={arr.nbytes}")


scalar = np.array(42)
vec = np.array([1.5, 2.5, 3.5])
mat = np.arange(12).reshape(3, 4)
cube = np.ones((2, 3, 4), dtype=bool)

describe("scalar", scalar)
describe("vec", vec)
describe("mat", mat)
describe("cube", cube)

print("0-d array:", scalar, repr(scalar))
print("Matrix:")
print(mat)
print("Transpose:")
print(mat.T)
print(repr(mat.T))
print("T shape:", mat.T.shape)
print("1-D transpose is unchanged:", vec.T, vec.T.shape)

print("len(mat) =", len(mat), "(first axis)")
print("mat.shape[1] =", mat.shape[1])

# Reshaping changes shape but not size
for new_shape in [(4, 3), (2, 6), (12,), (2, 2, 3)]:
    r = mat.reshape(new_shape)
    print(f"reshape{new_shape}: ndim={r.ndim} size={r.size}")

flat = mat.ravel()
print("ravel:", flat)

col = vec.reshape(-1, 1)
print("Column vector:")
print(col)
print("column shape:", col.shape)

print("Total bytes of three arrays:", vec.nbytes + mat.nbytes + cube.nbytes)
print("dtype names:", vec.dtype.name, mat.dtype.name, cube.dtype.name)
print("dtype kinds:", vec.dtype.kind, mat.dtype.kind, cube.dtype.kind)
