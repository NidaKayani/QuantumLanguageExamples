"""Decorator factories that take arguments: repeat, default values, rate tags and optional-args style."""
from functools import wraps


def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(times)]
        return wrapper
    return decorator


def clamp_result(low, high):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return max(low, min(high, func(*args, **kwargs)))
        return wrapper
    return decorator


def tag(func=None, *, prefix="[", suffix="]"):
    """Usable as @tag or @tag(prefix=...)."""
    if func is None:
        return lambda f: tag(f, prefix=prefix, suffix=suffix)

    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"{prefix}{func(*args, **kwargs)}{suffix}"
    return wrapper


def suppress(*exceptions, default=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions as exc:
                print(f"  suppressed {type(exc).__name__}: {exc}")
                return default
        return wrapper
    return decorator


counter = iter(range(100))


@repeat(times=4)
def next_ticket():
    return f"T{next(counter):03d}"


@clamp_result(0, 100)
def percentage(part, whole):
    return round(100 * part / whole)


@tag
def plain(text):
    return text


@tag(prefix="<b>", suffix="</b>")
def bold(text):
    return text


@suppress(ZeroDivisionError, KeyError, default=-1)
def risky(mapping, key, divisor):
    return mapping[key] // divisor


print("tickets:", next_ticket())
print("more tickets:", next_ticket())
print("percentages:", [percentage(p, 40) for p in (-5, 10, 40, 55)])
print("tags:", plain("note"), bold("important"))
print("risky ok:", risky({"a": 10}, "a", 3))
print("risky div:", risky({"a": 10}, "a", 0))
print("risky key:", risky({"a": 10}, "b", 2))
try:
    risky(None, "a", 1)
except TypeError as exc:
    print("not suppressed:", type(exc).__name__)
