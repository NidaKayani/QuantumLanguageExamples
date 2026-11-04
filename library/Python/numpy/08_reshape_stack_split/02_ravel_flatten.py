"""Flattening arrays with ravel and flatten, and the view-versus-copy distinction."""
import numpy as np

grid = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(grid)

r = grid.ravel()
f = grid.flatten()
print("ravel:  ", r)
print("flatten:", f)
print(repr(r))

r[0] = 100
print("after r[0]=100, grid[0,0] =", grid[0, 0], "(ravel is a view)")
f[1] = 200
print("after f[1]=200, grid[0,1] =", grid[0, 1], "(flatten is a copy)")
grid[0, 0] = 1

print("C order:", grid.ravel(order="C"))
print("F order:", grid.ravel(order="F"))
print("flatten F:", grid.flatten("F"))
print("np.ravel function:", np.ravel(grid.T))

# ravel of a transposed (non-contiguous) array must copy
t = grid.T
rt = t.ravel()
print("transposed ravel:", rt)
print("shares memory with grid:", np.shares_memory(rt, grid))

# flat iterator and index conversion
print("grid.flat[4] =", grid.flat[4])
idx = np.ravel_multi_index((np.array([0, 1, 2]), np.array([2, 1, 0])), grid.shape)
print("flat indices of anti-diagonal:", idx)
print("values:", grid.ravel()[idx])
rows, cols = np.unravel_index(np.array([0, 4, 8]), grid.shape)
print("unravel 0,4,8 ->", rows, cols)

cube = np.arange(8.0).reshape(2, 2, 2) / 2
print(cube)
flat = cube.flatten()
print(repr(flat))
print("sorted descending:", np.sort(flat)[::-1])

mask = np.array([[True, False], [False, True]])
print(repr(mask.ravel()))
print("count true:", mask.ravel().sum())
