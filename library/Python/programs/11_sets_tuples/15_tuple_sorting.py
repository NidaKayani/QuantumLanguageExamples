"""Sorting tuples: natural lexicographic order and itemgetter keys."""

from operator import itemgetter

students = [
    ("emma", "math", 91),
    ("liam", "art", 85),
    ("olivia", "math", 85),
    ("noah", "art", 97),
    ("ava", "history", 85),
    ("liam", "math", 72),
]

print("natural order:")
for row in sorted(students):
    print("  ", row)

print("by score desc, then name:")
for row in sorted(students, key=lambda t: (-t[2], t[0])):
    print("  ", row)

print("by subject then score (itemgetter):")
for row in sorted(students, key=itemgetter(1, 2)):
    print("  ", row)

get_name = itemgetter(0)
print("names:", list(map(get_name, students)))

best_by_subject = {}
for name, subject, score in students:
    if score > best_by_subject.get(subject, ("", -1))[1]:
        best_by_subject[subject] = (name, score)
for subject, (name, score) in sorted(best_by_subject.items()):
    print(f"top in {subject}: {name} ({score})")

versions = ["1.10.0", "1.2.9", "1.2.10", "0.9.12", "1.10.1"]
as_tuples = sorted(versions, key=lambda v: tuple(map(int, v.split("."))))
print("version sort:", as_tuples)
print("string sort for contrast:", sorted(versions))
