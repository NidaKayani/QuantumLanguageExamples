"""Convert arrays between int64, float64 and bool with astype and observe the results."""
import numpy as np

readings = np.array([-2.7, -0.5, 0.0, 0.49, 1.5, 3.99])
print("Floats:", readings)
print(repr(readings))

as_int = readings.astype(np.int64)
print("astype(int64) truncates toward zero:", as_int)
print(repr(as_int))

rounded = np.round(readings).astype(int)
print("round then int:", rounded)

floored = np.floor(readings).astype(int)
print("floor then int:", floored)

as_bool = readings.astype(bool)
print("Floats -> bool (nonzero is True):", as_bool)
print(repr(as_bool))

ints = np.array([0, 1, 2, 0, -3])
print("Ints -> bool:", repr(ints.astype(bool)))
print("Ints -> float:", repr(ints.astype(np.float64)))

flags = np.array([True, False, True, True, False])
print("bool -> int:", repr(flags.astype(int)))
print("bool -> float:", repr(flags.astype(float)))
print("Count of True via sum:", flags.sum())

# astype always returns a new array by default
src = np.arange(4)
dst = src.astype(np.int64)
dst[0] = 99
print("Source unchanged after modifying astype copy:", src)
same = src.astype(np.int64, copy=False)
print("copy=False with same dtype returns same object:", same is src)

# Percentages stored as ints, converted for math
pct = np.array([25, 50, 75, 100])
fractions = pct.astype(float) / 100
print("Fractions:", fractions)
print("Integer division instead:", pct // 100)

# Round trip
back = (fractions * 100).astype(np.int64)
print("Round trip:", repr(back))
print("Equal to original:", np.array_equal(back, pct))

# String dtype argument works too
print(repr(np.array([1, 2, 3]).astype("float64")))
