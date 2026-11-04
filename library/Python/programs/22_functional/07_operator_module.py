"""The operator module: itemgetter, attrgetter, methodcaller and arithmetic functions."""
import operator
from collections import namedtuple
from functools import reduce
from itertools import starmap

Employee = namedtuple("Employee", "name dept salary age")
staff = [
    Employee("Ana", "eng", 120, 34),
    Employee("Bo", "ops", 85, 45),
    Employee("Cy", "eng", 110, 29),
    Employee("Di", "sales", 95, 38),
    Employee("Ed", "ops", 85, 31),
]

by_salary_then_name = sorted(staff, key=operator.attrgetter("salary", "name"))
print("By salary, name:", [e.name for e in by_salary_then_name])

get_name_dept = operator.attrgetter("name", "dept")
print("Name/dept pairs:", list(map(get_name_dept, staff)))

rows = [("apple", 3, 0.5), ("pear", 1, 0.75), ("plum", 6, 0.3)]
print("Sorted by qty:", sorted(rows, key=operator.itemgetter(1)))
print("Second column:", list(map(operator.itemgetter(1), rows)))
print("Name and price:", [operator.itemgetter(0, 2)(r) for r in rows])

print("Line totals:", list(starmap(lambda _, q, p: operator.mul(q, p), rows)))

upper = operator.methodcaller("upper")
padded = operator.methodcaller("center", 9, "*")
print([upper(r[0]) for r in rows], [padded(r[0]) for r in rows])

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv,
       "//": operator.floordiv, "%": operator.mod, "**": operator.pow}
for symbol, fn in ops.items():
    print(f"17 {symbol:>2} 5 = {fn(17, 5):.4g}")

print("Comparisons:", [f(3, 4) for f in (operator.lt, operator.le, operator.eq, operator.ne, operator.ge)])
print("neg/not/abs:", operator.neg(7), operator.not_(0), operator.abs(-2.5))
print("contains:", operator.contains("haystack", "st"), operator.countOf([1, 2, 1, 1], 1))
print("concat:", reduce(operator.concat, (["a"], ["b", "c"], ["d"])))

data = {"k": [10, 20, 30]}
operator.setitem(data, "j", 5)
operator.iadd(data["k"], [40])
print("setitem/iadd:", data, "indexOf 30 ->", operator.indexOf(data["k"], 30))
print("truth of values:", [operator.truth(v) for v in (0, 1, "", "x", [], None)])
