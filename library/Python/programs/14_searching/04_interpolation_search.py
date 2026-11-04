"""Interpolation search versus binary search on uniformly distributed keys."""


def interpolation_search(arr, target):
    lo, hi, probes = 0, len(arr) - 1, 0
    while lo <= hi and arr[lo] <= target <= arr[hi]:
        probes += 1
        if arr[hi] == arr[lo]:
            return (lo if arr[lo] == target else -1), probes
        pos = lo + (target - arr[lo]) * (hi - lo) // (arr[hi] - arr[lo])
        if arr[pos] == target:
            return pos, probes
        if arr[pos] < target:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1, probes


def binary_search(arr, target):
    lo, hi, probes = 0, len(arr) - 1, 0
    while lo <= hi:
        probes += 1
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid, probes
        lo, hi = (mid + 1, hi) if arr[mid] < target else (lo, mid - 1)
    return -1, probes


uniform = list(range(0, 100_000, 7))
print(f"uniform array of {len(uniform)} multiples of 7")
print(f"{'target':>8} {'interp idx':>10} {'probes':>6} {'binary idx':>10} {'probes':>6}")
for target in [0, 7, 34_993, 70_000, 99_995, 50_001]:
    i1, p1 = interpolation_search(uniform, target)
    i2, p2 = binary_search(uniform, target)
    print(f"{target:>8} {i1:>10} {p1:>6} {i2:>10} {p2:>6}")

skewed = [2 ** k for k in range(40)]
print("\nexponential (skewed) array of", len(skewed), "powers of two")
for target in [2 ** 5, 2 ** 30, 2 ** 39]:
    i1, p1 = interpolation_search(skewed, target)
    i2, p2 = binary_search(skewed, target)
    print(f"2^{i1:<2}: interpolation probes={p1:>2}, binary probes={p2}")
