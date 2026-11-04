"""Single-dispatch generic functions with functools.singledispatch."""
from functools import singledispatch
from fractions import Fraction
from decimal import Decimal


@singledispatch
def describe(value):
    return f"something of type {type(value).__name__}"


@describe.register
def _(value: int):
    return f"integer {value} ({'even' if value % 2 == 0 else 'odd'})"


@describe.register
def _(value: float):
    return f"float {value:.3f}"


@describe.register
def _(value: str):
    return f"string of length {len(value)}"


@describe.register(list)
@describe.register(tuple)
def _(value):
    inner = ", ".join(describe(v) for v in value)
    return f"{type(value).__name__}[{inner}]"


@describe.register
def _(value: dict):
    return "dict with keys " + ", ".join(sorted(map(str, value)))


@describe.register
def _(value: bool):
    return f"boolean {value}"


samples = [42, 7, 3.14159, "hello", [1, "x"], (2.5, True), {"b": 1, "a": 2},
           Fraction(3, 4), Decimal("1.50"), None, True]
for s in samples:
    print(describe(s))

print("registered:", sorted(t.__name__ for t in describe.registry))
