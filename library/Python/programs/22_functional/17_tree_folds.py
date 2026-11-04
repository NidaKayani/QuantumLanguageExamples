"""Folding over immutable expression trees: evaluation, pretty-printing and simplification."""
from dataclasses import dataclass
from functools import reduce
from typing import Union


@dataclass(frozen=True)
class Num:
    value: float


@dataclass(frozen=True)
class Var:
    name: str


@dataclass(frozen=True)
class Op:
    symbol: str
    left: "Expr"
    right: "Expr"


Expr = Union[Num, Var, Op]


def fold(expr, on_num, on_var, on_op):
    """Catamorphism: replace each constructor with a function."""
    def go(e):
        if isinstance(e, Num):
            return on_num(e.value)
        if isinstance(e, Var):
            return on_var(e.name)
        return on_op(e.symbol, go(e.left), go(e.right))
    return go(expr)


OPS = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "*": lambda a, b: a * b, "/": lambda a, b: a / b}


def evaluate(expr, env):
    return fold(expr, lambda v: v, lambda n: env[n], lambda s, a, b: OPS[s](a, b))


def show(expr):
    return fold(expr, lambda v: f"{v:g}", str, lambda s, a, b: f"({a} {s} {b})")


def depth(expr):
    return fold(expr, lambda _: 1, lambda _: 1, lambda _, a, b: 1 + max(a, b))


def variables(expr):
    return fold(expr, lambda _: frozenset(), lambda n: frozenset([n]), lambda _, a, b: a | b)


def simplify(expr):
    def on_op(s, a, b):
        if isinstance(a, Num) and isinstance(b, Num):
            return Num(OPS[s](a.value, b.value))
        if s == "*" and Num(0) in (a, b):
            return Num(0)
        if s == "*" and a == Num(1):
            return b
        if s in "*/" and b == Num(1) or s in "+-" and b == Num(0):
            return a
        if s == "+" and a == Num(0):
            return b
        return Op(s, a, b)
    return fold(expr, Num, Var, on_op)


def chain_sum(*terms):
    return reduce(lambda acc, t: Op("+", acc, t), terms)


e = Op("*", Op("+", Var("x"), Num(0)), Op("-", Num(5), Op("*", Num(1), Num(2))))
print("expr      :", show(e))
print("depth     :", depth(e))
print("variables :", sorted(variables(e)))
print("x=4       :", evaluate(e, {"x": 4}))
s = simplify(e)
print("simplified:", show(s), "| depth", depth(s), "| x=4 ->", evaluate(s, {"x": 4}))

poly = chain_sum(Op("*", Num(3), Op("*", Var("x"), Var("x"))), Op("*", Num(2), Var("x")), Num(1), Op("*", Num(0), Var("y")))
print("poly      :", show(poly))
print("poly simp :", show(simplify(poly)))
print("values    :", [evaluate(simplify(poly), {"x": x}) for x in range(-2, 3)])
