"""A 2D Vector class implementing arithmetic, comparison, hashing, truthiness and iteration dunders."""
import math


class Vector:
    __slots__ = ("x", "y")

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        if isinstance(scalar, Vector):
            return self.x * scalar.x + self.y * scalar.y  # dot product
        return Vector(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __eq__(self, other):
        return isinstance(other, Vector) and (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __iter__(self):
        yield self.x
        yield self.y

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


a, b = Vector(3, 4), Vector(1, -2)
print("a + b =", a + b, "| a - b =", a - b)
print("a * 2 =", a * 2, "| 3 * b =", 3 * b, "| a / 2 =", a / 2)
print("dot a.b =", a * b, "| -a =", -a, "| |a| =", abs(a))
print("bool:", bool(a), bool(Vector()), "| equal:", a == Vector(3, 4), a != b)
x, y = a
print("unpacked:", x, y, "| as tuple:", tuple(b), "| max component:", max(a))
print("set dedup:", len({Vector(1, 1), Vector(1, 1), Vector(2, 2)}))
try:
    a + 5
except TypeError as exc:
    print("TypeError:", exc)

pos, vel = Vector(0, 0), Vector(1.5, 2.0)
start = pos
for _ in range(4):
    pos += vel
print("after 4 steps:", pos, "| same object after +=:", pos is start)
print("total:", sum([Vector(1, 2), Vector(3, 4), Vector(5, 6)], Vector()))
angle = math.degrees(math.acos((a * b) / (abs(a) * abs(b))))
print(f"angle between a and b: {angle:.2f} degrees")
try:
    a.z = 1
except AttributeError:
    print("__slots__ prevents new attributes")
