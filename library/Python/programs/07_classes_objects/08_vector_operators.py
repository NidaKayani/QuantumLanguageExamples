"""Operator overloading on a 2D vector: arithmetic, unary, reflected, and in-place ops."""
import math


class Vector:
    __slots__ = ("x", "y")

    def __init__(self, x=0.0, y=0.0):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        if isinstance(k, Vector):
            return self.x * k.x + self.y * k.y  # dot product
        return Vector(self.x * k, self.y * k)

    __rmul__ = __mul__

    def __truediv__(self, k):
        return Vector(self.x / k, self.y / k)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __eq__(self, other):
        return isinstance(other, Vector) and (self.x, self.y) == (other.x, other.y)

    def __repr__(self):
        return f"Vector({self.x:g}, {self.y:g})"


a, b = Vector(3, 4), Vector(1, -2)
print("a + b =", a + b)
print("a - b =", a - b)
print("a * 2 =", a * 2, "| 3 * b =", 3 * b)
print("a / 2 =", a / 2)
print("-a =", -a)
print("|a| =", abs(a))
print("a . b =", a * b)
print("bool(Vector()) =", bool(Vector()), "| bool(a) =", bool(a))
pos = Vector()
for step in [Vector(1, 0), Vector(0, 2), Vector(-3, 1)]:
    pos += step
print("position after steps:", pos)
print("equal:", Vector(1, 2) == Vector(1.0, 2.0))
print("sum of vectors:", sum([a, b, pos], Vector()))
