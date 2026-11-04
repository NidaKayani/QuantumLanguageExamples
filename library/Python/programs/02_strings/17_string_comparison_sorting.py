"""Compare and sort strings lexicographically, case-insensitively and naturally."""

import re

names = ["banana", "Apple", "cherry", "apple", "Banana", "date", "Éclair"]

print("default sort:", ascii(sorted(names)))
print("case-insensitive:", ascii(sorted(names, key=str.casefold)))
print("by length then alpha:", ascii(sorted(names, key=lambda s: (len(s), s.lower()))))
print("reverse:", ascii(sorted(names, reverse=True)))

print("'apple' < 'banana':", "apple" < "banana")
print("'Zebra' < 'apple':", "Zebra" < "apple")
print("'abc' < 'abcd':", "abc" < "abcd")
print("ord('Z'), ord('a'):", ord("Z"), ord("a"))

files = ["file10.txt", "file2.txt", "file1.txt", "file20.txt", "file3.txt", "File11.txt"]


def natural_key(s):
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", s)]


print("plain:", sorted(files))
print("natural:", sorted(files, key=natural_key))

print("min/max:", min(names), ascii(max(names)), "| max by length:", max(names, key=len))

versions = ["1.10.0", "1.2.3", "1.2.10", "0.9", "1.2"]
print("versions:", sorted(versions, key=lambda v: tuple(map(int, v.split(".")))))


def common_prefix(strings):
    if not strings:
        return ""
    lo, hi = min(strings), max(strings)
    i = 0
    while i < len(lo) and lo[i] == hi[i]:
        i += 1
    return lo[:i]


print("common prefix:", common_prefix(["interstellar", "internet", "interval", "internal"]))
