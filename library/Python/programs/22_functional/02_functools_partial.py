"""Using functools.partial to specialize functions, builtins and callbacks."""
from functools import partial


def power(base, exponent):
    return base ** exponent


def log(message, *, level="INFO", prefix=""):
    return f"[{level}] {prefix}{message}"


square = partial(power, exponent=2)
cube = partial(power, exponent=3)
two_to = partial(power, 2)

print("squares:", [square(n) for n in range(1, 7)])
print("cubes:", list(map(cube, range(1, 6))))
print("powers of two:", [two_to(n) for n in range(11)])

warn = partial(log, level="WARN")
db_error = partial(log, level="ERROR", prefix="db: ")
print(warn("disk almost full"))
print(db_error("connection lost"))
print(db_error("overridden", level="FATAL"))

parse_binary = partial(int, base=2)
parse_hex = partial(int, base=16)
print("binary:", [parse_binary(s) for s in ("101", "1111", "100000")])
print("hex:", [parse_hex(s) for s in ("ff", "1A", "beef")])

join_csv = partial(str.join, ",")
print("csv:", join_csv(["a", "b", "c"]))

sort_desc = partial(sorted, reverse=True)
by_len = partial(sorted, key=len)
words = ["kiwi", "banana", "fig", "cherry", "apple"]
print("desc:", sort_desc(words))
print("by length:", by_len(words))

print("partial introspection:", db_error.func.__name__, db_error.args, sorted(db_error.keywords.items()))


def apply_discount(rate, price):
    return round(price * (1 - rate), 2)


discounts = {name: partial(apply_discount, rate) for name, rate in
             [("member", 0.10), ("staff", 0.25), ("clearance", 0.50)]}
for name, fn in discounts.items():
    print(f"{name:>9}: {[fn(p) for p in (10, 19.99, 100)]}")
