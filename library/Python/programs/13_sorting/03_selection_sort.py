"""Selection sort and a min/max double selection variant."""


def selection_sort(arr):
    arr = list(arr)
    n = len(arr)
    trace = []
    for i in range(n - 1):
        min_idx = min(range(i, n), key=arr.__getitem__)
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        trace.append(arr[:])
    return arr, trace


def double_selection_sort(arr):
    arr = list(arr)
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mn = mx = lo
        for i in range(lo, hi + 1):
            if arr[i] < arr[mn]:
                mn = i
            if arr[i] > arr[mx]:
                mx = i
        arr[lo], arr[mn] = arr[mn], arr[lo]
        if mx == lo:
            mx = mn
        arr[hi], arr[mx] = arr[mx], arr[hi]
        lo += 1
        hi -= 1
    return arr


values = [64, 25, 12, 22, 11, 3]
result, trace = selection_sort(values)
for step, snapshot in enumerate(trace, 1):
    print(f"after pass {step}: {snapshot}")
print("result:", result)

for sample in ([5, 1, 4, 2, 8, 0, 2], [9, 8, 7, 6, 5], list("selection"), []):
    out = double_selection_sort(sample)
    assert out == sorted(sample)
    print("double selection:", sample, "->", out)

# Selection sort is not stable: show it with tagged records
cards = [(4, "a"), (2, "b"), (4, "c"), (1, "d")]
def selection_by_rank(cards):
    cards = list(cards)
    for i in range(len(cards)):
        m = min(range(i, len(cards)), key=lambda j: cards[j][0])
        cards[i], cards[m] = cards[m], cards[i]
    return cards
print("unstable selection:", selection_by_rank(cards))
print("stable sorted():   ", sorted(cards, key=lambda c: c[0]))
