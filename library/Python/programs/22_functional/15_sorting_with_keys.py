"""Sorting with key functions, cmp_to_key, multi-level and stable sorts."""
import re
from functools import cmp_to_key
from operator import itemgetter

students = [
    {"name": "Zoe", "grade": 88, "year": 2},
    {"name": "adam", "grade": 92, "year": 3},
    {"name": "Liam", "grade": 88, "year": 1},
    {"name": "mia", "grade": 75, "year": 2},
    {"name": "Noah", "grade": 92, "year": 1},
]

print("by name (case-insensitive):", [s["name"] for s in sorted(students, key=lambda s: s["name"].lower())])
print("by grade desc, name:", [(s["grade"], s["name"]) for s in
                              sorted(students, key=lambda s: (-s["grade"], s["name"].lower()))])

stable = sorted(sorted(students, key=itemgetter("name")), key=itemgetter("year"))
print("stable two-pass (year, then name):", [(s["year"], s["name"]) for s in stable])

print("max grade:", max(students, key=itemgetter("grade"))["name"],
      "| min year:", min(students, key=lambda s: (s["year"], s["name"]))["name"])


def version_cmp(a, b):
    pa = [int(x) for x in a.split(".")]
    pb = [int(x) for x in b.split(".")]
    return (pa > pb) - (pa < pb)


versions = ["1.10.0", "1.2.9", "1.2.10", "0.9", "1.2", "2.0.0", "1.10"]
print("string sort :", sorted(versions))
print("version sort:", sorted(versions, key=cmp_to_key(version_cmp)))


def largest_number(nums):
    as_str = sorted(map(str, nums), key=cmp_to_key(lambda a, b: (b + a > a + b) - (b + a < a + b)))
    return "".join(as_str).lstrip("0") or "0"


print("largest concatenation:", largest_number([3, 30, 34, 5, 9]))

files = ["img12.png", "img10.png", "IMG2.png", "img1.png", "readme", "img2.jpg"]


def natural_key(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]


print("natural sort:", sorted(files, key=natural_key))
print("by extension then name:", sorted(files, key=lambda f: (f.rpartition(".")[2], f.lower())))
print("reverse=True keeps stability:", sorted([(1, "b"), (2, "a"), (1, "a")], key=itemgetter(0), reverse=True))
