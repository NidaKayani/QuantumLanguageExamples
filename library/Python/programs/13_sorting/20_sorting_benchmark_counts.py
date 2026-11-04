"""Counting comparisons across sort algorithms with an instrumented value class."""

from functools import total_ordering


@total_ordering
class Counted:
    comparisons = 0

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        Counted.comparisons += 1
        return self.value == other.value

    def __lt__(self, other):
        Counted.comparisons += 1
        return self.value < other.value

    def __repr__(self):
        return repr(self.value)


def insertion(a):
    for i in range(1, len(a)):
        x, j = a[i], i - 1
        while j >= 0 and x < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
    return a


def merge_sort(a):
    if len(a) < 2:
        return a
    m = len(a) // 2
    l, r = merge_sort(a[:m]), merge_sort(a[m:])
    out = []
    while l and r:
        out.append((r if r[0] < l[0] else l).pop(0))
    return out + l + r


def quick(a):
    if len(a) < 2:
        return a
    pivot, rest = a[0], a[1:]
    return quick([x for x in rest if x < pivot]) + [pivot] + quick([x for x in rest if not x < pivot])


def builtin(a):
    return sorted(a)


def make_data(n, seed=99):
    out = []
    for _ in range(n):
        seed = (seed * 1664525 + 1013904223) % 2 ** 32
        out.append(seed % 1000)
    return out


for label, data in [("random", make_data(300)), ("sorted", list(range(300))), ("reversed", list(range(300, 0, -1)))]:
    print(f"{label} input (n={len(data)}):")
    for fn in (insertion, merge_sort, quick, builtin):
        Counted.comparisons = 0
        result = fn([Counted(v) for v in data])
        assert [c.value for c in result] == sorted(data)
        print(f"  {fn.__name__:<11} {Counted.comparisons:>6} comparisons")
