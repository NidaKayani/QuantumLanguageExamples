"""Compare LRU, FIFO and LFU cache eviction policies on the same access trace."""
from abc import ABC, abstractmethod
from collections import OrderedDict, Counter, deque


class Cache(ABC):
    def __init__(self, capacity):
        self.capacity = capacity
        self.hits = self.misses = 0

    def access(self, key):
        if self.contains(key):
            self.hits += 1
            self.touch(key)
        else:
            self.misses += 1
            if self.size() >= self.capacity:
                self.evict()
            self.insert(key)

    @abstractmethod
    def contains(self, key): ...
    @abstractmethod
    def touch(self, key): ...
    @abstractmethod
    def evict(self): ...
    @abstractmethod
    def insert(self, key): ...
    @abstractmethod
    def size(self): ...


class LRU(Cache):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.data = OrderedDict()
    def contains(self, key): return key in self.data
    def touch(self, key): self.data.move_to_end(key)
    def evict(self): self.data.popitem(last=False)
    def insert(self, key): self.data[key] = True
    def size(self): return len(self.data)


class FIFO(Cache):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.order, self.keys = deque(), set()
    def contains(self, key): return key in self.keys
    def touch(self, key): pass
    def evict(self): self.keys.remove(self.order.popleft())
    def insert(self, key): self.order.append(key); self.keys.add(key)
    def size(self): return len(self.keys)


class LFU(Cache):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.freq, self.clock, self.last = Counter(), 0, {}
    def contains(self, key): return key in self.last
    def touch(self, key):
        self.freq[key] += 1
        self.clock += 1
        self.last[key] = self.clock
    def evict(self):
        victim = min(self.last, key=lambda k: (self.freq[k], self.last[k]))
        del self.last[victim], self.freq[victim]
    def insert(self, key): self.touch(key)
    def size(self): return len(self.last)


def trace(n=600, seed=17):
    x = seed
    for i in range(n):
        x = (x * 214013 + 2531011) % 2**32
        r = (x >> 16) % 100
        yield r % 5 if r < 60 else (i // 7) % 30 + 5 if r < 90 else r


print(f"{'capacity':>8} " + " ".join(f"{cls.__name__:>8}" for cls in (LRU, FIFO, LFU)))
for capacity in (4, 8, 16, 32):
    rates = []
    for cls in (LRU, FIFO, LFU):
        cache = cls(capacity)
        for key in trace():
            cache.access(key)
        rates.append(cache.hits / (cache.hits + cache.misses))
    print(f"{capacity:>8} " + " ".join(f"{r:>8.1%}" for r in rates))
