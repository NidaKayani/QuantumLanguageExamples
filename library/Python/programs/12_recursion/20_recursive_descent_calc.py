"""A recursive-descent calculator supporting + - * / ^, unary minus and parentheses."""

import re
from fractions import Fraction

TOKEN = re.compile(r"\s*(?:(\d+(?:\.\d+)?)|(.))")


def tokenize(src: str) -> list[str]:
    tokens = []
    for number, op in TOKEN.findall(src):
        tokens.append(number or op)
    return [t for t in tokens if t.strip()]


class Parser:
    def __init__(self, src: str):
        self.tokens = tokenize(src)
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def take(self, expected=None):
        tok = self.peek()
        if expected is not None and tok != expected:
            raise SyntaxError(f"expected {expected!r}, got {tok!r}")
        self.pos += 1
        return tok

    def parse(self):
        value = self.expr()
        if self.peek() is not None:
            raise SyntaxError(f"unexpected {self.peek()!r}")
        return value

    def expr(self):            # expr := term (('+'|'-') term)*
        value = self.term()
        while self.peek() in ("+", "-"):
            value = value + self.term() if self.take() == "+" else value - self.term()
        return value

    def term(self):            # term := factor (('*'|'/') factor)*
        value = self.factor()
        while self.peek() in ("*", "/"):
            value = value * self.factor() if self.take() == "*" else value / self.factor()
        return value

    def factor(self):          # factor := '-' factor | power
        if self.peek() == "-":
            self.take()
            return -self.factor()
        return self.power()

    def power(self):           # power := atom ('^' factor)?   (right associative)
        base = self.atom()
        if self.peek() == "^":
            self.take()
            return base ** int(self.factor())
        return base

    def atom(self):
        tok = self.take()
        if tok == "(":
            value = self.expr()
            self.take(")")
            return value
        if tok is None or not tok[0].isdigit():
            raise SyntaxError(f"unexpected token {tok!r}")
        return Fraction(tok)


for src in ["1 + 2 * 3", "(1 + 2) * 3", "2 ^ 3 ^ 2", "-4 + 10 / 4", "1/3 + 1/6", "((7))", "2 * (3 + 4) ^ 2 - 1.5", "3 +", "4 * (2 + 1"]:
    try:
        result = Parser(src).parse()
        print(f"{src:<24} = {result} ({float(result):g})")
    except (SyntaxError, ZeroDivisionError) as exc:
        print(f"{src:<24} ! {type(exc).__name__}: {exc}")
