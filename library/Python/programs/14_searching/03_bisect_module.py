"""The bisect module: insertion points, grading tables and sorted collections."""

import bisect

scores = [33, 99, 77, 70, 89, 90, 100, 59, 61]
breakpoints = [60, 70, 80, 90]
grades = "FDCBA"


def grade(score):
    return grades[bisect.bisect(breakpoints, score)]


print("grades:", [(s, grade(s)) for s in scores])

data = [10, 20, 20, 20, 30, 40]
print("bisect_left(20):", bisect.bisect_left(data, 20))
print("bisect_right(20):", bisect.bisect_right(data, 20))
print("bisect_left(25):", bisect.bisect_left(data, 25))

sorted_list = []
for x in [5, 1, 9, 3, 7, 3, 8]:
    bisect.insort(sorted_list, x)
    print(f"insert {x}: {sorted_list}")


def count_in_range(arr, lo, hi):
    return bisect.bisect_right(arr, hi) - bisect.bisect_left(arr, lo)


temps = sorted([12.5, 15.0, 9.8, 22.1, 18.4, 15.0, 30.2, 25.5, 11.1])
print("temps:", temps)
print("readings in [12, 20]:", count_in_range(temps, 12, 20))

events = [("09:00", "standup"), ("10:30", "design review"), ("13:00", "lunch"), ("15:45", "retro")]
times = [t for t, _ in events]
for query in ["08:00", "10:30", "14:00", "17:00"]:
    i = bisect.bisect_right(times, query)
    nxt = events[i][1] if i < len(events) else "nothing"
    print(f"at {query} the next event after is: {nxt}")

people = sorted([("ann", 31), ("bob", 25), ("cy", 42), ("di", 25)], key=lambda p: p[1])
i = bisect.bisect_left(people, 30, key=lambda p: p[1])
print("people aged 30+:", people[i:])
