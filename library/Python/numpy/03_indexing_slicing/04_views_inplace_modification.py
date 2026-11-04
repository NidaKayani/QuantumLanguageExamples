"""Slices are views: modifying a slice changes the original array."""
import numpy as np

data = np.arange(10)
print("original:", data)

window = data[2:6]
print("window:", window)
window[:] = 0
print("after zeroing window, data:", data)

window += 7
print("after window += 7, data:", data)

# The view knows its base
print("window.base is data:", window.base is data)
print("np.shares_memory(window, data):", np.shares_memory(window, data))

# Strided view modifications
evens = data[::2]
evens *= -1
print("after negating evens:", data)

# 2-D views: column and row modifications
board = np.zeros((4, 5), dtype=np.int64)
board[1] = 3              # whole row
board[:, 3] = 9           # whole column
board[2:, :2] = 5         # sub-block
print("board:")
print(board)

col = board[:, 0]
col[...] = np.arange(4) * 10
print("after writing through column view:")
print(board)

# Views of views
inner = board[1:3, 1:4]
inner_row = inner[0]
inner_row[1] = -1
print("inner block:")
print(inner)
print("board after nested view write:")
print(repr(board))

# Reshape usually returns a view too
flat = np.arange(12, dtype=np.float64)
mat = flat.reshape(3, 4)
mat[1, 1] = 99.5
print("flat after mat write:", flat)
print("mat.base is flat:", mat.base is flat)

# ravel of a contiguous array is a view
r = mat.ravel()
r[0] = -2.5
print("mat after ravel write:")
print(mat)

# In-place ufuncs on a view
signal = np.linspace(0.0, 1.0, 9)
np.multiply(signal[4:], 2.0, out=signal[4:])
print("signal with doubled tail:")
print(signal)
