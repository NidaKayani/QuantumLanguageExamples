"""Immutability patterns: namedtuple _replace, tuples, frozensets and persistent-style updates."""
from collections import namedtuple
from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float

    def moved(self, dx, dy):
        return self._replace(x=self.x + dx, y=self.y + dy)


Config = namedtuple("Config", "host port debug tags", defaults=("localhost", 8080, False, frozenset()))

p = Point(1, 2)
q = p.moved(3, -1)
print("original:", p, "moved:", q, "same object:", p is q)
try:
    p.x = 10
except AttributeError as exc:
    print("cannot mutate:", exc)

base = Config()
dev = base._replace(debug=True, tags=base.tags | {"dev"})
prod = base._replace(host="example.org", port=443, tags=frozenset({"prod", "tls"}))
for name, cfg in (("base", base), ("dev", dev), ("prod", prod)):
    print(f"{name:>4}: host={cfg.host} port={cfg.port} debug={cfg.debug} tags={sorted(cfg.tags)}")
print("as dict:", dev._asdict())


def assoc(mapping, key, value):
    return {**mapping, key: value}


def dissoc(mapping, key):
    return {k: v for k, v in mapping.items() if k != key}


def update_in(mapping, path, fn):
    head, *rest = path
    new_value = update_in(mapping[head], rest, fn) if rest else fn(mapping[head])
    return assoc(mapping, head, new_value)


state = {"user": {"name": "ann", "visits": 1}, "cart": ("apple",)}
s1 = update_in(state, ["user", "visits"], lambda v: v + 1)
s2 = assoc(s1, "cart", s1["cart"] + ("pear",))
s3 = dissoc(s2, "user")
print("state :", state)
print("s1    :", s1)
print("s2    :", s2)
print("s3    :", s3)
print("shared untouched branch:", s1["cart"] is state["cart"])

history = [(0, 0)]
for move in [(1, 0), (0, 2), (-1, 1)]:
    last = history[-1]
    history = history + [(last[0] + move[0], last[1] + move[1])]
print("tuple history:", tuple(history))
print("hashable as keys:", {Point(0, 0): "origin", q: "q"}[Point(4, 1)])
