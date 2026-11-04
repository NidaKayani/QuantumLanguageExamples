"""Binary search on the answer: peaks, first bad version, shipping capacity."""


def find_peak(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo


def first_bad_version(n, is_bad):
    lo, hi, calls = 1, n, 0
    while lo < hi:
        mid = (lo + hi) // 2
        calls += 1
        if is_bad(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo, calls


def days_needed(weights, capacity):
    days, load = 1, 0
    for w in weights:
        if load + w > capacity:
            days += 1
            load = 0
        load += w
    return days


def min_capacity(weights, days):
    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if days_needed(weights, mid) <= days:
            hi = mid
        else:
            lo = mid + 1
    return lo


def min_eating_speed(piles, hours):
    lo, hi = 1, max(piles)
    while lo < hi:
        k = (lo + hi) // 2
        if sum(-(-p // k) for p in piles) <= hours:
            hi = k
        else:
            lo = k + 1
    return lo


for arr in ([1, 2, 3, 1], [1, 2, 1, 3, 5, 6, 4], [5, 4, 3], [1, 9]):
    i = find_peak(arr)
    print(f"peak in {arr}: index {i} (value {arr[i]})")

version, calls = first_bad_version(1_000_000, lambda v: v >= 765_432)
print(f"first bad version: {version} after {calls} checks")

packages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for d in (1, 3, 5, 10):
    print(f"ship within {d:>2} days: capacity {min_capacity(packages, d)}")
print("koko eating speed:", min_eating_speed([3, 6, 7, 11], 8), min_eating_speed([30, 11, 23, 4, 20], 6))
