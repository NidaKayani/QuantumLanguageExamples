"""Search and insert into sorted lists using bisect and binary search."""

import bisect


def binary_search(seq, target):
    lo, hi = 0, len(seq) - 1
    steps = 0
    while lo <= hi:
        steps += 1
        mid = (lo + hi) // 2
        if seq[mid] == target:
            return mid, steps
        if seq[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, steps


data = list(range(0, 200, 7))
for target in (0, 49, 50, 196, 300):
    idx, steps = binary_search(data, target)
    print(f"search {target:3}: index {idx:3} in {steps} steps")

scores = [55, 62, 70, 78, 85, 91]
print("bisect_left(70):", bisect.bisect_left(scores, 70))
print("bisect_right(70):", bisect.bisect_right(scores, 70))

bisect.insort(scores, 80)
bisect.insort(scores, 50)
print("after insort:", scores)


def letter_grade(score, cutoffs=(60, 70, 80, 90), grades="FDCBA"):
    return grades[bisect.bisect(cutoffs, score)]


print("grades:", [letter_grade(s) for s in (33, 60, 77, 89, 90, 100)])

# count values in a range with two bisects
readings = sorted([12, 45, 3, 67, 23, 45, 89, 34, 45, 56])
lo, hi = 30, 60
count = bisect.bisect_right(readings, hi) - bisect.bisect_left(readings, lo)
print(f"readings in [{lo}, {hi}]: {count}")

# key-based bisect on records
people = sorted([("amy", 31), ("bob", 25), ("cat", 40)], key=lambda p: p[1])
pos = bisect.bisect_left(people, 33, key=lambda p: p[1])
print("first person aged >= 33:", people[pos])
