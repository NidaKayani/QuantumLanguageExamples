"""Comparison operators produce boolean arrays used for counting and filtering."""
import numpy as np

temps = np.array([18.5, 22.1, 25.7, 30.2, 27.9, 19.4, 15.0, 31.8, 24.0, 22.1])
print("temps:", temps)

hot = temps > 25
print("temps > 25:", hot)
print(repr(hot))
print("hot days:", hot.sum(), " fraction:", hot.mean())
print("hot values:", temps[hot])

print("temps == 22.1:", temps == 22.1)
print("temps != 22.1 count:", (temps != 22.1).sum())
print("temps <= 19.4:", temps <= 19.4)
print("temps >= 30:", np.nonzero(temps >= 30)[0])

# combining masks with & | ~
mild = (temps >= 20) & (temps < 26)
extreme = (temps < 16) | (temps > 31)
print("mild:   ", mild)
print("extreme:", extreme)
print("not mild:", ~mild)
print("mild values:", temps[mild])

# comparisons broadcast too
thresholds = np.array([20, 25, 30])
above = temps[None, :] > thresholds[:, None]
print("days above each threshold (rows=threshold):")
print(above.astype(np.int64))
print("counts per threshold:", above.sum(axis=1))

# any / all
print("any below 16?", np.any(temps < 16))
print("all above 10?", np.all(temps > 10))

# integer array comparisons and bool arithmetic
grades = np.array([[72, 88, 95], [55, 61, 49], [90, 91, 100]])
passed = grades >= 60
print("passed:")
print(passed)
print("passes per student:", passed.sum(axis=1))
print("students passing all:", passed.all(axis=1))

# booleans in arithmetic become 0/1
bonus = passed * 5
print("bonus points:")
print(bonus)

# np.where on a comparison
labels = np.where(temps > 25, 1, 0)
print("labels:", labels)
print("clipped:", np.where(temps > 28, 28.0, temps))

# element-wise comparison of two arrays
a = np.array([1, 5, 3, 8])
b = np.array([2, 5, 1, 9])
print("a < b:", a < b, " a == b:", a == b, " a > b:", a > b)
