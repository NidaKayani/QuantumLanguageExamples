"""Build a 2D vector class with arithmetic dunder methods and math helpers."""

import math
from functools import total_ordering


@total_ordering
class Vector:
    __slots__ = ("x", "y")

    def __init__(self, x=0.0, y=0.0):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vector({self.x:g}, {self.y:g})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k)

    __rmul__ = __mul__

    def __truediv__(self, k):
        return Vector(self.x / k, self.y / k)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __iter__(self):
        yield self.x
        yield self.y

    def __bool__(self):
        return bool(self.x or self.y)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def angle_to(self, other):
        return math.degrees(math.acos(self.dot(other) / (abs(self) * abs(other))))

    def normalized(self):
        return self / abs(self)


a, b = Vector(3, 4), Vector(1, -2)
print("a + b =", a + b, "| a - b =", a - b, "| -a =", -a)
print("2 * a =", 2 * a, "| a * 0.5 =", a * 0.5, "| a / 2 =", a / 2)
print("|a| =", abs(a), "| a.b =", a.dot(b))
print("angle between x and y axes:", Vector(1, 0).angle_to(Vector(0, 1)))
print("unit a:", a.normalized(), "| length:", abs(a.normalized()))
print("a > b:", a > b, "| sorted:", sorted([a, b, Vector(0, 1)]))
print("unpacked:", tuple(a), "| bool(Vector()):", bool(Vector()))
print("sum of vectors:", sum([a, b, Vector(10, 10)], Vector()))
