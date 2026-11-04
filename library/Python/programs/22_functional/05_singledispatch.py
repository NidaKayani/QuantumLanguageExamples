"""Type-based dispatch with functools.singledispatch and singledispatchmethod."""
from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from functools import singledispatch, singledispatchmethod


@singledispatch
def to_json(value):
    raise TypeError(f"cannot serialize {type(value).__name__}")


@to_json.register
def _(value: bool):
    return "true" if value else "false"


@to_json.register(int)
@to_json.register(float)
def _(value):
    return repr(value)


@to_json.register
def _(value: str):
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


@to_json.register(type(None))
def _(value):
    return "null"


@to_json.register(list)
@to_json.register(tuple)
def _(value):
    return "[" + ", ".join(to_json(v) for v in value) + "]"


@to_json.register
def _(value: dict):
    return "{" + ", ".join(f"{to_json(str(k))}: {to_json(v)}" for k, v in value.items()) + "}"


@to_json.register
def _(value: Fraction):
    return to_json(f"{value.numerator}/{value.denominator}")


doc = {"name": "Widget \"Pro\"", "price": 9.5, "qty": 3, "tags": ("new", "sale"),
       "active": True, "parent": None, "ratio": Fraction(3, 8)}
print(to_json(doc))
try:
    to_json(Decimal("1.5"))
except TypeError as exc:
    print("Error:", exc)

print("Registered types:", sorted(t.__name__ for t in to_json.registry if t is not object))


@dataclass
class Shape:
    name: str


class Geometry:
    @singledispatchmethod
    def describe(self, arg):
        return f"something else: {arg!r}"

    @describe.register
    def _(self, arg: int):
        return f"an integer with {arg.bit_length()} bits"

    @describe.register
    def _(self, arg: Shape):
        return f"a shape called {arg.name}"

    @describe.register
    def _(self, arg: list):
        return f"a list of {len(arg)}: " + "; ".join(self.describe(x) for x in arg)


g = Geometry()
print(g.describe(255))
print(g.describe(Shape("hexagon")))
print(g.describe([1, Shape("circle"), "text"]))
