"""Copies vs views: np.copy, .copy(), and how to avoid accidental aliasing."""
import numpy as np

prices = np.array([100.0, 102.5, 101.0, 105.0, 107.5, 106.0])
print(repr(prices))

view = prices[1:4]
snapshot = prices[1:4].copy()
independent = np.copy(prices)

prices[2] = 0.0
print("after prices[2] = 0.0")
print("  prices:     ", prices)
print("  view:       ", view)
print("  snapshot:   ", snapshot)
print("  independent:", independent)

print("view shares memory:", np.shares_memory(view, prices))
print("snapshot shares memory:", np.shares_memory(snapshot, prices))
print("snapshot.base is None:", snapshot.base is None)

# np.array(x) copies by default; np.asarray does not
a = np.array(prices)
b = np.asarray(prices)
prices[0] = -1.0
print("np.array copy first:", a[0], " np.asarray first:", b[0])

# A function that should not modify its input
def normalise(arr):
    out = np.copy(arr)
    out -= out.min()
    span = out.max()
    if span > 0:
        out /= span
    return out

raw = np.array([3.0, 7.0, 5.0, 11.0, 9.0])
scaled = normalise(raw)
print("raw (unchanged):", raw)
print("scaled:", scaled)

# The buggy version modifies the caller's data through a slice
def bad_clear_head(arr, n):
    head = arr[:n]
    head[:] = 0
    return head

values = np.arange(1, 8)
bad_clear_head(values, 3)
print("values after bad_clear_head:", values)

# Copy of a 2-D sub-block
m = np.arange(16).reshape(4, 4)
block = m[1:3, 1:3].copy()
block[:] = 100
print("m unchanged:")
print(m)
print("modified block copy:")
print(block)

# Copies are contiguous even when the source view is strided
stride_view = m[:, ::2]
c = stride_view.copy()
print("strided view contiguous:", stride_view.flags["C_CONTIGUOUS"])
print("copy contiguous:", c.flags["C_CONTIGUOUS"])
print(repr(c))
