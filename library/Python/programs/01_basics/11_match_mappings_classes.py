"""Match dictionaries and dataclass instances with structural patterns."""

from dataclasses import dataclass


@dataclass
class Circle:
    radius: float


@dataclass
class Rect:
    width: float
    height: float


def area(shape):
    match shape:
        case Circle(radius=r):
            return 3.14159 * r * r
        case Rect(width=w, height=h) if w == h:
            print("  (a square)")
            return w * w
        case Rect(w, h):
            return w * h
        case _:
            raise ValueError("unknown shape")


def handle(event):
    match event:
        case {"type": "click", "x": x, "y": y}:
            return f"click at ({x}, {y})"
        case {"type": "key", "key": str(k)} if len(k) == 1:
            return f"key press {k!r}"
        case {"type": "key", "key": k}:
            return f"special key {k}"
        case {"type": t, **rest}:
            return f"unhandled {t} with {sorted(rest)}"
        case _:
            return "not an event"



for s in (Circle(2), Rect(3, 4), Rect(5, 5)):
    print(f"{s} area = {area(s):.2f}")

events = [
    {"type": "click", "x": 10, "y": 20},
    {"type": "key", "key": "a"},
    {"type": "key", "key": "Enter"},
    {"type": "scroll", "dy": -3, "dx": 0},
    42,
]
for e in events:
    print(handle(e))
