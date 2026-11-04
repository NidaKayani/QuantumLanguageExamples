"""collections.namedtuple: fields, defaults and helper methods."""

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Color = namedtuple("Color", "red green blue alpha", defaults=[255])

p = Point(3, 4)
print(p)
print("x:", p.x, "y:", p.y, "index access:", p[0], p[1])
print("distance from origin:", (p.x ** 2 + p.y ** 2) ** 0.5)

q = p._replace(y=10)
print("replaced:", q, "original unchanged:", p)

print("as dict:", p._asdict())
print("fields:", Point._fields)
print("made from list:", Point._make([7, 8]))

c = Color(10, 20, 30)
print(c, "| defaults:", Color._field_defaults)

x, y = p
print("unpacked:", x, y)
print("is a tuple:", isinstance(p, tuple), "| equal to plain tuple:", p == (3, 4))

points = [Point(5, 1), Point(-2, 3), Point(0, 0), Point(5, -1)]
print("sorted:", sorted(points))
print("max by y:", max(points, key=lambda pt: pt.y))

Employee = namedtuple("Employee", "name dept salary")
staff = [Employee("Ann", "eng", 120), Employee("Bo", "ops", 90), Employee("Cy", "eng", 110)]
eng_total = sum(e.salary for e in staff if e.dept == "eng")
print("engineering payroll:", eng_total)
