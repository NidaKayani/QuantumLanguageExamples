"""Sort lists with key functions, reverse order, and multi-level keys."""

from operator import itemgetter, attrgetter
from dataclasses import dataclass

nums = [5, -2, 9, -7, 0, 3]
print("sorted:", sorted(nums))
print("by abs:", sorted(nums, key=abs))
print("descending:", sorted(nums, reverse=True))

words = ["banana", "Pie", "apple", "fig", "Cherry", "kiwi"]
print("default:", sorted(words))
print("case-insensitive:", sorted(words, key=str.lower))
print("by length, then alpha:", sorted(words, key=lambda w: (len(w), w.lower())))

students = [("alice", "B", 88), ("bob", "A", 95), ("carol", "B", 91), ("dave", "A", 72)]
print("by score:", sorted(students, key=itemgetter(2), reverse=True))
print("by grade then name:", sorted(students, key=itemgetter(1, 0)))
# grade ascending, score descending
print("grade asc, score desc:", sorted(students, key=lambda s: (s[1], -s[2])))


@dataclass
class Employee:
    name: str
    dept: str
    salary: int


staff = [Employee("Zed", "ops", 50), Employee("Amy", "dev", 70),
         Employee("Bo", "dev", 65), Employee("Cy", "ops", 80)]
for e in sorted(staff, key=attrgetter("dept", "name")):
    print(f"  {e.dept} {e.name:4} {e.salary}")

# stable sort: sort by secondary key first, then primary
records = sorted(staff, key=attrgetter("salary"), reverse=True)
records.sort(key=attrgetter("dept"))
print("stable multi-pass:", [e.name for e in records])

# in-place sort vs sorted
data = [3, 1, 2]
result = data.sort()
print("list.sort returns", result, "and data is", data)
print("min/max with key:", min(words, key=len), max(words, key=len))
