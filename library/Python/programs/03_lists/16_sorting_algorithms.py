"""Implement insertion, selection, merge and quick sort on lists and compare results."""


def insertion_sort(items):
    a = list(items)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def selection_sort(items):
    a = list(items)
    for i in range(len(a)):
        smallest = min(range(i, len(a)), key=a.__getitem__)
        a[i], a[smallest] = a[smallest], a[i]
    return a


def merge_sort(items):
    if len(items) <= 1:
        return list(items)
    mid = len(items) // 2
    left, right = merge_sort(items[:mid]), merge_sort(items[mid:])
    merged = []
    while left and right:
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    return merged + left + right


def quick_sort(items):
    if len(items) <= 1:
        return list(items)
    pivot, *rest = items
    return (quick_sort([x for x in rest if x < pivot]) + [pivot]
            + quick_sort([x for x in rest if x >= pivot]))


def lcg(seed):
    while True:
        seed = (seed * 1103515245 + 12345) % 2 ** 31
        yield seed


gen = lcg(2024)
data = [next(gen) % 100 for _ in range(20)]
print("input:", data)
expected = sorted(data)
for fn in (insertion_sort, selection_sort, merge_sort, quick_sort):
    result = fn(data)
    print(f"{fn.__name__:15} ok={result == expected}  {result[:8]}...")
print("input unchanged:", data[:5])
print("strings:", quick_sort(["pear", "apple", "fig", "banana"]))
