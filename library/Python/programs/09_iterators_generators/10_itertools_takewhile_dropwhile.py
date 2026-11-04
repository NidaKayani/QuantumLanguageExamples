"""Predicate-driven slicing with takewhile, dropwhile, filterfalse, and compress."""
from itertools import takewhile, dropwhile, filterfalse, compress, count

nums = [2, 4, 6, 7, 8, 10, 3]
print("takewhile even:", list(takewhile(lambda n: n % 2 == 0, nums)))
print("dropwhile even:", list(dropwhile(lambda n: n % 2 == 0, nums)))
print("filter even:", list(filter(lambda n: n % 2 == 0, nums)))
print("filterfalse even:", list(filterfalse(lambda n: n % 2 == 0, nums)))

log = """# config file
# generated
host=example.org
port=8080
# trailing comment
debug=true""".splitlines()
body = list(dropwhile(lambda line: line.startswith("#"), log))
print("after header:", body)
settings = dict(line.split("=") for line in body if not line.startswith("#"))
print("settings:", settings)

triangular = (n * (n + 1) // 2 for n in count(1))
print("triangular numbers < 60:", list(takewhile(lambda t: t < 60, triangular)))

names = ["ann", "bob", "cid", "dee", "eve"]
present = [1, 0, 1, 1, 0]
print("compress:", list(compress(names, present)))
print("absent:", list(compress(names, (not p for p in present))))
