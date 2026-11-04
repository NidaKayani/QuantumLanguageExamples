"""A polymorphic expression tree where each node subclass implements evaluate and str."""


class Expr:
    def evaluate(self, env):
        raise NotImplementedError

    def __add__(self, other):
        return Add(self, wrap(other))

    def __mul__(self, other):
        return Mul(self, wrap(other))


class Num(Expr):
    def __init__(self, value):
        self.value = value

    def evaluate(self, env):
        return self.value

    def __str__(self):
        return str(self.value)


class Var(Expr):
    def __init__(self, name):
        self.name = name

    def evaluate(self, env):
        if self.name not in env:
            raise KeyError(f"unbound variable {self.name!r}")
        return env[self.name]

    def __str__(self):
        return self.name


class BinOp(Expr):
    symbol = "?"

    def __init__(self, left, right):
        self.left, self.right = left, right

    def evaluate(self, env):
        return self.apply(self.left.evaluate(env), self.right.evaluate(env))

    def __str__(self):
        return f"({self.left} {self.symbol} {self.right})"


class Add(BinOp):
    symbol = "+"

    def apply(self, a, b):
        return a + b


class Mul(BinOp):
    symbol = "*"

    def apply(self, a, b):
        return a * b


def wrap(value):
    return value if isinstance(value, Expr) else Num(value)


x, y = Var("x"), Var("y")
expr = (x + 3) * (y + x * 2)
print("expression:", expr)
for env in [{"x": 1, "y": 2}, {"x": -3, "y": 10}, {"x": 0.5, "y": 0}]:
    print(f"  with {env}: {expr.evaluate(env)}")
try:
    expr.evaluate({"x": 1})
except KeyError as exc:
    print("error:", exc)
print("node types:", type(expr).__name__, type(expr.left).__name__, type(expr.left.left).__name__)
print("Add is BinOp:", issubclass(Add, BinOp), "| Num is BinOp:", issubclass(Num, BinOp))
