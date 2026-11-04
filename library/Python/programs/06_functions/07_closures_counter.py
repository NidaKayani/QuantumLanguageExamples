"""Closures that capture state: counters, accumulators, and late-binding behavior."""


def make_counter(start=0, step=1):
    count = start

    def increment():
        nonlocal count
        count += step
        return count

    return increment


def make_averager():
    values = []

    def add(value):
        values.append(value)
        return sum(values) / len(values)

    return add


def multiplier_factory(n):
    return lambda x: x * n


c1 = make_counter()
c2 = make_counter(100, 10)
print([c1() for _ in range(5)])
print([c2() for _ in range(3)])
print("c1 again:", c1())

avg = make_averager()
for v in [10, 20, 30, 40]:
    print(f"added {v}: running average = {avg(v)}")

print("free vars:", avg.__code__.co_freevars)
print("cell contents:", avg.__closure__[0].cell_contents)

late = [lambda: i for i in range(3)]
print("late binding:", [f() for f in late])
early = [lambda i=i: i for i in range(3)]
print("default capture:", [f() for f in early])

double, triple = multiplier_factory(2), multiplier_factory(3)
print("double(7) =", double(7), "triple(7) =", triple(7))
