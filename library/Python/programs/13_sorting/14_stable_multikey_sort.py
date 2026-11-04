"""Stable multi-key sorting: chained passes versus tuple keys."""

from operator import itemgetter

employees = [
    {"name": "Ana", "dept": "Sales", "level": 2, "salary": 58000},
    {"name": "Ben", "dept": "Eng", "level": 3, "salary": 98000},
    {"name": "Cid", "dept": "Eng", "level": 2, "salary": 85000},
    {"name": "Dee", "dept": "Sales", "level": 3, "salary": 70000},
    {"name": "Eli", "dept": "Eng", "level": 3, "salary": 101000},
    {"name": "Fay", "dept": "Ops", "level": 1, "salary": 45000},
    {"name": "Gus", "dept": "Ops", "level": 2, "salary": 52000},
    {"name": "Hal", "dept": "Sales", "level": 2, "salary": 58000},
]


def show(rows, title):
    print(title)
    for r in rows:
        print(f"  {r['dept']:<6} L{r['level']} {r['salary']:>7} {r['name']}")


# Goal: dept ascending, level descending, salary descending, name ascending
chained = sorted(employees, key=itemgetter("name"))
chained.sort(key=itemgetter("salary"), reverse=True)
chained.sort(key=itemgetter("level"), reverse=True)
chained.sort(key=itemgetter("dept"))
show(chained, "chained stable sorts (least significant key first):")

tuple_key = sorted(employees, key=lambda r: (r["dept"], -r["level"], -r["salary"], r["name"]))
print("tuple key gives same order:", tuple_key == chained)

# Stability: equal keys keep original relative order
same_salary = [r["name"] for r in sorted(employees, key=itemgetter("salary")) if r["salary"] == 58000]
print("equal salaries keep input order:", same_salary)

by_dept_name = sorted(employees, key=itemgetter("dept", "name"))
show(by_dept_name[:4], "first four by (dept, name):")
