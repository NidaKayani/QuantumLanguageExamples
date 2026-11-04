"""Adding and removing length-1 axes: expand_dims, newaxis, squeeze, atleast_2d."""
import numpy as np

x = np.array([1.5, 2.5, 3.5])
print(repr(x), x.shape)

r = np.expand_dims(x, axis=0)
c = np.expand_dims(x, axis=1)
print("expand_dims axis=0:", r, r.shape)
print("expand_dims axis=1:")
print(c)
print("shape:", c.shape)
print("multiple axes (0, 2):", np.expand_dims(x, axis=(0, 2)).shape)
print("newaxis equivalents:", x[np.newaxis, :].shape, x[:, None].shape)

# outer-style broadcasting via an expanded axis
y = np.array([10, 20])
table = x[:, None] * y[None, :]
print("outer product table:")
print(table)
print(repr(table))

z = np.zeros((1, 3, 1, 2))
print("z shape:", z.shape)
print("squeeze:", np.squeeze(z).shape)
print("squeeze axis=0:", z.squeeze(axis=0).shape)
print("squeeze axis=2:", np.squeeze(z, axis=2).shape)

col = np.array([[7], [8], [9]])
print("column:")
print(col)
print("squeezed:", col.squeeze())
single = np.array([[[42]]])
s = single.squeeze()
print("squeeze to 0-d:", repr(s), s.ndim, int(s))

print("atleast_2d of scalar:", repr(np.atleast_2d(5)))
print("atleast_2d of 1-D:", repr(np.atleast_2d(x)))
m = np.arange(4).reshape(2, 2)
print("atleast_2d leaves 2-D alone:", np.atleast_2d(m) is m)
a2, b2 = np.atleast_2d(np.array([1, 2]), np.array([[3], [4]]))
print("multiple inputs:", a2.shape, b2.shape)
print("atleast_1d of scalar:", repr(np.atleast_1d(3.0)))
print("atleast_3d of 1-D shape:", np.atleast_3d(x).shape)


def as_matrix(data):
    """Accept a vector or a matrix and always return rows of samples."""
    return np.atleast_2d(np.asarray(data, dtype=float))


for item in ([1, 2, 3], [[1, 2], [3, 4]], 9):
    mat = as_matrix(item)
    print(f"input {item!r} -> shape {mat.shape}, row sums {mat.sum(axis=1)}")
