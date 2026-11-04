"""A recursive expression tree using dataclasses: evaluate, print, differentiate."""

from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)
class Num:
    value: float


@dataclass(frozen=True)
class Var:
    name: str


@dataclass(frozen=True)
class BinOp:
    op: str
    left: "Expr"
    right: "Expr"


Expr = Union[Num, Var, BinOp]


def evaluate(e: Expr, env: dict[str, float]) -> float:
    match e:
        case Num(v):
            return v
        case Var(name):
            return env[name]
        case BinOp("+", l, r):
            return evaluate(l, env) + evaluate(r, env)
        case BinOp("*", l, r):
            return evaluate(l, env) * evaluate(r, env)
        case BinOp("-", l, r):
            return evaluate(l, env) - evaluate(r, env)
    raise ValueError(e)


def show(e: Expr) -> str:
    match e:
        case Num(v):
            return f"{v:g}"
        case Var(name):
            return name
        case BinOp(op, l, r):
            return f"({show(l)} {op} {show(r)})"


def derive(e: Expr, x: str) -> Expr:
    match e:
        case Num(_):
            return Num(0)
        case Var(name):
            return Num(1 if name == x else 0)
        case BinOp("+" | "-" as op, l, r):
            return BinOp(op, derive(l, x), derive(r, x))
        case BinOp("*", l, r):
            return BinOp("+", BinOp("*", derive(l, x), r), BinOp("*", l, derive(r, x)))


def simplify(e: Expr) -> Expr:
    if not isinstance(e, BinOp):
        return e
    l, r = simplify(e.left), simplify(e.right)
    if isinstance(l, Num) and isinstance(r, Num):
        return Num(evaluate(BinOp(e.op, l, r), {}))
    if e.op == "*" and Num(0) in (l, r):
        return Num(0)
    if e.op == "*" and l == Num(1):
        return r
    if e.op == "*" and r == Num(1):
        return l
    if e.op in "+-" and r == Num(0):
        return l
    if e.op == "+" and l == Num(0):
        return r
    return BinOp(e.op, l, r)


x, y = Var("x"), Var("y")
expr = BinOp("+", BinOp("*", Num(3), BinOp("*", x, x)), BinOp("-", BinOp("*", x, y), Num(7)))
print("f(x, y)   =", show(expr))
print("f(2, 5)   =", evaluate(expr, {"x": 2, "y": 5}))
d = derive(expr, "x")
print("raw df/dx =", show(d))
print("df/dx     =", show(simplify(d)))
print("df/dx(2,5)=", evaluate(d, {"x": 2, "y": 5}))
