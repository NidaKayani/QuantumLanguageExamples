"""Using super() inside classmethods and properties across an inheritance chain."""


class Shape:
    sides = 0

    @classmethod
    def describe(cls):
        return [f"{cls.__name__} with {cls.sides} sides"]

    @property
    def label(self):
        return "shape"


class Polygon(Shape):
    sides = 3

    @classmethod
    def describe(cls):
        return super().describe() + ["a closed polygon"]

    @property
    def label(self):
        return "polygon/" + super().label


class Quad(Polygon):
    sides = 4

    @classmethod
    def describe(cls):
        return super().describe() + ["with four corners"]

    @property
    def label(self):
        return "quad/" + super().label


class Square(Quad):
    @classmethod
    def describe(cls):
        return super().describe() + ["all sides equal"]


for cls in (Shape, Polygon, Quad, Square):
    print(f"{cls.__name__}.describe():")
    for line in cls.describe():
        print("   ", line)
    print("    label:", cls().label)

print("Square inherits sides:", Square.sides, "| defined on Square?", "sides" in vars(Square))
