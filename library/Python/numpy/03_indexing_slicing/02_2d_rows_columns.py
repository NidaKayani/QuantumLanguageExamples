"""2-D indexing: elements, rows, columns, sub-blocks and strided sub-grids."""
import numpy as np

grid = np.arange(1, 37).reshape(6, 6)
print("grid:")
print(grid)

# Element access, tuple-style and chained
print("grid[2, 3] =", grid[2, 3])
print("grid[2][3] =", grid[2][3])
print("grid[-1, -1] =", grid[-1, -1])

# Rows and columns
print("row 0:", grid[0])
print("row -2:", grid[-2, :])
print("column 1:", grid[:, 1])
print("last column:", grid[:, -1])
print("column 2 kept 2-D:")
print(grid[:, 2:3])
print(repr(grid[:, 2:3]))

# Sub-blocks
print("top-left 3x3:")
print(grid[:3, :3])
print("bottom-right 2x2:")
print(grid[-2:, -2:])
print("inner block (strip border):")
print(grid[1:-1, 1:-1])

# Strided sub-grids
print("every other row and column:")
print(grid[::2, ::2])
print("odd rows, reversed columns:")
print(grid[1::2, ::-1])

# Corners using slices with step = size - 1
print("corners:")
print(grid[::5, ::5])

# Row and column statistics
print("row sums:", grid.sum(axis=1))
print("column means:", grid.mean(axis=0))

# Diagonal and anti-diagonal via indexing
idx = np.arange(6)
print("diagonal:", grid[idx, idx])
print("anti-diagonal:", grid[idx, idx[::-1]])

# Shapes of different selections
for name, sel in [("grid[0]", grid[0]), ("grid[0:1]", grid[0:1]),
                  ("grid[:, 0]", grid[:, 0]), ("grid[:, :1]", grid[:, :1]),
                  ("grid[2, 3]", grid[2, 3])]:
    print(f"{name:12s} shape={np.shape(sel)}")

# Float matrix: extract a checkerboard of values
m = np.linspace(0.0, 1.0, 16).reshape(4, 4)
print(repr(m))
print("m[1::2, ::2]:")
print(m[1::2, ::2])
