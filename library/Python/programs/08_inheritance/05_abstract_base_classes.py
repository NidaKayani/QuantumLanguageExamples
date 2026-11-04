"""Abstract base classes with abc.ABC and @abstractmethod enforcing an interface."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimeter(self):
        ...

    def describe(self):
        return f"{type(self).__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Incomplete(Shape):
    def area(self):
        return 0


try:
    Shape()
except TypeError as exc:
    print("TypeError:", exc)
try:
    Incomplete()
except TypeError as exc:
    print("TypeError:", exc)

shapes = [Circle(1), Rectangle(3, 4), Square(2.5), Circle(0.5)]
for s in shapes:
    print(s.describe())
print("largest:", type(max(shapes, key=lambda s: s.area())).__name__)
print("total area:", round(sum(s.area() for s in shapes), 3))
print("abstract methods:", sorted(Shape.__abstractmethods__))
print("Incomplete still missing:", sorted(Incomplete.__abstractmethods__))
