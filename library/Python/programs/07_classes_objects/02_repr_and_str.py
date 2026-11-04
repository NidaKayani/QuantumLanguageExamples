"""__repr__ versus __str__ and how print, f-strings, and containers use them."""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"

    def __str__(self):
        return f"({self.x}, {self.y})"


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __repr__(self):
        return f"{type(self).__name__}(celsius={self.celsius})"

    def __format__(self, spec):
        if spec.endswith("F"):
            value = self.celsius * 9 / 5 + 32
            return f"{value:{spec[:-1] or '.1f'}}°F"
        return f"{self.celsius:{spec or '.1f'}}°C"


p = Point(3, 4)
print(p)
print(repr(p))
print(f"str: {p}  repr: {p!r}")
print("in a list:", [p, Point(-1, 0.5)])
print("in a dict:", {"origin": Point(0, 0)})
print("str() of string coords:", str(Point("a", "b")), repr(Point("a", "b")))

t = Temperature(21.5)
print(repr(t))
print(f"{t}")
print(f"{t:.2f}")
print(f"{t:F}")
print(f"{t:.0F}")
print(format(t, "8.3f"))
print("rebuilt from repr:", eval(repr(p)).x)
