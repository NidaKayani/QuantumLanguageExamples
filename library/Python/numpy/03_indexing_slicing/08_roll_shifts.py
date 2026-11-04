"""Circular shifts with np.roll in 1-D and 2-D, plus finite differences."""
import numpy as np

ring = np.arange(8)
print("ring:", ring)
print("roll +2:", np.roll(ring, 2))
print("roll -3:", np.roll(ring, -3))
print("roll by length is identity:", np.array_equal(np.roll(ring, 8), ring))

# Periodic finite difference and Laplacian
x = np.array([0.0, 1.0, 4.0, 9.0, 16.0, 25.0, 36.0, 49.0])
forward = np.roll(x, -1) - x
laplace = np.roll(x, -1) - 2 * x + np.roll(x, 1)
print("forward diff (periodic):", forward)
print("laplacian (periodic):")
print(repr(laplace))

# 2-D roll
g = np.arange(12).reshape(3, 4)
print("grid:")
print(g)
print("roll 1 along axis 0:")
print(np.roll(g, 1, axis=0))
print("roll -1 along axis 1:")
print(np.roll(g, -1, axis=1))
print("roll (1, 2) along axes (0, 1):")
print(np.roll(g, (1, 2), axis=(0, 1)))
print("roll without axis flattens first:")
print(np.roll(g, 5))

# Game-of-life neighbour count on a torus
life = np.zeros((6, 6), dtype=np.int64)
life[1, 2] = life[2, 3] = life[3, 1] = life[3, 2] = life[3, 3] = 1  # glider
neighbours = sum(np.roll(np.roll(life, dr, axis=0), dc, axis=1)
                 for dr in (-1, 0, 1) for dc in (-1, 0, 1)
                 if (dr, dc) != (0, 0))
print("glider:")
print(life)
print("neighbour counts:")
print(neighbours)
nxt = ((neighbours == 3) | ((life == 1) & (neighbours == 2))).astype(np.int64)
print("next generation:")
print(nxt)

# Rotating a schedule: who is on duty each day
staff = np.array([101, 102, 103, 104])
for day in range(4):
    print("day", day, "order:", np.roll(staff, -day))

# Smoothing with a 3-point circular average
signal = np.array([1.0, 5.0, 2.0, 8.0, 3.0, 7.0])
smooth = (np.roll(signal, 1) + signal + np.roll(signal, -1)) / 3
print("smoothed:", np.round(smooth, 3))
