"""Basic decorators: tracing calls, counting invocations, and enforcing preconditions."""
import functools


def trace(func):
    depth = 0

    @functools.wraps(func)
    def wrapper(*args):
        nonlocal depth
        print(f"{'  ' * depth}-> {func.__name__}{args}")
        depth += 1
        try:
            result = func(*args)
        finally:
            depth -= 1
        print(f"{'  ' * depth}<- {func.__name__} = {result}")
        return result

    return wrapper


def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def non_negative(func):
    @functools.wraps(func)
    def wrapper(n):
        if n < 0:
            raise ValueError(f"{func.__name__} requires n >= 0, got {n}")
        return func(n)

    return wrapper


@trace
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


@count_calls
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


@non_negative
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


print("gcd trace:")
gcd(84, 36)

print("fib(15) =", fib(15), "using", fib.calls, "calls")
fib.calls = 0
print("fib(10) =", fib(10), "using", fib.calls, "calls")

print("factorial(10) =", factorial(10))
try:
    factorial(-3)
except ValueError as exc:
    print("error:", exc)


def shout(func):
    return lambda *a: func(*a).upper() + "!"


def greet(name):
    return f"hello, {name}"


manual = shout(greet)
print("manually decorated:", manual("world"))
print("original untouched:", greet("world"))
print("wrapped names:", gcd.__name__, fib.__name__, factorial.__name__)
