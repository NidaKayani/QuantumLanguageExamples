"""Cartesian/polar conversion with np.hypot, np.arctan2, np.degrees and np.radians."""
import numpy as np

x = np.array([1.0, 0.0, -1.0, -1.0, 0.0, 1.0, 3.0, -2.0])
y = np.array([0.0, 1.0, 1.0, -1.0, -2.0, -1.0, 4.0, 0.0])

r = np.hypot(x, y)
theta = np.arctan2(y, x)
print("x:", x)
print("y:", y)
print("r:", r)
print("theta (rad):", theta)
print("theta (deg):", np.degrees(theta))
print(repr(np.round(np.degrees(theta), 2)))

# hypot is the same as sqrt(x^2 + y^2)
print("hypot matches sqrt:", np.allclose(r, np.sqrt(x ** 2 + y ** 2)))

# arctan2 vs arctan: quadrant awareness
naive = np.degrees(np.arctan(np.array([1.0, 1.0]) / np.array([1.0, -1.0])))
correct = np.degrees(np.arctan2(np.array([1.0, -1.0]), np.array([1.0, -1.0])))
print("arctan(y/x) for (1,1),(-1,-1):", naive)
print("arctan2 for (1,1),(-1,-1):   ", correct)

# back to Cartesian
x2 = r * np.cos(theta)
y2 = r * np.sin(theta)
print("round trip ok:", np.allclose(x2, x) and np.allclose(y2, y))

# compass bearings 0..360 measured clockwise from north
dx = np.array([0.0, 5.0, 0.0, -5.0, 3.0])
dy = np.array([5.0, 0.0, -5.0, 0.0, 3.0])
bearing = np.degrees(np.arctan2(dx, dy)) % 360
print("bearings:", bearing)

# points evenly spaced on a circle
k = np.arange(6)
phi = np.radians(60.0 * k)
pts = np.stack([2 * np.cos(phi), 2 * np.sin(phi)], axis=1)
print("hexagon vertices:")
print(np.round(pts, 4))
side = np.hypot(*(pts[1] - pts[0]))
print("side length: %.6f" % side)

# degrees <-> radians helpers
print("np.radians(180) =", np.radians(180.0), " np.pi =", np.pi)
print("np.deg2rad([90, 45]):", np.deg2rad(np.array([90.0, 45.0])))
print("np.rad2deg(pi/3):", np.rad2deg(np.pi / 3))

# pairwise distances via hypot broadcasting
px = np.array([0.0, 3.0, 6.0])
py = np.array([0.0, 4.0, 0.0])
D = np.hypot(px[:, None] - px, py[:, None] - py)
print("distance matrix:")
print(D)
