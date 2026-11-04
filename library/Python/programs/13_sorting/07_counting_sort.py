"""Counting sort for bounded integers, including a stable record version."""

from collections import Counter
from itertools import accumulate


def counting_sort(nums):
    if not nums:
        return []
    lo, hi = min(nums), max(nums)
    counts = [0] * (hi - lo + 1)
    for n in nums:
        counts[n - lo] += 1
    result = []
    for offset, c in enumerate(counts):
        result.extend([offset + lo] * c)
    return result


def counting_sort_stable(records, key, max_key):
    counts = [0] * (max_key + 1)
    for r in records:
        counts[key(r)] += 1
    starts = [0] + list(accumulate(counts))[:-1]
    out = [None] * len(records)
    for r in records:
        k = key(r)
        out[starts[k]] = r
        starts[k] += 1
    return out


nums = [4, -2, 2, 8, 3, 3, 1, -2, 0, 8, 8]
print("input: ", nums)
print("sorted:", counting_sort(nums))

grades = "BACABDCFAABCB"
histogram = Counter(grades)
print("grade histogram:", dict(sorted(histogram.items())))
print("sorted grades:", "".join(ch * histogram[ch] for ch in sorted(histogram)))

students = [("ivy", 3), ("ann", 1), ("joe", 2), ("kim", 1), ("lee", 3), ("max", 0), ("ned", 2)]
by_year = counting_sort_stable(students, key=lambda s: s[1], max_key=3)
print("stable by year:")
for name, year in by_year:
    print(f"  year {year}: {name}")

ages = [31, 25, 31, 47, 25, 19, 62, 47, 31]
print("ages:", counting_sort(ages))
