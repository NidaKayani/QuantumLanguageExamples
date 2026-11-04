"""functools.wraps preserving metadata in logging, validation and retry decorators."""
from functools import wraps


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        parts = [repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()]
        result = func(*args, **kwargs)
        print(f"  {func.__name__}({', '.join(parts)}) -> {result!r}")
        return result
    return wrapper


def validate(**checks):
    def decorator(func):
        @wraps(func)
        def wrapper(**kwargs):
            for name, check in checks.items():
                if not check(kwargs[name]):
                    raise ValueError(f"{func.__name__}: invalid {name}={kwargs[name]!r}")
            return func(**kwargs)
        return wrapper
    return decorator


def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            for attempt in range(1, times + 1):
                try:
                    return func(*args)
                except ConnectionError as exc:
                    print(f"  attempt {attempt} failed: {exc}")
            raise RuntimeError(f"{func.__name__} gave up after {times} attempts")
        return wrapper
    return decorator


@logged
def area(width, height=1):
    """Rectangle area."""
    return width * height


@validate(age=lambda a: 0 <= a < 150, name=lambda n: n.isalpha())
def register(name, age):
    """Register a person."""
    return f"{name} ({age})"


calls = {"n": 0}


@retry(times=3)
def flaky_fetch(url):
    """Fails twice, then succeeds."""
    calls["n"] += 1
    if calls["n"] < 3:
        raise ConnectionError(f"timeout #{calls['n']}")
    return f"payload from {url}"


print("Logging:")
area(3, 4)
area(5, height=2)
print("Metadata kept:", area.__name__, "|", area.__doc__, "|", area.__wrapped__(2, 3))

print("Validation:")
print(" ", register(name="Ada", age=36))
for bad in ({"name": "R2D2", "age": 3}, {"name": "Bob", "age": 200}):
    try:
        register(**bad)
    except ValueError as exc:
        print("  rejected:", exc)

print("Retry:")
print(" ", flaky_fetch("api/items"))
print(" ", flaky_fetch.__name__, "-", flaky_fetch.__doc__)
