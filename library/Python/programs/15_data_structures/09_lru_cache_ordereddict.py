"""An LRU cache built on OrderedDict, compared with functools.lru_cache."""

from collections import OrderedDict
from functools import lru_cache


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data: OrderedDict = OrderedDict()
        self.hits = self.misses = 0

    def get(self, key, default=None):
        if key in self.data:
            self.data.move_to_end(key)
            self.hits += 1
            return self.data[key]
        self.misses += 1
        return default

    def put(self, key, value):
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.capacity:
            evicted, _ = self.data.popitem(last=False)
            print(f"    evict {evicted!r}")

    def __repr__(self):
        return f"LRU({list(self.data.items())})"


cache = LRUCache(3)
ops = [("put", "a", 1), ("put", "b", 2), ("put", "c", 3), ("get", "a"), ("put", "d", 4),
       ("get", "b"), ("get", "c"), ("put", "e", 5), ("put", "c", 33), ("get", "a")]
for op, key, *val in ops:
    if op == "put":
        cache.put(key, val[0])
        print(f"put {key}={val[0]:<3} -> {cache}")
    else:
        print(f"get {key}      -> {cache.get(key)!r:<5} {cache}")
print(f"hits={cache.hits} misses={cache.misses}")

calls = []


@lru_cache(maxsize=2)
def square(n):
    calls.append(n)
    return n * n


for n in [1, 2, 1, 3, 2, 1]:
    square(n)
print("computed for:", calls)
print(square.cache_info())
