"""Create arrays matching another array's shape and dtype with zeros_like, ones_like, full_like."""
import numpy as np

prices = np.array([[10.5, 12.0, 9.75], [11.25, 13.5, 8.0]])
print("Prices:")
print(prices)

z = np.zeros_like(prices)
print("zeros_like:")
print(z)
print(repr(z))

counts = np.array([[3, 0, 2], [1, 4, 5]])
o = np.ones_like(counts)
print("ones_like (int):")
print(repr(o))

f = np.full_like(counts, 9)
print("full_like with 9:")
print(f)

# full_like keeps the int dtype, so 2.7 is truncated
trunc = np.full_like(counts, 2.7)
print("full_like int with 2.7:", repr(trunc))

ff = np.full_like(counts, 2.7, dtype=float)
print("full_like with dtype=float:")
print(ff)

flags = np.zeros_like(counts, dtype=bool)
flags[counts > 2] = True
print("Flags where count > 2:")
print(flags)

# Running maximum, starting from an array shaped like the data
data = np.array([3, 1, 4, 1, 5, 9, 2, 6])
running = np.zeros_like(data)
best = data[0]
for i, v in enumerate(data):
    best = max(best, v)
    running[i] = best
print("Data:   ", data)
print("Running:", running)
print("Matches maximum.accumulate:", np.array_equal(running, np.maximum.accumulate(data)))

out = np.ones_like(prices) * prices.mean()
print("Mean-filled:")
print(out)
