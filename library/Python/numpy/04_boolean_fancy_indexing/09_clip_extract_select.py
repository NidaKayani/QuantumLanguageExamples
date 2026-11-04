"""Value-based selection with np.clip, np.extract, np.select and np.compress."""
import numpy as np

# Sensor values with spikes, clipped to a valid range
sensor = np.array([0.4, 1.7, -0.3, 0.9, 2.5, 0.0, 1.0, -1.2])
print(repr(sensor))
print("clip to [0, 1]:", np.clip(sensor, 0.0, 1.0))
print("method form:", sensor.clip(-0.5, 2.0))
print("upper bound only:", np.clip(sensor, None, 1.0))
print("lower bound only:", np.clip(sensor, 0.0, None))

# Per-element bounds with broadcasting
lo = np.array([0, 0, 0, 1, 1, 1, 2, 2])
hi = lo + 1
ints = np.arange(-2, 6)
print("ints:", ints)
print("clip per element:", np.clip(ints, lo, hi))

# In-place clip with out=
pixels = np.array([[-20, 130, 300], [255, 0, 512]])
np.clip(pixels, 0, 255, out=pixels)
print("pixels clipped in place:")
print(pixels)

# np.extract returns elements where condition holds (flattened)
grid = np.arange(16).reshape(4, 4)
cond = (grid % 4 == 0) | (grid % 4 == 3)
print("extract edge columns:", np.extract(cond, grid))
print("same as boolean indexing:", np.array_equal(np.extract(cond, grid), grid[cond]))

# np.compress with an axis
keep = np.array([True, False, True, True])
print("compress rows:")
print(np.compress(keep, grid, axis=0))
print("compress columns:")
print(np.compress([False, True, True], grid, axis=1))

# np.select: grade buckets
marks = np.array([92, 85, 71, 64, 58, 77, 100, 49])
conditions = [marks >= 90, marks >= 80, marks >= 70, marks >= 60]
choices = [4, 3, 2, 1]
grade_points = np.select(conditions, choices, default=0)
print("marks:", marks)
print("grade points:", grade_points)

# np.select with array-valued choices: piecewise tax
income = np.array([8000.0, 15000.0, 42000.0, 90000.0, 120000.0])
tax = np.select(
    [income <= 10000, income <= 50000, income > 50000],
    [np.zeros_like(income),
     (income - 10000) * 0.2,
     8000 + (income - 50000) * 0.4],
)
print("income:", income)
print("tax:", tax)
print(repr(tax))

# Clip + select combined: normalized score banding
z = np.clip((marks - marks.mean()) / marks.std(), -2, 2)
band = np.select([z < -1, z > 1], [-1, 1], default=0)
print("z-scores:", z.round(3))
print("bands:", band)
