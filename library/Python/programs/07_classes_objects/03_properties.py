"""Managed attributes with @property, setters, deleters, and computed values."""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError(f"width must be positive, got {value}")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError(f"height must be positive, got {value}")
        self._height = value

    @property
    def area(self):
        return self.width * self.height

    @property
    def is_square(self):
        return self.width == self.height


class Person:
    def __init__(self, first, last):
        self.first, self.last = first, last
        self._nickname = None

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, value):
        self.first, self.last = value.split(" ", 1)

    @property
    def nickname(self):
        return self._nickname or self.first

    @nickname.setter
    def nickname(self, value):
        self._nickname = value

    @nickname.deleter
    def nickname(self):
        self._nickname = None


r = Rectangle(3, 4)
print(f"{r.width}x{r.height} area={r.area} square={r.is_square}")
r.width = 4
print(f"{r.width}x{r.height} area={r.area} square={r.is_square}")
for bad in (0, -2):
    try:
        r.height = bad
    except ValueError as exc:
        print("rejected:", exc)
try:
    r.area = 100
except AttributeError:
    print("area is read-only")

p = Person("Margaret", "Hamilton")
print(p.full_name, "/", p.nickname)
p.nickname = "Maggie"
print("nickname:", p.nickname)
del p.nickname
print("after delete:", p.nickname)
p.full_name = "Katherine Johnson"
print("renamed:", p.first, "|", p.last)
