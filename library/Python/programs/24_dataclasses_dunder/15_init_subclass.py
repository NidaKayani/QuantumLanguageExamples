"""__init_subclass__ for automatic subclass registration, required attributes and per-class config."""


class Shape:
    registry = {}

    def __init_subclass__(cls, /, key=None, sides=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "area"):
            raise TypeError(f"{cls.__name__} must define area()")
        cls.sides = sides
        Shape.registry[key or cls.__name__.lower()] = cls

    @classmethod
    def create(cls, kind, *args):
        return cls.registry[kind](*args)

    def describe(self):
        return f"{type(self).__name__} with {self.sides} sides, area {self.area():.2f}"


class Square(Shape, sides=4):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape, key="tri", sides=3):
    def __init__(self, base, height):
        self.base, self.height = base, height

    def area(self):
        return 0.5 * self.base * self.height


class Circle(Shape, sides=0):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.141592653589793 * self.r ** 2


print("registry:", sorted(Shape.registry))
for kind, args in [("square", (3,)), ("tri", (4, 5)), ("circle", (1.5,))]:
    print(" ", Shape.create(kind, *args).describe())

try:
    class Blob(Shape):
        pass
except TypeError as exc:
    print("rejected subclass:", exc)
print("Blob registered?", "blob" in Shape.registry)


class Serializer:
    formats = {}

    def __init_subclass__(cls, fmt, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.fmt = fmt
        Serializer.formats[fmt] = cls()


class CSV(Serializer, fmt="csv"):
    def dump(self, rows):
        return "\n".join(",".join(map(str, r)) for r in rows)


class Markdown(Serializer, fmt="md"):
    def dump(self, rows):
        header, *body = rows
        lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
        return "\n".join(lines + ["| " + " | ".join(map(str, r)) + " |" for r in body])


data = [("name", "qty"), ("apple", 3), ("pear", 7)]
for fmt, serializer in Serializer.formats.items():
    print(f"--- {fmt} ({type(serializer).__name__}) ---")
    print(serializer.dump(data))
