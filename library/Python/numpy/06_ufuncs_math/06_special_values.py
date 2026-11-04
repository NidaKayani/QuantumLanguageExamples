"""Working with np.pi, np.e, np.inf and np.nan: detection, cleanup and safe division."""
import numpy as np

print("np.pi =", np.pi)
print("np.e  =", np.e)
print("np.inf =", np.inf, " -np.inf =", -np.inf)
print("np.nan =", np.nan)
print("nan == nan:", np.nan == np.nan)

data = np.array([1.5, np.nan, 3.0, np.inf, -2.0, -np.inf, np.nan, 0.0])
print("data:", data)
print(repr(data))
print("isnan:   ", np.isnan(data))
print("isinf:   ", np.isinf(data))
print("isfinite:", np.isfinite(data))
print("isposinf:", np.isposinf(data))
print("finite values:", data[np.isfinite(data)])
print("count nan:", np.isnan(data).sum())

# NaN propagates through ordinary reductions; nan-aware versions skip it
print("sum:", data[~np.isinf(data)].sum())
print("nansum (finite part):", np.nansum(data[~np.isinf(data)]))
print("nanmax of finite+nan:", np.nanmax(data[~np.isinf(data)]))
print("nanmean:", np.nanmean(np.array([1.0, np.nan, 5.0])))

# nan_to_num with defaults and custom replacements
print("nan_to_num default:", np.nan_to_num(np.array([np.nan, 1.0, -np.inf])))
cleaned = np.nan_to_num(data, nan=0.0, posinf=999.0, neginf=-999.0)
print("nan_to_num custom:", cleaned)

# division by zero produces inf/nan when warnings are silenced
num = np.array([1.0, -1.0, 0.0, 4.0])
den = np.array([0.0, 0.0, 0.0, 2.0])
with np.errstate(divide="ignore", invalid="ignore"):
    ratio = num / den
    logs = np.log(np.array([0.0, 1.0, np.e, -1.0]))
print("num / den:", ratio)
print("log([0, 1, e, -1]):", logs)

# safe division: replace non-finite results
safe = np.where(np.isfinite(ratio), ratio, 0.0)
print("safe ratio:", safe)
with np.errstate(divide="ignore", invalid="ignore"):
    alt = np.divide(num, den, out=np.zeros_like(num), where=den != 0)
print("divide with where:", alt)

# inf arithmetic
print("inf + 1:", np.inf + 1, " inf * -2:", np.inf * -2, " 1 / inf:", 1 / np.inf)
print("max with inf:", np.max(np.array([1.0, np.inf, 3.0])))
print("min of empty-safe init:", np.min(np.array([4.0, 2.0]), initial=np.inf))

# matrix with missing entries: fill with column means
M = np.array([[1.0, np.nan, 3.0], [4.0, 5.0, np.nan], [7.0, 8.0, 9.0]])
col_means = np.nanmean(M, axis=0)
filled = np.where(np.isnan(M), col_means, M)
print("column means ignoring nan:", col_means)
print("filled:")
print(filled)
