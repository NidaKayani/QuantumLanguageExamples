"""Structural typing with typing.Protocol and runtime_checkable, versus nominal abc.ABC."""
from abc import ABC, abstractmethod
from typing import Iterable, Protocol, runtime_checkable


@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str: ...


@runtime_checkable
class Sized2D(Protocol):
    width: int
    height: int


class SupportsArea(Protocol):
    def area(self) -> float: ...


class Box:
    def __init__(self, width, height):
        self.width, self.height = width, height

    def draw(self):
        return "\n".join("#" * self.width for _ in range(self.height))

    def area(self):
        return float(self.width * self.height)


class Label:
    def __init__(self, text):
        self.text = text

    def draw(self):
        return f"[{self.text}]"


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y


class Animal(ABC):
    @abstractmethod
    def sound(self) -> str: ...

    def speak(self):
        return f"{type(self).__name__} says {self.sound()}"


class Dog(Animal):
    def sound(self):
        return "woof"


def render_all(items: Iterable[Drawable]) -> list[str]:
    return [item.draw() for item in items]


def total_area(shapes: Iterable[SupportsArea]) -> float:
    return sum(s.area() for s in shapes)


objects = [Box(3, 2), Label("ok"), Point(1, 2)]
for obj in objects:
    print(f"{type(obj).__name__:<6} Drawable={isinstance(obj, Drawable)!s:<5} Sized2D={isinstance(obj, Sized2D)}")

drawables = [o for o in objects if isinstance(o, Drawable)]
print("rendered:")
for text in render_all(drawables):
    print(text)
print("total area:", total_area([Box(2, 2), Box(5, 1)]))

print(Dog().speak())
try:
    Animal()
except TypeError as exc:
    print("cannot instantiate ABC:", type(exc).__name__)
print("Dog is Animal (nominal):", issubclass(Dog, Animal), "| Box is Animal:", issubclass(Box, Animal))
print("Label structurally Drawable without inheriting:", Drawable not in Label.__mro__ and isinstance(Label("x"), Drawable))
