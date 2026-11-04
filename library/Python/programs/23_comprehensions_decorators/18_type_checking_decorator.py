"""A decorator that enforces type annotations at call time and coerces simple values."""
from functools import wraps
from typing import get_type_hints


def typechecked(func=None, *, coerce=False):
    if func is None:
        return lambda f: typechecked(f, coerce=coerce)

    hints = get_type_hints(func)
    names = func.__code__.co_varnames[:func.__code__.co_argcount]

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = dict(zip(names, args), **kwargs)
        for name, value in list(bound.items()):
            expected = hints.get(name)
            if expected is None or isinstance(value, expected):
                continue
            if coerce:
                try:
                    bound[name] = expected(value)
                    continue
                except (TypeError, ValueError):
                    pass
            raise TypeError(f"{func.__name__}(): {name} must be {expected.__name__}, "
                            f"got {type(value).__name__} {value!r}")
        result = func(**bound)
        if "return" in hints and not isinstance(result, hints["return"]):
            raise TypeError(f"{func.__name__}() returned {type(result).__name__}")
        return result

    return wrapper


@typechecked
def repeat(text: str, times: int) -> str:
    return text * times


@typechecked(coerce=True)
def area(width: float, height: float) -> float:
    return width * height


@typechecked
def broken(n: int) -> str:
    return n * 2


tests = [
    (repeat, ("ab", 3), {}),
    (repeat, ("ab",), {"times": 2}),
    (repeat, (3, "ab"), {}),
    (area, ("2.5", 4), {}),
    (area, (3, "wide"), {}),
    (broken, (4,), {}),
]
for func, args, kwargs in tests:
    try:
        print(f"{func.__name__}{args} {kwargs or ''} -> {func(*args, **kwargs)!r}")
    except TypeError as exc:
        print(f"{func.__name__}{args} {kwargs or ''} !! {exc}")

print("annotations:", {k: v.__name__ for k, v in get_type_hints(repeat.__wrapped__).items()})
