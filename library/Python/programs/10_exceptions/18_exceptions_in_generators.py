"""How exceptions interact with generators, comprehensions, and StopIteration."""


def numbers(items):
    for item in items:
        try:
            yield int(item)
        except ValueError:
            print(f"  skipping bad item {item!r}")


def strict_numbers(items):
    for item in items:
        yield int(item)


def guarded(gen):
    try:
        yield from gen
    except ValueError as exc:
        print(f"  generator aborted: {exc}")
        yield -1


raw = ["1", "2", "x", "4", "five", "6"]
print("tolerant:", list(numbers(raw)))
print("guarded strict:", list(guarded(strict_numbers(raw))))

try:
    total = sum(strict_numbers(raw))
except ValueError as exc:
    print("sum failed:", exc)


def bad_generator():
    yield 1
    raise StopIteration("manual stop")


try:
    list(bad_generator())
except RuntimeError as exc:
    print("RuntimeError:", exc, "| cause:", type(exc.__cause__).__name__)

it = iter([10, 20])
collected = []
while True:
    try:
        collected.append(next(it))
    except StopIteration:
        break
print("manual loop collected:", collected)

safe = [x for x in (int(s) if s.isdigit() else None for s in raw) if x is not None]
print("comprehension filter instead of try:", safe)
