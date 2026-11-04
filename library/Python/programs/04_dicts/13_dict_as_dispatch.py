"""Dispatch operations through a dictionary of functions instead of if/elif chains."""

import operator


def cmd_help(args):
    return "commands: " + ", ".join(sorted(COMMANDS))


def cmd_add(args):
    return sum(map(float, args))


def cmd_upper(args):
    return " ".join(args).upper()


def cmd_count(args):
    return {word: args.count(word) for word in dict.fromkeys(args)}


COMMANDS = {
    "help": cmd_help,
    "add": cmd_add,
    "upper": cmd_upper,
    "count": cmd_count,
}


def run(line):
    name, *args = line.split()
    handler = COMMANDS.get(name)
    if handler is None:
        return f"unknown command {name!r}"
    return handler(args)


for line in ["help", "add 1 2 3.5", "upper hello there", "count a b a c b a", "fly away"]:
    print(f"> {line}\n  {run(line)}")

OPS = {
    "+": operator.add, "-": operator.sub, "*": operator.mul,
    "/": operator.truediv, "**": operator.pow, "%": operator.mod,
}


def calc(expr):
    left, op, right = expr.split()
    return OPS[op](float(left), float(right))


for expr in ("6 * 7", "2 ** 10", "17 % 5", "1 / 8"):
    print(f"{expr} = {calc(expr)}")

handlers = {int: lambda v: f"int {v}", str: lambda v: f"str of len {len(v)}", list: lambda v: f"list with {len(v)} items"}
for value in (42, "hello", [1, 2, 3], 3.14):
    print(handlers.get(type(value), lambda v: f"unhandled {type(v).__name__}")(value))
