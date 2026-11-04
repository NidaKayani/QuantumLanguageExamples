"""Function docstrings, type annotations, and introspecting them at runtime."""
from typing import Optional, Union, Callable


def area(width: float, height: float = 1.0) -> float:
    """Return the area of a rectangle.

    Width and height must be non-negative.
    """
    return width * height


def find(items: list[str], target: str) -> Optional[int]:
    """Return the index of target or None."""
    try:
        return items.index(target)
    except ValueError:
        return None


def apply(fn: Callable[[int], int], value: Union[int, str]) -> int:
    return fn(int(value))


def undocumented(x, y):
    return x + y


print("area name:", area.__name__)
print("area doc first line:", area.__doc__.splitlines()[0])
print("area annotations:")
for name, kind in area.__annotations__.items():
    print(f"  {name}: {kind.__name__}")
print("area(3, 4) =", area(3, 4))

print("find annotations:", {k: str(v) for k, v in find.__annotations__.items()})
print("find hit:", find(["x", "y", "z"], "z"), "miss:", find(["x"], "q"))
print("apply:", apply(lambda n: n * 10, "7"))
print("undocumented doc:", undocumented.__doc__)
print("undocumented annotations:", undocumented.__annotations__)

# Annotations are not enforced at runtime
print("area('ab', 3) =", area("ab", 3))
