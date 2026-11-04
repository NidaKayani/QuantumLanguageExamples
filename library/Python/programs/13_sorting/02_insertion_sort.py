"""Insertion sort: classic, binary-search insertion and key-based variants."""

from bisect import insort


def insertion_sort(arr: list) -> int:
    shifts = 0
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
            shifts += 1
        arr[j + 1] = current
    return shifts


def binary_insertion_sort(items):
    result = []
    for x in items:
        insort(result, x)
    return result


def insertion_sort_by(items, key):
    out = []
    for item in items:
        k = key(item)
        pos = len(out)
        while pos > 0 and key(out[pos - 1]) > k:
            pos -= 1
        out.insert(pos, item)
    return out


data = [29, 10, 14, 37, 13, 5, 88, 1]
copy = data[:]
shifts = insertion_sort(copy)
print("insertion:", copy, "shifts:", shifts)

nearly = [1, 2, 4, 3, 5, 6, 8, 7, 9]
print("nearly sorted needs only", insertion_sort(nearly[:]), "shifts")

print("binary insertion:", binary_insertion_sort([5.5, -1, 3, 3, 0.25, 9]))

people = [("zoe", 31), ("adam", 25), ("mia", 31), ("li", 19), ("bob", 25)]
by_age = insertion_sort_by(people, key=lambda p: p[1])
print("by age (stable):", by_age)

words = "banana Apple cherry apple Banana".split()
print("case-insensitive:", insertion_sort_by(words, key=str.lower))

letters = list("insertionsort")
insertion_sort(letters)
print("letters:", "".join(letters))
