"""Square roots, exponentials and logarithms in several bases."""
import numpy as np

x = np.array([1.0, 2.0, 4.0, 10.0, 16.0, 100.0, 1024.0])
print("x       =", x)
print("sqrt    =", np.sqrt(x))
print("exp(1..4)", np.exp(np.arange(1, 5)))
print("log     =", np.log(x))
print("log2    =", np.log2(x))
print("log10   =", np.log10(x))
print(repr(np.log2(x)))

# exp and log are inverses
print("exp(log(x)) ~ x:", np.allclose(np.exp(np.log(x)), x))
print("change of base log_3(81):", np.log(81.0) / np.log(3.0))

# exponential decay of a radioactive sample
half_life = 5.0
t = np.arange(0, 31, 5)
remaining = 100.0 * np.exp(-np.log(2) / half_life * t)
print("t:", t)
print("remaining %:", np.round(remaining, 3))

# compound growth vs continuous growth
years = np.array([1, 5, 10, 20])
rate = 0.05
discrete = (1 + rate) ** years
continuous = np.exp(rate * years)
print("discrete:  ", discrete)
print("continuous:", continuous)
print("ratio:     ", continuous / discrete)

# number of bits needed to represent integers
n = np.array([1, 7, 8, 255, 256, 1000, 65535])
bits = np.floor(np.log2(n)).astype(np.int64) + 1
print("n:", n)
print("bits:", bits)
digits = np.floor(np.log10(n)).astype(np.int64) + 1
print("decimal digits:", digits)

# geometric mean via logs
data = np.array([2.0, 8.0, 4.0, 16.0, 1.0])
print("geometric mean:", np.exp(np.log(data).mean()))
print("arithmetic mean:", data.mean())

# sqrt on a 2-D grid and log1p/expm1 for small values
grid = np.arange(1, 13, dtype=np.float64).reshape(3, 4)
print("sqrt(grid):")
print(np.sqrt(grid))
small = np.array([1e-10, 1e-5, 1e-2])
print("log1p:", np.log1p(small))
print("expm1:", np.expm1(small))
print("cbrt([8, 27, -64]):", np.cbrt(np.array([8.0, 27.0, -64.0])))
