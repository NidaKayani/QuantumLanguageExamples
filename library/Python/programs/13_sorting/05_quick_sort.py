"""Quicksort variants: Lomuto, Hoare, and a functional three-way partition."""


def quicksort_lomuto(a, lo=0, hi=None):
    if hi is None:
        hi = len(a) - 1
    if lo < hi:
        pivot = a[hi]
        i = lo
        for j in range(lo, hi):
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        quicksort_lomuto(a, lo, i - 1)
        quicksort_lomuto(a, i + 1, hi)


def hoare_partition(a, lo, hi):
    pivot = a[(lo + hi) // 2]
    i, j = lo - 1, hi + 1
    while True:
        i += 1
        while a[i] < pivot:
            i += 1
        j -= 1
        while a[j] > pivot:
            j -= 1
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]


def quicksort_hoare(a, lo=0, hi=None):
    if hi is None:
        hi = len(a) - 1
    while lo < hi:
        p = hoare_partition(a, lo, hi)
        # recurse into smaller side, loop on larger side
        if p - lo < hi - p:
            quicksort_hoare(a, lo, p)
            lo = p + 1
        else:
            quicksort_hoare(a, p + 1, hi)
            hi = p


def quicksort3(xs):
    if len(xs) <= 1:
        return list(xs)
    pivot = xs[len(xs) // 2]
    less = [x for x in xs if x < pivot]
    equal = [x for x in xs if x == pivot]
    greater = [x for x in xs if x > pivot]
    return quicksort3(less) + equal + quicksort3(greater)


samples = [
    [10, 7, 8, 9, 1, 5],
    [3, 3, 3, 1, 1, 2, 2, 2],
    list(range(12, 0, -1)),
    [0.5, -2.25, 3.0, 0.0, -1.0],
]
for s in samples:
    a, b = s[:], s[:]
    quicksort_lomuto(a)
    quicksort_hoare(b)
    c = quicksort3(s)
    assert a == b == c == sorted(s)
    print(f"{str(s):<40} -> {c}")

print("strings:", quicksort3("the quick brown fox jumps".split()))
