"""Geometry with namedtuple subclasses: polygon area, perimeter, centroid."""

from collections import namedtuple
from math import hypot


class Point(namedtuple("Point", "x y")):
    __slots__ = ()

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def __str__(self):
        return f"({self.x:g}, {self.y:g})"


Segment = namedtuple("Segment", "start end")


def length(seg: Segment) -> float:
    d = seg.end - seg.start
    return hypot(d.x, d.y)


def edges(poly):
    return [Segment(a, b) for a, b in zip(poly, poly[1:] + poly[:1])]


def area(poly):
    return abs(sum(s.start.cross(s.end) for s in edges(poly))) / 2


def centroid(poly):
    n = len(poly)
    return Point(sum(p.x for p in poly) / n, sum(p.y for p in poly) / n)


def is_convex(poly):
    signs = set()
    for a, b, c in zip(poly, poly[1:] + poly[:1], poly[2:] + poly[:2]):
        turn = (b - a).cross(c - b)
        if turn:
            signs.add(turn > 0)
    return len(signs) == 1


shapes = {
    "square": [Point(0, 0), Point(4, 0), Point(4, 4), Point(0, 4)],
    "triangle": [Point(0, 0), Point(6, 0), Point(3, 4)],
    "arrow": [Point(0, 0), Point(4, 2), Point(0, 4), Point(1, 2)],
}

for name, poly in shapes.items():
    perim = sum(map(length, edges(poly)))
    print(f"{name:<8} vertices={' '.join(map(str, poly))}")
    print(f"         area={area(poly):.2f} perimeter={perim:.3f} "
          f"centroid={centroid(poly)} convex={is_convex(poly)}")
