"""Order statistics: median, percentile and quantile with linear interpolation."""
import numpy as np

# response times in milliseconds
latency = np.array([120.0, 95.0, 310.0, 101.0, 87.0, 140.0, 99.0, 450.0, 115.0, 108.0, 92.0])
print("latency:", latency)
print("sorted:", np.sort(latency))

print("median:", np.median(latency))
print("mean:", round(latency.mean(), 3), "(pulled up by outliers)")

print("p50:", np.percentile(latency, 50))
print("p90:", np.percentile(latency, 90))
print("p99:", np.percentile(latency, 99))
pcts = np.percentile(latency, [25, 50, 75])
print("quartiles:", pcts)
print(repr(pcts))

q = np.quantile(latency, [0.0, 0.1, 0.5, 0.9, 1.0])
print("quantiles:", q)
iqr = np.subtract(*np.percentile(latency, [75, 25]))
print("IQR:", iqr)

lo = pcts[0] - 1.5 * iqr
hi = pcts[2] + 1.5 * iqr
outliers = latency[(latency < lo) | (latency > hi)]
print("fences:", lo, hi)
print("outliers:", outliers)

# 2-D: per-server medians
grid = np.array([
    [3, 9, 1, 7],
    [8, 2, 6, 4],
    [5, 5, 10, 0],
])
print(grid)
print("median per column:", np.median(grid, axis=0))
print("median per row:", np.median(grid, axis=1))
print("median keepdims:")
print(np.median(grid, axis=1, keepdims=True))
print("30th percentile per row:", np.percentile(grid, 30, axis=1))
print("quantile 0.75 per column:", np.quantile(grid, 0.75, axis=0))

even = np.array([4, 1, 3, 2])
print("median of even-length:", np.median(even))
print(repr(np.quantile(even, [0.25, 0.5, 0.75])))
