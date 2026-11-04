"""Explore NumPy type promotion when mixing int, float and bool arrays and scalars."""
import numpy as np

ints = np.array([1, 2, 3])
floats = np.array([0.5, 1.5, 2.5])
bools = np.array([True, False, True])

combos = [
    ("int + float", ints + floats),
    ("int + bool", ints + bools),
    ("float * bool", floats * bools),
    ("bool + bool", bools + bools),
    ("bool & bool", bools & bools),
    ("int / int", ints / ints),
    ("int // int", ints // 2),
    ("int ** 2", ints ** 2),
    ("int + 1.0", ints + 1.0),
    ("int * True", ints * True),
]
for label, res in combos:
    print(f"{label:>12}: {res} -> {res.dtype}")

print(repr(ints + floats))
print(repr(ints + bools))

print("result_type(int64, float64):", np.result_type(np.int64, np.float64))
print("result_type(int8, int16):", np.result_type(np.int8, np.int16))
print("result_type(uint8, int8):", np.result_type(np.uint8, np.int8))
print("result_type(int32, float32):", np.result_type(np.int32, np.float32))
print("result_type(bool, int8):", np.result_type(np.bool_, np.int8))
print("promote_types(int16, uint8):", np.promote_types(np.int16, np.uint8))

# Python scalars are "weak": they do not upcast small arrays
small = np.array([1, 2, 3], dtype=np.int8)
print("int8 + 5 ->", (small + 5).dtype)
print("int8 + 5.0 ->", (small + 5.0).dtype)
print("int8 + int64 array ->", (small + np.array([5])).dtype)

f32 = np.array([1.0, 2.0], dtype=np.float32)
print("float32 * 2.0 ->", (f32 * 2.0).dtype)
print("float32 + float64 array ->", (f32 + np.array([1.0])).dtype)

# Mean of an integer array is always float
scores = np.array([7, 8, 10, 9])
print("mean:", scores.mean(), type(scores.mean()).__name__)

# Comparisons always give bool
print("comparison dtype:", (ints > 1).dtype, ints > 1)

# In-place ops keep the left operand's dtype
acc = np.zeros(3, dtype=np.int64)
acc += np.array([1, 2, 3])
print("In-place int accumulator:", repr(acc))
facc = np.zeros(3)
facc += ints
print("In-place float accumulator:", repr(facc))
