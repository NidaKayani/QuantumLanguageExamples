"""Heap sort implemented by hand and with the heapq module."""

import heapq


def sift_down(a, start, end):
    root = start
    while (child := 2 * root + 1) <= end:
        if child + 1 <= end and a[child] < a[child + 1]:
            child += 1
        if a[root] < a[child]:
            a[root], a[child] = a[child], a[root]
            root = child
        else:
            return


def heap_sort(a):
    n = len(a)
    for start in range(n // 2 - 1, -1, -1):
        sift_down(a, start, n - 1)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift_down(a, 0, end - 1)


def heapq_sort(iterable):
    h = list(iterable)
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]


def show_heap(a):
    level, i, lines = 0, 0, []
    while i < len(a):
        width = 2 ** level
        lines.append("  " * (3 - level) + " ".join(str(x) for x in a[i:i + width]))
        i += width
        level += 1
    return "\n".join(lines)


data = [12, 11, 13, 5, 6, 7, 21, 3, 9]
heap = data[:]
for start in range(len(heap) // 2 - 1, -1, -1):
    sift_down(heap, start, len(heap) - 1)
print("max-heap array:", heap)
print(show_heap(heap))

sorted_data = data[:]
heap_sort(sorted_data)
print("heap sort:", sorted_data)
print("heapq sort:", heapq_sort(data))
print("3 smallest:", heapq.nsmallest(3, data), "3 largest:", heapq.nlargest(3, data))

words = ["delta", "alpha", "echo", "bravo", "charlie"]
heap_sort(words)
print("words:", words)
print("longest two:", heapq.nlargest(2, words, key=len))
