"""Query numeric limits of integer and float types with np.iinfo and np.finfo."""
import numpy as np

print("Integer limits:")
for t in [np.int8, np.int16, np.int32, np.int64, np.uint8]:
    info = np.iinfo(t)
    print(f"  {info.dtype}: min={info.min} max={info.max} bits={info.bits}")

i8 = np.iinfo(np.int8)
print(i8)

print("Float limits:")
for t in [np.float32, np.float64]:
    fi = np.finfo(t)
    print(f"  {fi.dtype}: bits={fi.bits} eps={fi.eps} max={fi.max}")
    print(f"    tiny={fi.tiny} resolution={fi.resolution} precision={fi.precision}")

f64 = np.finfo(np.float64)
print("1 + eps > 1:", 1.0 + f64.eps > 1.0)
print("1 + eps/2 == 1:", 1.0 + f64.eps / 2 == 1.0)


def fits(values, dtype):
    """Check whether all integer values fit inside the given integer dtype."""
    info = np.iinfo(dtype)
    arr = np.asarray(values)
    return bool((arr >= info.min).all() and (arr <= info.max).all())


samples = np.array([0, 100, 250, 40000, -5])
for dt in [np.uint8, np.int16, np.int32]:
    print(f"fits {np.dtype(dt).name}:", fits(samples, dt))


def smallest_int_type(values):
    for dt in [np.int8, np.int16, np.int32, np.int64]:
        if fits(values, dt):
            return np.dtype(dt)
    return None


for vals in [[1, 2, 3], [-200, 5], [70000], [2 ** 40]]:
    print(vals, "->", smallest_int_type(vals))

# Detect approximate equality with machine epsilon
a = np.array([0.1 + 0.2, 1.0 / 3.0])
b = np.array([0.3, 0.333333333333333])
print("Exact equal:", a == b)
print("Within 10 eps:", np.abs(a - b) <= 10 * f64.eps * np.abs(b))
print("isclose:", np.isclose(a, b))
print("iinfo for array dtype:", np.iinfo(np.arange(3).dtype).max)
