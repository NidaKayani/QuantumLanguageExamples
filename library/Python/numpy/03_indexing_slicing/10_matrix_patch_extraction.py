"""Extracting patches, tiles and borders from a 2-D field using slicing."""
import numpy as np

# Deterministic "terrain" built from an LCG
def lcg(n, seed=7):
    out = np.empty(n, dtype=np.int64)
    state = seed
    for i in range(n):
        state = (1103515245 * state + 12345) % (2 ** 31)
        out[i] = state % 10
    return out

field = lcg(64).reshape(8, 8)
print("field:")
print(field)

# Split into 2x2 grid of 4x4 tiles
tiles = {}
for r in range(2):
    for c in range(2):
        tiles[(r, c)] = field[r * 4:(r + 1) * 4, c * 4:(c + 1) * 4]
for key, tile in tiles.items():
    print("tile", key, "sum =", tile.sum())
print("tile (1, 0):")
print(tiles[(1, 0)])

# Same tiling with reshape + swapaxes (all views)
blocks = field.reshape(2, 4, 2, 4).swapaxes(1, 2)
print("blocks shape:", blocks.shape)
print("block sums:")
print(blocks.sum(axis=(2, 3)))

# 3x3 patch around a point, clipped at the border
def patch(arr, r, c, radius=1):
    r0, r1 = max(r - radius, 0), min(r + radius + 1, arr.shape[0])
    c0, c1 = max(c - radius, 0), min(c + radius + 1, arr.shape[1])
    return arr[r0:r1, c0:c1]

print("patch at (3, 4):")
print(patch(field, 3, 4))
print("patch at corner (0, 7):")
print(repr(patch(field, 0, 7)))

# Border values in clockwise order
top = field[0, :]
right = field[1:, -1]
bottom = field[-1, -2::-1]
left = field[-2:0:-1, 0]
border = np.concatenate([top, right, bottom, left])
print("border length:", border.size)
print("border:", border)

# Downsample by taking every second element; pooled max per 2x2
print("downsampled:")
print(field[::2, ::2])
pooled = field.reshape(4, 2, 4, 2).max(axis=(1, 3))
print("2x2 max pooling:")
print(pooled)

# Upper triangle values with slicing loop vs np.triu
upper = np.concatenate([field[i, i + 1:] for i in range(8)])
print("upper triangle count:", upper.size, "sum:", upper.sum())
print("matches np.triu sum:", upper.sum() == np.triu(field, 1).sum())
