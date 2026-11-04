"""Generate number sequences with np.arange using integer and float steps."""
import numpy as np

a = np.arange(10)
print("arange(10):", a)
print(repr(a))

b = np.arange(2, 12)
print("arange(2, 12):", b)

evens = np.arange(0, 20, 2)
print("Evens:", evens)

countdown = np.arange(10, 0, -1)
print("Countdown:", countdown)

steps = np.arange(0.0, 1.0, 0.25)
print("Float step 0.25:", steps)
print(repr(steps))

half = np.arange(1, 4, 0.5)
print("arange(1, 4, 0.5):", half)

neg = np.arange(-1.5, 1.6, 0.5)
print("Symmetric float range:", neg)

# Reshape an arange into a table
table = np.arange(1, 13).reshape(3, 4)
print("1..12 as 3x4:")
print(table)
print(repr(table))

# Multiplication table using arange and broadcasting
n = np.arange(1, 6)
mult = n[:, None] * n
print("Multiplication table:")
print(mult)

# Squares and cumulative sum
sq = np.arange(1, 8) ** 2
print("Squares:", sq)
print("Cumulative sum:", np.cumsum(sq))

empty = np.arange(5, 5)
print("Empty range:", repr(empty), "size", empty.size)

fl = np.arange(5, dtype=float)
print("arange with dtype=float:", repr(fl))
print("Length of arange(0, 1, 0.1):", len(np.arange(0, 1, 0.1)))
