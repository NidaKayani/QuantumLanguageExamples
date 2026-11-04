"""Recursive traversal of nested JSON-like data."""

import json

config = json.loads("""
{
  "service": "api",
  "replicas": 3,
  "env": {"DEBUG": false, "LEVEL": "info", "PORTS": [8080, 8443]},
  "databases": [
    {"name": "users", "host": "db1", "pool": {"min": 2, "max": 10}},
    {"name": "logs", "host": "db2", "pool": {"min": 1, "max": 4}}
  ],
  "features": {"beta": {"enabled": true, "users": ["ann", "bo"]}}
}
""")


def flatten(node, prefix=""):
    if isinstance(node, dict):
        for key, value in node.items():
            yield from flatten(value, f"{prefix}.{key}" if prefix else key)
    elif isinstance(node, list):
        for i, value in enumerate(node):
            yield from flatten(value, f"{prefix}[{i}]")
    else:
        yield prefix, node


def depth(node):
    if isinstance(node, dict):
        return 1 + max((depth(v) for v in node.values()), default=0)
    if isinstance(node, list):
        return 1 + max((depth(v) for v in node), default=0)
    return 0


def find_key(node, wanted):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == wanted:
                yield v
            yield from find_key(v, wanted)
    elif isinstance(node, list):
        for item in node:
            yield from find_key(item, wanted)


def transform(node, fn):
    match node:
        case dict():
            return {k: transform(v, fn) for k, v in node.items()}
        case list():
            return [transform(v, fn) for v in node]
        case _:
            return fn(node)


for path, value in flatten(config):
    print(f"{path:<28} = {value!r}")
print("max depth:", depth(config))
print("all 'name' values:", list(find_key(config, "name")))
print("sum of pool maxima:", sum(p["max"] for p in find_key(config, "pool")))
upper = transform(config["features"], lambda v: v.upper() if isinstance(v, str) else v)
print("uppercased features:", json.dumps(upper, sort_keys=True))
