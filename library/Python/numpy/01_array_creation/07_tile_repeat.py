"""Replicate data with np.tile and np.repeat, including along specific axes."""
import numpy as np

base = np.array([1, 2, 3])
print("Base:", base)
print("tile x3:", np.tile(base, 3))
print("repeat x3:", np.repeat(base, 3))
print(repr(np.repeat(base, [1, 2, 3])))

tiled2d = np.tile(base, (2, 2))
print("tile (2, 2):")
print(tiled2d)

block = np.array([[1, 0], [0, 1]])
print("Tiled block 2x3:")
print(np.tile(block, (2, 3)))

m = np.array([[1, 2], [3, 4]])
print("repeat axis=0:")
print(np.repeat(m, 2, axis=0))
print("repeat axis=1:")
print(np.repeat(m, 3, axis=1))
print("repeat no axis (flattened):", np.repeat(m, 2))

# Upscale a tiny image by 2x in both directions
img = np.array([[0, 9], [5, 1]])
up = np.repeat(np.repeat(img, 2, axis=0), 2, axis=1)
print("Upscaled image:")
print(up)
print(repr(up))

# Checkerboard via tile
checker = np.tile(np.array([[0, 1], [1, 0]]), (3, 3))
print("Checkerboard 6x6:")
print(checker)

# Labels for grouped data
groups = np.repeat(np.arange(3), [2, 4, 1])
print("Group labels:", groups)
print("Group sizes:", np.bincount(groups))

floats = np.tile(np.array([0.5, 1.5]), 3)
print("Tiled floats:", floats)
