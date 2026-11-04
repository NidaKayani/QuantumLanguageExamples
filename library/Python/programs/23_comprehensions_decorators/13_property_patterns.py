"""The @property decorator for validation, computed attributes, read-only fields and lazy values."""
import math


class Temperature:
    def __init__(self, celsius=0.0):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError(f"{value} is below absolute zero")
        self._celsius = float(value)

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    @property
    def kelvin(self):
        return self._celsius + 273.15


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area_computations = 0

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("radius must be positive")
        self._radius = value
        self._area = None

    @radius.deleter
    def radius(self):
        raise AttributeError("radius cannot be deleted")

    @property
    def area(self):
        if self._area is None:
            self._area_computations += 1
            self._area = math.pi * self._radius ** 2
        return self._area


class Account:
    def __init__(self, owner):
        self._owner = owner

    owner = property(lambda self: self._owner, doc="read-only owner name")


t = Temperature(25)
print(f"{t.celsius:.1f}C = {t.fahrenheit:.1f}F = {t.kelvin:.2f}K")
t.fahrenheit = 212
print(f"after setting 212F: {t.celsius:.1f}C")
for bad in (-300,):
    try:
        t.celsius = bad
    except ValueError as exc:
        print("rejected:", exc)

c = Circle(2)
print(f"area={c.area:.4f} area again={c.area:.4f} computations={c._area_computations}")
c.radius = 3
print(f"new area={c.area:.4f} computations={c._area_computations}")
for action in (lambda: setattr(c, "radius", -1), lambda: delattr(c, "radius"), lambda: setattr(c, "area", 5)):
    try:
        action()
    except (ValueError, AttributeError) as exc:
        print(f"{type(exc).__name__}: {exc}")

acct = Account("ann")
print("owner:", acct.owner, "| doc:", Account.owner.__doc__)
print("is property:", isinstance(Account.owner, property), "| has setter:", Account.owner.fset is not None)
