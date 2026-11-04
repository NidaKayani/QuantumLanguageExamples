"""Bubble sort with early termination and operation counting."""


def bubble_sort(items):
    data = list(items)
    comparisons = swaps = passes = 0
    for end in range(len(data) - 1, 0, -1):
        swapped = False
        passes += 1
        for i in range(end):
            comparisons += 1
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return data, {"comparisons": comparisons, "swaps": swaps, "passes": passes}


def cocktail_sort(data):
    data = list(data)
    lo, hi = 0, len(data) - 1
    while lo < hi:
        for i in range(lo, hi):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        hi -= 1
        for i in range(hi, lo, -1):
            if data[i - 1] > data[i]:
                data[i - 1], data[i] = data[i], data[i - 1]
        lo += 1
    return data


cases = {
    "random": [64, 34, 25, 12, 22, 11, 90, 5],
    "sorted": [1, 2, 3, 4, 5, 6, 7, 8],
    "reversed": [8, 7, 6, 5, 4, 3, 2, 1],
    "duplicates": [3, 1, 3, 2, 1, 3, 2],
    "single": [42],
    "empty": [],
}

for name, values in cases.items():
    result, stats = bubble_sort(values)
    assert result == sorted(values)
    print(f"{name:<10} {values} -> {result}")
    print(f"{'':<10} {stats}")

print("cocktail:", cocktail_sort(["pear", "fig", "apple", "kiwi", "date"]))
