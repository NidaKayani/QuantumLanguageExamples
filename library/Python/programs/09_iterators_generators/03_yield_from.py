"""Delegating to sub-generators with yield from, including return values."""


def walk(tree, depth=0):
    """Yield (depth, name) pairs from a nested dict tree."""
    for name, children in tree.items():
        yield depth, name
        yield from walk(children, depth + 1)


def averager():
    total = count = 0
    while True:
        value = yield
        if value is None:
            return total / count if count else 0
        total += value
        count += 1


def collect_averages(results, key):
    results[key] = yield from averager()


def chain(*iterables):
    for it in iterables:
        yield from it


filesystem = {
    "src": {"main.py": {}, "utils": {"io.py": {}, "math.py": {}}},
    "tests": {"test_main.py": {}},
    "README.md": {},
}
for depth, name in walk(filesystem):
    print("  " * depth + name)

print("chain:", list(chain([1, 2], "ab", range(3))))

results = {}
for key, values in {"math": [90, 80, 70], "art": [100, 95], "none": []}.items():
    coro = collect_averages(results, key)
    next(coro)
    for v in values:
        coro.send(v)
    try:
        coro.send(None)
    except StopIteration:
        pass
print("averages:", results)


def gen_with_return():
    yield "a"
    return "the result"

g = gen_with_return()
next(g)
try:
    next(g)
except StopIteration as stop:
    print("StopIteration.value:", stop.value)
