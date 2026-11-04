"""A hash map with separate chaining and automatic resizing."""

from collections.abc import MutableMapping


class HashMap(MutableMapping):
    def __init__(self, capacity=4, load_factor=0.75):
        self._buckets = [[] for _ in range(capacity)]
        self._size = 0
        self._load = load_factor
        self.resizes = 0

    @staticmethod
    def _hash(key):
        # deterministic polynomial hash for str/int/tuple keys
        if isinstance(key, int):
            return key * 2654435761 & 0xFFFFFFFF
        if isinstance(key, tuple):
            h = 7
            for part in key:
                h = (h * 31 + HashMap._hash(part)) & 0xFFFFFFFF
            return h
        h = 0
        for ch in str(key):
            h = (h * 131 + ord(ch)) & 0xFFFFFFFF
        return h

    def _bucket(self, key):
        return self._buckets[self._hash(key) % len(self._buckets)]

    def __setitem__(self, key, value):
        bucket = self._bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1
        if self._size > self._load * len(self._buckets):
            self._resize(len(self._buckets) * 2)

    def __getitem__(self, key):
        for k, v in self._bucket(key):
            if k == key:
                return v
        raise KeyError(key)

    def __delitem__(self, key):
        bucket = self._bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return
        raise KeyError(key)

    def _resize(self, new_cap):
        items = [pair for b in self._buckets for pair in b]
        self._buckets = [[] for _ in range(new_cap)]
        self._size = 0
        self.resizes += 1
        for k, v in items:
            self[k] = v

    def __iter__(self):
        for bucket in self._buckets:
            for k, _ in bucket:
                yield k

    def __len__(self):
        return self._size

    def stats(self):
        lengths = [len(b) for b in self._buckets]
        return {"buckets": len(lengths), "size": self._size, "longest_chain": max(lengths), "resizes": self.resizes}


m = HashMap()
for word in "the quick brown fox jumps over the lazy dog the end".split():
    m[word] = m.get(word, 0) + 1
print("word counts:", dict(sorted(m.items())))
print("stats:", m.stats())
m[(1, 2)] = "tuple key"
m[42] = "int key"
print("m[(1, 2)] =", m[(1, 2)], "| m[42] =", m[42], "| 'fox' in m:", "fox" in m)
del m["fox"]
print("after delete, 'fox' in m:", "fox" in m, "len:", len(m))
try:
    m["missing"]
except KeyError as exc:
    print("KeyError:", exc)
m.update({"x": 1, "y": 2})
print("keys sorted by str:", sorted(map(str, m.keys())))
