"""Controlling generators from outside with throw(), close(), and try/finally cleanup."""


class Reset(Exception):
    pass


def counter(start=0):
    value = start
    try:
        while True:
            try:
                yield value
                value += 1
            except Reset:
                print("  counter reset requested")
                value = start
    finally:
        print(f"  cleanup: counter stopped at {value}")


def resource(name):
    print(f"  open {name}")
    try:
        yield f"{name}-handle"
        yield f"{name}-more"
    finally:
        print(f"  close {name}")


c = counter(10)
print("values:", next(c), next(c), next(c))
print("after throw(Reset):", c.throw(Reset))
print("continue:", next(c))
c.close()
print("closed; next() gives:", next(c, "StopIteration"))

r = resource("db")
print("first:", next(r))
r.close()

r2 = resource("cache")
for item in r2:
    print("  item", item)

g = counter()
next(g)
try:
    g.throw(ValueError("bad state"))
except ValueError as exc:
    print("propagated out of generator:", exc)
