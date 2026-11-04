"""A small expression calculator that reports errors with custom exception types."""
import re
import operator


class CalcError(Exception):
    pass


class TokenError(CalcError):
    pass


class SyntaxProblem(CalcError):
    pass


OPS = {"+": (1, operator.add), "-": (1, operator.sub),
       "*": (2, operator.mul), "/": (2, operator.truediv)}


def tokenize(expr):
    tokens = re.findall(r"\d+\.?\d*|[-+*/()]|\S", expr)
    for t in tokens:
        if not (t in OPS or t in "()" or re.fullmatch(r"\d+\.?\d*", t)):
            raise TokenError(f"unexpected character {t!r}")
    return tokens


def evaluate(expr):
    tokens = tokenize(expr)
    pos = 0

    def parse(min_prec=1):
        nonlocal pos
        left = atom()
        while pos < len(tokens) and tokens[pos] in OPS and OPS[tokens[pos]][0] >= min_prec:
            prec, fn = OPS[tokens[pos]]
            pos += 1
            right = parse(prec + 1)
            try:
                left = fn(left, right)
            except ZeroDivisionError as exc:
                raise CalcError("division by zero in expression") from exc
        return left

    def atom():
        nonlocal pos
        if pos >= len(tokens):
            raise SyntaxProblem("unexpected end of expression")
        tok = tokens[pos]
        pos += 1
        if tok == "(":
            value = parse()
            if pos >= len(tokens) or tokens[pos] != ")":
                raise SyntaxProblem("missing closing parenthesis")
            pos += 1
            return value
        if tok in OPS or tok == ")":
            raise SyntaxProblem(f"unexpected {tok!r}")
        return float(tok)

    result = parse()
    if pos != len(tokens):
        raise SyntaxProblem(f"trailing input at token {pos}")
    return result


for expr in ["1 + 2 * 3", "(1 + 2) * 3", "10 / 4 - 1", "2 * (3 + 4", "5 / (2 - 2)",
             "7 $ 3", "4 +", "3 4"]:
    try:
        print(f"{expr:<14} = {evaluate(expr):g}")
    except CalcError as exc:
        print(f"{expr:<14} ! {type(exc).__name__}: {exc}")
