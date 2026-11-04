"""Function decorators: plain, parameterized, stacked, and with functools.wraps."""
from functools import wraps

call_log = []


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        call_log.append(f"{func.__name__}{args}")
        return func(*args, **kwargs)
    return wrapper


def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(times)]
        return wrapper
    return decorator


def validate_positive(func):
    @wraps(func)
    def wrapper(*args):
        if any(a <= 0 for a in args):
            raise ValueError(f"{func.__name__} requires positive arguments, got {args}")
        return func(*args)
    return wrapper


@logged
def add(a, b):
    """Add two numbers."""
    return a + b


@repeat(3)
def shout(word):
    return word.upper() + "!"


@logged
@validate_positive
def ratio(a, b):
    return a / b


print(add(2, 3), add(10, -4))
print(shout("hey"))
print(ratio(9, 3))
try:
    ratio(5, 0)
except ValueError as exc:
    print("error:", exc)
print("log:", call_log)
print("metadata:", add.__name__, "-", add.__doc__)
print("unwrapped:", add.__wrapped__(100, 1))
