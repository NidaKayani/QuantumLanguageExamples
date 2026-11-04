"""Assigning through boolean masks and integer index arrays."""
import numpy as np

# Data cleaning: replace sentinel values
raw = np.array([4.2, -999.0, 3.8, 5.1, -999.0, 4.9, 6.3, -999.0])
print(repr(raw))
missing = raw == -999.0
valid_mean = raw[~missing].mean()
cleaned = raw.copy()
cleaned[missing] = valid_mean
print("missing count:", missing.sum())
print("cleaned:", cleaned.round(3))

# Scale values above a threshold in place
x = np.arange(10, dtype=np.float64)
x[x > 6] *= 10
print("scaled tail:", x)

# Assign an array of matching length to masked positions
y = np.zeros(8, dtype=np.int64)
mask = np.array([1, 0, 1, 1, 0, 0, 1, 0], dtype=bool)
y[mask] = [11, 22, 33, 44]
print("masked assignment of sequence:", y)

# 2-D: zero out negatives
m = np.array([[3, -1, 4], [-1, 5, -9], [2, -6, 5]])
m[m < 0] = 0
print("negatives zeroed:")
print(m)

# Fancy-index assignment
scores = np.zeros(6)
winners = [0, 3, 5]
scores[winners] = [9.5, 8.0, 7.25]
print("scores:", scores)

# Repeated indices: plain += applies only once, np.add.at accumulates
votes = np.zeros(4, dtype=np.int64)
ballots = np.array([0, 2, 2, 3, 2, 0])
votes[ballots] += 1
print("buffered += with repeats:", votes)
votes[:] = 0
np.add.at(votes, ballots, 1)
print("np.add.at with repeats:  ", votes)

# 2-D paired-index assignment: set a diagonal
grid = np.zeros((5, 5), dtype=np.int64)
i = np.arange(5)
grid[i, i] = 1
grid[i[:-1], i[1:]] = 2
grid[i[1:], i[:-1]] = 3
print("tridiagonal via fancy assignment:")
print(grid)

# Row-wise mask assignment
table = np.arange(12).reshape(3, 4)
bad_rows = table.sum(axis=1) > 20
table[bad_rows] = -1
print("rows with sum > 20 replaced:")
print(repr(table))

# Swap elements by fancy assignment
arr = np.array([10, 20, 30, 40, 50])
arr[[0, 4]] = arr[[4, 0]]
print("first/last swapped:", arr)

# np.putmask and np.place
p = np.arange(8)
np.putmask(p, p % 3 == 0, -p)
print("putmask negate multiples of 3:", p)
q = np.arange(8)
np.place(q, q > 4, [100, 200])
print("place cycles values:", q)
