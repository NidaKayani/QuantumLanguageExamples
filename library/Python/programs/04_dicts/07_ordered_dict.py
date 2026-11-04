"""Use OrderedDict for ordering operations and to build an LRU cache."""

from collections import OrderedDict

od = OrderedDict()
od["first"] = 1
od["second"] = 2
od["third"] = 3
print("start:", list(od.items()))

od.move_to_end("first")
print("move first to end:", list(od))
od.move_to_end("third", last=False)
print("move third to front:", list(od))

print("popitem last:", od.popitem())
print("popitem first:", od.popitem(last=False))
print("remaining:", od)

# order matters for OrderedDict equality but not for dict
a = OrderedDict([("x", 1), ("y", 2)])
b = OrderedDict([("y", 2), ("x", 1)])
print("OrderedDict equal:", a == b, "| as dicts:", dict(a) == dict(b))


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = OrderedDict()
        self.hits = self.misses = 0

    def get(self, key):
        if key in self.data:
            self.data.move_to_end(key)
            self.hits += 1
            return self.data[key]
        self.misses += 1
        return None

    def put(self, key, value):
        self.data[key] = value
        self.data.move_to_end(key)
        if len(self.data) > self.capacity:
            evicted, _ = self.data.popitem(last=False)
            print(f"  evicted {evicted}")


cache = LRUCache(3)
for k in "abc":
    cache.put(k, k.upper())
cache.get("a")
cache.put("d", "D")
cache.get("b")
cache.put("e", "E")
print("cache order:", list(cache.data), "hits:", cache.hits, "misses:", cache.misses)
