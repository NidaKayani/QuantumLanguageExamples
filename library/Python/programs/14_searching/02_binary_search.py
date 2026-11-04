"""Binary search: iterative, recursive, and lower/upper bound forms."""


def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    steps = 0
    while lo <= hi:
        steps += 1
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid, steps
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, steps


def binary_search_rec(arr, target, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search_rec(arr, target, mid + 1, hi)
    return binary_search_rec(arr, target, lo, mid - 1)


def lower_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
for t in [2, 31, 71, 50, 1]:
    idx, steps = binary_search(primes, t)
    print(f"find {t:>2}: iterative={idx:>2} ({steps} steps) recursive={binary_search_rec(primes, t):>2}")

dups = [1, 2, 2, 2, 3, 5, 5, 8]
for t in [2, 5, 4, 9]:
    lo, hi = lower_bound(dups, t), upper_bound(dups, t)
    print(f"value {t}: lower={lo} upper={hi} count={hi - lo}")

big = list(range(0, 2_000_000, 2))
idx, steps = binary_search(big, 1_234_566)
print(f"in a million evens, found 1234566 at {idx} in {steps} steps")
