"""Searching rotated sorted arrays with modified binary search."""


def find_rotation(arr):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] > arr[hi]:
            lo = mid + 1
        else:
            hi = mid
    return lo


def search_rotated(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[lo] <= arr[mid]:
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def rotate(seq, k):
    k %= len(seq)
    return seq[k:] + seq[:k]


base = [3, 8, 12, 17, 21, 25, 30, 41, 56]
for k in [0, 3, 5, 8]:
    arr = rotate(base, k)
    pivot = find_rotation(arr)
    print(f"rotated by {k}: {arr}")
    print(f"   minimum {arr[pivot]} at index {pivot}; rotation count = {pivot}")
    results = {t: search_rotated(arr, t) for t in (3, 25, 56, 10)}
    print("   search:", results)

times = ["14:00", "18:30", "22:15", "02:00", "06:45", "10:20"]
print("shift log (rotated by midnight):", times)
print("earliest entry is", times[find_rotation(times)])
print("index of '06:45':", search_rotated(times, "06:45"))
