"""Slice assignment with scalars, rows, columns and broadcasting."""
import numpy as np

# Build a 6x8 image canvas
img = np.zeros((6, 8))
img[0, :] = 1.0                          # scalar fills a row
img[:, 0] = np.arange(6) * 0.5           # 1-D array fills a column
img[2:4, 2:6] = [7.0, 8.0, 9.0, 10.0]    # row broadcast over 2 rows
img[4:, 5:] = [[1.5], [2.5]]             # column broadcast over 3 columns
print("canvas:")
print(img)

# Add a gradient to the right half using broadcasting
grad = np.linspace(0.0, 0.3, 4)
img[:, 4:] += grad
print("after adding gradient to right half:")
print(img)

# Fill a strided pattern (checkerboard)
board = np.zeros((5, 5), dtype=np.int64)
board[::2, ::2] = 1
board[1::2, 1::2] = 1
print("checkerboard:")
print(board)

# Border frame
frame = np.full((5, 7), 8)
frame[1:-1, 1:-1] = 0
print("frame:")
print(repr(frame))

# Assign one slice to another (overlapping shift)
seq = np.arange(10)
seq[1:] = seq[:-1].copy()
print("shifted right:", seq)

# Swap two rows using fancy-free slicing and a temp copy
m = np.arange(12).reshape(3, 4)
tmp = m[0].copy()
m[0] = m[2]
m[2] = tmp
print("rows 0 and 2 swapped:")
print(m)

# Swap two columns in one shot
m[:, [1, 3]] = m[:, [3, 1]]
print("columns 1 and 3 swapped:")
print(m)

# Broadcasting a column vector into a block
weights = np.array([[1.0], [10.0], [100.0]])
table = np.ones((3, 4))
table[:, 1:3] = weights
print("table:")
print(table)

# Type casting on assignment: floats truncated into int array
ints = np.zeros(5, dtype=np.int64)
ints[1:4] = [1.9, 2.5, -3.7]
print("int assignment truncates:", repr(ints))
