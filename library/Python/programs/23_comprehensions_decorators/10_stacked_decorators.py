"""Stacking decorators and observing the order in which they wrap and execute."""
from functools import wraps

events = []


def layer(name):
    def decorator(func):
        events.append(f"decorate with {name}")

        @wraps(func)
        def wrapper(*args, **kwargs):
            events.append(f"enter {name}")
            result = func(*args, **kwargs)
            events.append(f"exit {name}")
            return result
        return wrapper
    return decorator


@layer("outer")
@layer("middle")
@layer("inner")
def compute(x):
    events.append("run compute")
    return x * 2


print("At definition time:", events)
events.clear()
print("compute(21) =", compute(21))
print("At call time:")
for e in events:
    print("  ", e)


def bold(func):
    @wraps(func)
    def wrapper(*a):
        return f"<b>{func(*a)}</b>"
    return wrapper


def italic(func):
    @wraps(func)
    def wrapper(*a):
        return f"<i>{func(*a)}</i>"
    return wrapper


def strip_args(func):
    @wraps(func)
    def wrapper(*a):
        return func(*(s.strip() for s in a))
    return wrapper


@bold
@italic
@strip_args
def greet(name):
    return f"Hello {name}"


@italic
@bold
def farewell(name):
    return f"Bye {name}"


print(greet("   Ada  "))
print(farewell("Ada"))

unwrapped = greet
chain = []
while hasattr(unwrapped, "__wrapped__"):
    chain.append(unwrapped.__name__)
    unwrapped = unwrapped.__wrapped__
print("wrapper depth:", len(chain), "| innermost result:", unwrapped(" raw "))

equivalent = bold(italic(strip_args(lambda n: f"Hello {n}")))
print("manual stacking matches:", equivalent("  Ada ") == greet("   Ada  "))
