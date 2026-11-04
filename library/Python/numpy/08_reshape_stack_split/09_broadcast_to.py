"""Explicit broadcasting with np.broadcast_to, broadcast_arrays and broadcast_shapes."""
import numpy as np

row = np.array([1, 2, 3])
tiled = np.broadcast_to(row, (4, 3))
print(tiled)
print(repr(tiled))
print("shape:", tiled.shape, "writeable:", tiled.flags.writeable)
print("strides:", tiled.strides, "(row stride 0 -> no copy)")

col = np.array([[10], [20]])
print("column broadcast to (2, 5):")
print(np.broadcast_to(col, (2, 5)))

scalar_grid = np.broadcast_to(7.5, (2, 3))
print("scalar broadcast:")
print(scalar_grid)

try:
    np.broadcast_to(np.array([1, 2]), (3, 3))
except ValueError as exc:
    print("incompatible broadcast raised ValueError")

print("broadcast_shapes:", np.broadcast_shapes((3, 1), (1, 4)))
print("broadcast_shapes 3 inputs:", np.broadcast_shapes((5, 1, 3), (4, 1), (3,)))

xs = np.array([0, 1, 2])
ys = np.array([[0], [10]])
bx, by = np.broadcast_arrays(xs, ys)
print("broadcast_arrays x:")
print(bx)
print("broadcast_arrays y:")
print(by)
print("sum grid:")
print(bx + by)

# make a writable copy when you need to modify
board = np.broadcast_to(np.array([0, 1]), (3, 2)).copy()
board[1, 0] = 5
print("modified copy:")
print(board)

# compare each sample to per-feature thresholds
samples = np.array([[0.2, 5.0, 3.0], [0.9, 2.0, 7.5], [0.5, 8.0, 1.0]])
thresholds = np.array([0.5, 4.0, 2.0])
T = np.broadcast_to(thresholds, samples.shape)
print("threshold matrix:")
print(T)
above = samples > T
print("above threshold:")
print(above)
print("features above per sample:", above.sum(axis=1))

# broadcast a (3,1,1) array to an image stack
gains = np.arange(1.0, 4.0).reshape(3, 1, 1)
stack = np.broadcast_to(gains, (3, 2, 2))
print("gain stack shape:", stack.shape)
print(stack)
