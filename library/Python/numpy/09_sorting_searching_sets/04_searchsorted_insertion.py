"""Binary search with np.searchsorted: left/right sides, counting ranges and sorted insertion."""
import numpy as np

data = np.array([1, 3, 3, 3, 5, 8, 8, 13, 21, 34])
print("sorted data:", data)

queries = np.array([0, 3, 4, 8, 21, 40])
left = np.searchsorted(data, queries, side="left")
right = np.searchsorted(data, queries, side="right")
print("queries:", queries)
print("left: ", left)
print("right:", right)
print("occurrence counts:", right - left)
print(repr(left))

# Membership test via searchsorted
pos = np.clip(left, 0, data.size - 1)
found = data[pos] == queries
print("present:", found)

# Count values within closed range [lo, hi]
lo, hi = 3, 13
count = np.searchsorted(data, hi, side="right") - np.searchsorted(data, lo, side="left")
print(f"values in [{lo}, {hi}]:", count, data[(data >= lo) & (data <= hi)])

# Insert new values while keeping order
new_vals = np.array([4, 9, 2, 50])
spots = np.searchsorted(data, new_vals)
merged = np.insert(data, spots, new_vals)
print("insert positions:", spots)
print("merged:", merged)
print("merged sorted?", bool(np.all(np.diff(merged) >= 0)))

# Searching an unsorted array through a sorter
prices = np.array([19.99, 4.5, 12.0, 7.25, 30.0, 1.75])
sorter = np.argsort(prices)
budget = np.array([5.0, 12.0, 25.0])
k = np.searchsorted(prices, budget, side="right", sorter=sorter)
print("prices:", prices)
print("items affordable for each budget:", k)
for b, n in zip(budget, k):
    print(f"  budget {b:6.2f}: cheapest {n} items ->", prices[sorter[:n]])

# Grade boundaries: map scores to letter grades
cutoffs = np.array([60, 70, 80, 90])
letters = "FDCBA"
scores = np.array([55, 60, 69, 70, 85, 90, 100])
grade_idx = np.searchsorted(cutoffs, scores, side="right")
print("grade index:", grade_idx)
print("grades:", " ".join(letters[i] for i in grade_idx))

# Cumulative weights: pick bucket for target values
weights = np.array([0.1, 0.3, 0.4, 0.2])
cdf = np.cumsum(weights)
targets = np.array([0.05, 0.1, 0.35, 0.79, 0.99])
print("cdf:", cdf)
print("bucket:", np.searchsorted(cdf, targets, side="right"))
