"""Summarize a numeric dataset with the statistics module."""

import statistics as st

data = [23, 29, 20, 32, 23, 21, 33, 25, 23, 27, 30, 41, 19, 24, 26]

print("n:", len(data))
print("mean:", st.mean(data))
print("fmean:", round(st.fmean(data), 4))
print("median:", st.median(data), "| low/high:", st.median_low([1, 2, 3, 4]), st.median_high([1, 2, 3, 4]))
print("mode:", st.mode(data), "| multimode:", st.multimode([1, 1, 2, 2, 3]))
print("pstdev:", round(st.pstdev(data), 4), "| stdev:", round(st.stdev(data), 4))
print("variance:", round(st.variance(data), 4))
print("quartiles:", st.quantiles(data, n=4))
print("deciles:", [round(q, 1) for q in st.quantiles(data, n=10)])
print("geometric mean:", round(st.geometric_mean([1, 2, 4, 8]), 6))
print("harmonic mean:", st.harmonic_mean([40, 60]))

mean = st.mean(data)
sd = st.stdev(data)
outliers = [x for x in data if abs(x - mean) / sd > 2]
print("outliers (z > 2):", outliers)

hours = [1, 2, 3, 4, 5, 6]
scores = [52, 55, 61, 64, 70, 74]
print("correlation:", round(st.correlation(hours, scores), 4))
slope, intercept = st.linear_regression(hours, scores)
print(f"regression: score = {slope:.3f} * hours + {intercept:.3f}")
print("predicted for 8 hours:", round(slope * 8 + intercept, 2))

dist = st.NormalDist(mu=100, sigma=15)
print("P(IQ < 130):", round(dist.cdf(130), 4))
print("90th percentile:", round(dist.inv_cdf(0.9), 2))

bins = {}
for x in data:
    lo = x // 5 * 5
    bins[lo] = bins.get(lo, 0) + 1
for lo in sorted(bins):
    print(f"  {lo:>2}-{lo + 4:<2} {'*' * bins[lo]}")
