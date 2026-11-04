"""A simplified Timsort: natural runs, minimum run length and merging."""

MIN_RUN = 8


def insertion_sort(a, lo, hi):
    for i in range(lo + 1, hi):
        x = a[i]
        j = i - 1
        while j >= lo and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x


def find_runs(a):
    runs, i, n = [], 0, len(a)
    while i < n:
        j = i + 1
        if j < n and a[j] < a[i]:
            while j < n and a[j] < a[j - 1]:
                j += 1
            a[i:j] = reversed(a[i:j])
        else:
            while j < n and a[j] >= a[j - 1]:
                j += 1
        end = min(max(j, i + MIN_RUN), n)
        insertion_sort(a, i, end)
        runs.append((i, end))
        i = end
    return runs


def merge(a, lo, mid, hi):
    left, right = a[lo:mid], a[mid:hi]
    i = j = 0
    k = lo
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]; i += 1
        else:
            a[k] = right[j]; j += 1
        k += 1
    a[k:hi] = left[i:] + right[j:]


def timsort(a):
    runs = find_runs(a)
    print(f"  natural runs ({len(runs)}): {runs}")
    while len(runs) > 1:
        merged = []
        for idx in range(0, len(runs) - 1, 2):
            (lo, mid), (_, hi) = runs[idx], runs[idx + 1]
            merge(a, lo, mid, hi)
            merged.append((lo, hi))
        if len(runs) % 2:
            merged.append(runs[-1])
        runs = merged
    return a


seed = 7
def rand():
    global seed
    seed = (seed * 48271) % 2147483647
    return seed % 100

inputs = {
    "ascending+noise": list(range(20)) + [rand() for _ in range(6)],
    "descending runs": list(range(15, 0, -1)) + list(range(30, 20, -1)),
    "random": [rand() for _ in range(30)],
}
for name, data in inputs.items():
    print(name)
    expected = sorted(data)
    result = timsort(data)
    print("  ok:", result == expected, result[:10], "...")
