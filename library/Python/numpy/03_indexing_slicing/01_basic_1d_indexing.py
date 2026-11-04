"""Basic 1-D indexing: positive/negative indices, slices with steps and reversal."""
import numpy as np

temps = np.array([12.5, 14.0, 15.25, 13.75, 18.0, 21.5, 19.0, 16.5, 11.0, 9.75])
print("temps:", temps)
print(repr(temps))

# Single-element access
print("first:", temps[0])
print("last:", temps[-1])
print("third from end:", temps[-3])

# Slices
print("first three:", temps[:3])
print("last four:", temps[-4:])
print("middle:", temps[3:7])
print("every other:", temps[::2])
print("odd positions:", temps[1::2])
print("reversed:", temps[::-1])
print("reversed every third:", temps[::-3])
print("from 8 down to 2:", temps[8:1:-2])

# Out-of-range slices are clipped, not errors
print("clipped slice:", temps[5:100])
print("empty slice:", repr(temps[7:3]))

# Integer arrays
counts = np.arange(10, 101, 10)
print(repr(counts))
print("counts[2:5]:", counts[2:5])
print("sum of tail:", counts[-3:].sum())
print("diffs via slicing:", counts[1:] - counts[:-1])

# Moving average of window 3 using shifted slices
window = (temps[:-2] + temps[1:-1] + temps[2:]) / 3
print("3-day moving average:")
print(window)

# Find max and its position, then slice around it
peak = int(np.argmax(temps))
print("peak index:", peak, "value:", temps[peak])
print("neighbourhood of peak:", temps[max(peak - 2, 0):peak + 3])

# Using slice objects explicitly
s = slice(1, 9, 3)
print("slice object", s, "->", temps[s])
print("indices covered:", list(range(*s.indices(len(temps)))))

# Indexing returns NumPy scalars
x = temps[4]
print(type(x).__name__, x, x * 2)
print("as python float:", float(x))
