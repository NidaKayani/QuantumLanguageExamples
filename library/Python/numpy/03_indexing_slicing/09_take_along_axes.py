"""Selecting elements with np.take, including axis, mode='wrap' and mode='clip'."""
import numpy as np

lookup = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
print(repr(lookup))

idx = [0, 2, 4, 2]
print("np.take(lookup, idx):", np.take(lookup, idx))
print("method form:", lookup.take(idx))

# 2-D index array gives a 2-D result
pairs = np.array([[0, 1], [3, 4]])
print("take with 2-D indices:")
print(np.take(lookup, pairs))

# Out-of-range handling
wild = np.array([-1, 3, 5, 7, 12])
print("mode='wrap':", np.take(lookup, wild, mode="wrap"))
print("mode='clip':", np.take(lookup, wild, mode="clip"))

# take along an axis of a 2-D table
table = np.arange(20).reshape(4, 5)
print("table:")
print(table)
print("rows 3 and 1:")
print(np.take(table, [3, 1], axis=0))
print("columns 4, 0, 2:")
print(np.take(table, [4, 0, 2], axis=1))
print("without axis (flattened) [0, 7, 19]:", np.take(table, [0, 7, 19]))

# Re-ordering records by a sort key
scores = np.array([72.5, 91.0, 66.0, 88.5, 79.0])
ids = np.array([501, 502, 503, 504, 505])
order = np.argsort(scores)[::-1]
print("ranking ids:", np.take(ids, order))
print("ranking scores:", np.take(scores, order))

# Per-row picks with take_along_axis
data = np.array([[4, 9, 1, 7],
                 [8, 2, 6, 3],
                 [5, 5, 0, 9]])
best = np.argmax(data, axis=1)
print("argmax per row:", best)
picked = np.take_along_axis(data, best[:, None], axis=1)
print("max per row via take_along_axis:")
print(picked)
sorted_rows = np.take_along_axis(data, np.argsort(data, axis=1), axis=1)
print("rows sorted:")
print(repr(sorted_rows))

# Circular buffer read using wrap mode
buf = np.arange(100, 108)
head = 6
print("last 5 items ending at head:", np.take(buf, np.arange(head - 4, head + 1), mode="wrap"))
print("next 4 items from head:", np.take(buf, np.arange(head, head + 4), mode="wrap"))
