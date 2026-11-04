"""typing.NamedTuple with annotations, defaults, methods and properties."""

from typing import NamedTuple
import math


class Vector(NamedTuple):
    x: float
    y: float
    z: float = 0.0

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def scale(self, k: float) -> "Vector":
        return Vector(*(k * c for c in self))

    @property
    def length(self) -> float:
        return math.sqrt(sum(c * c for c in self))

    def dot(self, other: "Vector") -> float:
        return sum(a * b for a, b in zip(self, other))


class Book(NamedTuple):
    title: str
    author: str
    year: int
    tags: tuple = ()

    def describe(self) -> str:
        tag_str = ", ".join(self.tags) or "untagged"
        return f"{self.title!r} by {self.author} ({self.year}) [{tag_str}]"


v = Vector(1, 2, 2)
w = Vector(3, 0)
print("v:", v)
print("w (default z):", w)
print("length of v:", v.length)
print("v . w =", v.dot(w))
print("v.scale(2):", v.scale(2))
print("v + w (overridden __add__):", v + w)
print("annotations:", Vector.__annotations__)

library = [
    Book("Dune", "Herbert", 1965, ("scifi", "classic")),
    Book("Neuromancer", "Gibson", 1984, ("scifi", "cyberpunk")),
    Book("Emma", "Austen", 1815),
]
for book in sorted(library, key=lambda b: b.year):
    print(" ", book.describe())

print("as dict:", library[2]._asdict())
