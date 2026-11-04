"""Lambdas as sort keys, with map/filter/reduce and operator helpers."""
from functools import reduce
from operator import itemgetter, attrgetter
from collections import namedtuple

Employee = namedtuple("Employee", "name dept salary")
staff = [
    Employee("Ava", "eng", 120),
    Employee("Ben", "ops", 85),
    Employee("Cy", "eng", 105),
    Employee("Di", "sales", 95),
    Employee("Ed", "ops", 90),
]

by_salary = sorted(staff, key=lambda e: e.salary, reverse=True)
print("by salary:", [e.name for e in by_salary])

by_dept = sorted(staff, key=lambda e: (e.dept, -e.salary))
print("by dept, salary desc:", [(e.dept, e.name) for e in by_dept])

print("attrgetter:", [e.name for e in sorted(staff, key=attrgetter("name"))])

words = ["banana", "Apple", "cherry", "date", "Elderberry", "fig"]
print("case-insensitive:", sorted(words, key=str.lower))
print("by length then alpha:", sorted(words, key=lambda w: (len(w), w.lower())))

squares = list(map(lambda x: x * x, range(1, 8)))
evens = list(filter(lambda x: x % 2 == 0, squares))
product = reduce(lambda a, b: a * b, range(1, 7), 1)
print("squares:", squares)
print("even squares:", evens)
print("6! via reduce:", product)

pairs = [(3, "c"), (1, "a"), (2, "b")]
print("itemgetter(1):", sorted(pairs, key=itemgetter(1)))

ops = {"+": lambda a, b: a + b, "-": lambda a, b: a - b,
       "*": lambda a, b: a * b, "/": lambda a, b: a / b}
for sym, fn in ops.items():
    print(f"12 {sym} 4 = {fn(12, 4)}")
