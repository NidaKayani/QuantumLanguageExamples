"""Merge sort (top-down and bottom-up) plus inversion counting."""

from heapq import merge as heap_merge


def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def merge_sort_bottom_up(arr):
    runs = [[x] for x in arr]
    while len(runs) > 1:
        runs = [merge(runs[i], runs[i + 1]) if i + 1 < len(runs) else runs[i]
                for i in range(0, len(runs), 2)]
    return runs[0] if runs else []


def count_inversions(arr):
    if len(arr) <= 1:
        return arr[:], 0
    mid = len(arr) // 2
    left, a = count_inversions(arr[:mid])
    right, b = count_inversions(arr[mid:])
    merged, i, j, inv = [], 0, 0, a + b
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
            inv += len(left) - i
    return merged + left[i:] + right[j:], inv


data = [38, 27, 43, 3, 9, 82, 10, 3]
print("top-down: ", merge_sort(data))
print("bottom-up:", merge_sort_bottom_up(data))
print("inversions in", data, "=", count_inversions(data)[1])
print("inversions in reversed 1..10 =", count_inversions(list(range(10, 0, -1)))[1])

streams = [[1, 4, 9], [2, 3, 10, 11], [0, 5]]
print("heapq.merge of sorted streams:", list(heap_merge(*streams)))
print("merge desc with key:", list(heap_merge(["pear", "fig"], ["banana", "kiwi"], key=len, reverse=True)))
