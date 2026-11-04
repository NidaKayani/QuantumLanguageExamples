"""Higher-order functions that take and return functions: predicates, combinators, adapters."""


def complement(pred):
    return lambda *args: not pred(*args)


def both(p, q):
    return lambda x: p(x) and q(x)


def either(p, q):
    return lambda x: p(x) or q(x)


def all_of(*preds):
    return lambda x: all(p(x) for p in preds)


def flip(f):
    return lambda a, b: f(b, a)


def twice(f):
    return lambda x: f(f(x))


def iterate(f, n):
    def run(x):
        for _ in range(n):
            x = f(x)
        return x
    return run


def juxt(*fns):
    return lambda x: tuple(f(x) for f in fns)


def memo_counter(f):
    calls = 0

    def wrapped(x):
        nonlocal calls
        calls += 1
        return f(x)

    wrapped.calls = lambda: calls
    return wrapped


is_even = lambda n: n % 2 == 0
is_positive = lambda n: n > 0
is_small = lambda n: abs(n) < 10

nums = list(range(-6, 16, 3))
print("numbers:", nums)
print("odd:", list(filter(complement(is_even), nums)))
print("even and positive:", list(filter(both(is_even, is_positive), nums)))
print("even or small:", list(filter(either(is_even, is_small), nums)))
print("positive, small, even:", list(filter(all_of(is_positive, is_small, is_even), nums)))

power = flip(pow)
print("flip(pow)(2, 10) =", power(2, 10))
subtract_from = flip(lambda a, b: a - b)
print("flip(sub)(3, 10) =", subtract_from(3, 10))

print("twice(+3)(10) =", twice(lambda x: x + 3)(10))
print("twice(twice(*2))(1) =", twice(twice(lambda x: x * 2))(1))
print("iterate collatz step 10x from 27:", iterate(lambda n: n // 2 if n % 2 == 0 else 3 * n + 1, 10)(27))

stats = juxt(min, max, sum, len, lambda xs: sum(xs) / len(xs))
print("juxt(min, max, sum, len, mean):", stats([4, 8, 15, 16, 23, 42]))

counted = memo_counter(str.upper)
words = list(map(counted, ["a", "bb", "ccc"]))
print("counted calls:", words, counted.calls())

ranking = sorted(["pear", "Fig", "apple", "kiwi", "Banana"], key=juxt(len, str.lower))
print("sorted by (len, lower):", ranking)
