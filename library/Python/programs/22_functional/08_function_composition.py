"""Function composition with a small Composable wrapper supporting the | and @ operators."""
from functools import reduce


class Composable:
    def __init__(self, func, name=None):
        self.func = func
        self.name = name or func.__name__

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __or__(self, other):
        """Left-to-right: (f | g)(x) == g(f(x))."""
        other = other if isinstance(other, Composable) else Composable(other)
        return Composable(lambda *a, **k: other(self(*a, **k)), f"{self.name} | {other.name}")

    def __matmul__(self, other):
        """Mathematical: (f @ g)(x) == f(g(x))."""
        other = other if isinstance(other, Composable) else Composable(other)
        return other | self

    def __repr__(self):
        return f"<{self.name}>"


def compose(*funcs):
    return reduce(lambda f, g: lambda x: f(g(x)), funcs)


def pipe(value, *funcs):
    for f in funcs:
        value = f(value)
    return value


inc = Composable(lambda x: x + 1, "inc")
double = Composable(lambda x: x * 2, "double")
square = Composable(lambda x: x * x, "square")

f = inc | double | square
g = square @ double @ inc
h = inc @ double
print(repr(f), [f(x) for x in range(5)])
print(repr(g), [g(x) for x in range(5)])
print(repr(h), [h(x) for x in range(5)])

clean = Composable(str.strip) | str.lower | str.split | Composable(sorted) | " ".join
print(repr(clean))
print(clean("  The Zebra Ate An apple  "))

math_chain = compose(abs, lambda x: x - 10, lambda x: x * 3)
print("compose(abs, -10, *3):", [math_chain(x) for x in range(6)])

print("pipe:", pipe("3,1,2,5,4", lambda s: s.split(","), lambda xs: map(int, xs), sorted, tuple))

identity_law = all((inc | Composable(lambda x: x, "id"))(x) == inc(x) for x in range(10))
assoc_law = all(((inc | double) | square)(x) == (inc | (double | square))(x) for x in range(10))
print("identity law holds:", identity_law, "| associativity holds:", assoc_law)
