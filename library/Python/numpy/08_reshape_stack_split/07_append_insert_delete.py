"""Editing array contents with np.append, np.insert and np.delete (always new arrays)."""
import numpy as np

queue = np.array([10, 20, 30])
print(queue)

grown = np.append(queue, 40)
print("append scalar:", grown)
print("append list:", np.append(grown, [50, 60]))
print("original unchanged:", queue)

m = np.array([[1, 2], [3, 4]])
print("append without axis flattens:", np.append(m, [[5, 6]]))
print("append row (axis=0):")
print(np.append(m, [[5, 6]], axis=0))
print("append column (axis=1):")
col = np.append(m, [[9], [9]], axis=1)
print(col)
print(repr(col))

v = np.array([1.0, 2.0, 4.0, 5.0])
print("insert 3.0 at index 2:", np.insert(v, 2, 3.0))
print("insert several:", np.insert(v, [1, 3], [-1.0, -2.0]))
print("insert same index twice:", np.insert(v, [0, 0], [8.0, 9.0]))
print("insert at end:", np.insert(v, v.size, 6.0))

grid = np.arange(9).reshape(3, 3)
print(grid)
print("insert row of zeros at 1:")
print(np.insert(grid, 1, 0, axis=0))
print("insert column [7, 8, 9] at 0:")
print(np.insert(grid, 0, [7, 8, 9], axis=1))

w = np.arange(10, 20)
print("delete index 3:", np.delete(w, 3))
print("delete [0, 2, 4]:", np.delete(w, [0, 2, 4]))
print("delete slice 1:8:2:", np.delete(w, np.s_[1:8:2]))
print("delete boolean mask:", np.delete(w, w % 3 == 0))
print("delete row 1:")
print(np.delete(grid, 1, axis=0))
print("delete column 2:")
print(np.delete(grid, 2, axis=1))

# maintain a sorted list of scores
scores = np.array([55, 70, 88])
for new in [62, 95, 40]:
    pos = np.searchsorted(scores, new)
    scores = np.insert(scores, pos, new)
    print(f"inserted {new} at {pos}: {scores}")
low = np.flatnonzero(scores < 60)
scores = np.delete(scores, low)
print("dropped failing scores:", scores)
print(repr(scores))
