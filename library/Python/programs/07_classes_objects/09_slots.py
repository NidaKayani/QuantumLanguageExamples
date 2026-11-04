"""Memory-lean classes with __slots__ and the restrictions they impose."""


class SlottedPoint:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"SlottedPoint({self.x}, {self.y})"


class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Pixel(SlottedPoint):
    __slots__ = ("color",)

    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.color = color

    def __repr__(self):
        return f"Pixel({self.x}, {self.y}, {self.color!r})"


sp = SlottedPoint(1, 2)
rp = RegularPoint(1, 2)
print(sp)
print("slots:", SlottedPoint.__slots__)
print("SlottedPoint has __dict__:", hasattr(sp, "__dict__"))
print("RegularPoint has __dict__:", hasattr(rp, "__dict__"), vars(rp))

rp.z = 3
print("regular point gained z:", rp.z)
try:
    sp.z = 3
except AttributeError as exc:
    print("AttributeError:", exc)

sp.x = 10
print("slot attribute updated:", sp)
del sp.y
try:
    print(sp.y)
except AttributeError:
    print("y is unset after del")
sp.y = 20
print("restored:", sp)

px = Pixel(5, 6, "red")
print(px, "| all slots:", [s for cls in type(px).__mro__ for s in getattr(cls, "__slots__", ())])
pixels = [Pixel(i, i * i, c) for i, c in enumerate(["red", "green", "blue"])]
print("pixels:", pixels)
