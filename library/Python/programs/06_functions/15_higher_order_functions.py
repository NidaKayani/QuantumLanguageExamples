"""Higher-order functions: composing, piping, and returning functions."""
from functools import reduce


def compose(*funcs):
    def composed(x):
        return reduce(lambda acc, f: f(acc), reversed(funcs), x)
    return composed


def pipe(value, *funcs):
    for f in funcs:
        value = f(value)
    return value


def apply_n(func, n):
    def run(x):
        for _ in range(n):
            x = func(x)
        return x
    return run


def flip(func):
    return lambda a, b: func(b, a)


def tally(predicate):
    def count(items):
        return sum(1 for item in items if predicate(item))
    return count


inc = lambda x: x + 1
dbl = lambda x: x * 2
sq = lambda x: x ** 2

print("compose(sq, dbl, inc)(3) =", compose(sq, dbl, inc)(3))
print("pipe(3, inc, dbl, sq) =", pipe(3, inc, dbl, sq))
print("apply_n(dbl, 10)(1) =", apply_n(dbl, 10)(1))

subtract = lambda a, b: a - b
print("subtract(10, 3) =", subtract(10, 3), "flipped =", flip(subtract)(10, 3))

count_vowels = tally(lambda ch: ch in "aeiou")
print("vowels in 'functional programming':", count_vowels("functional programming"))

clean = compose(str.title, str.strip, lambda s: s.replace("_", " "))
for raw in ["  hello_world ", "quantum_language_compiler"]:
    print(repr(raw), "->", repr(clean(raw)))

print("map with builtin:", list(map(abs, [-3, 4, -5])))
print("sorted by function result:", sorted([-7, 2, -1, 5], key=abs))
