"""Check which dtype conversions are safe using np.can_cast with different casting rules."""
import numpy as np

types = [np.bool_, np.uint8, np.int8, np.int16, np.int32, np.int64, np.float32, np.float64]
names = [np.dtype(t).name for t in types]

print("Safe-cast table (row -> column):")
print(" " * 8 + " ".join(f"{n[:7]:>7}" for n in names))
for src, sname in zip(types, names):
    row = ["   yes " if np.can_cast(src, dst) else "    -  " for dst in types]
    print(f"{sname[:7]:>7} " + " ".join(row))

matrix = np.array([[np.can_cast(s, d) for d in types] for s in types])
print("As a boolean array:")
print(matrix.astype(int))
print("Safe casts available from each type:", matrix.sum(axis=1))

print("int64 -> float64 safe:", np.can_cast(np.int64, np.float64))
print("float64 -> int64 safe:", np.can_cast(np.float64, np.int64))
print("float64 -> int64 same_kind:", np.can_cast(np.float64, np.int64, casting="same_kind"))
print("float64 -> float32 same_kind:", np.can_cast(np.float64, np.float32, casting="same_kind"))
print("float64 -> int64 unsafe:", np.can_cast(np.float64, np.int64, casting="unsafe"))
print("int32 -> int32 no:", np.can_cast(np.int32, np.int32, casting="no"))
print("int32 -> int64 equiv:", np.can_cast(np.int32, np.int64, casting="equiv"))


def safe_convert(arr, dtype):
    """Convert only when the cast is lossless by dtype rules."""
    if np.can_cast(arr.dtype, dtype):
        return arr.astype(dtype)
    print(f"  refusing {arr.dtype} -> {np.dtype(dtype)}")
    return arr


x = np.array([1, 2, 3], dtype=np.int16)
print("int16 -> float64:", repr(safe_convert(x, np.float64)))
print("int16 -> int8:", repr(safe_convert(x, np.int8)))
y = np.array([1.25, 2.5])
print("float64 -> int64:", repr(safe_convert(y, np.int64)))

# Using casting= in astype
try:
    y.astype(np.int64, casting="safe")
except TypeError as exc:
    print("astype(casting='safe') raised TypeError:", type(exc).__name__)
print("astype unsafe default:", repr(y.astype(np.int64)))
