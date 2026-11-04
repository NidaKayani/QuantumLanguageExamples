"""A bitset backed by a Python int and a Bloom filter built on top of it."""


class BitSet:
    def __init__(self, size):
        self.size = size
        self.bits = 0

    def set(self, i):
        self.bits |= 1 << i

    def clear(self, i):
        self.bits &= ~(1 << i)

    def test(self, i):
        return bool(self.bits >> i & 1)

    def count(self):
        return bin(self.bits).count("1")

    def __or__(self, other):
        out = BitSet(max(self.size, other.size))
        out.bits = self.bits | other.bits
        return out

    def __and__(self, other):
        out = BitSet(max(self.size, other.size))
        out.bits = self.bits & other.bits
        return out

    def __str__(self):
        return format(self.bits, f"0{self.size}b")[::-1]


def fnv1a(text, seed):
    h = 2166136261 ^ seed
    for byte in text.encode():
        h = ((h ^ byte) * 16777619) & 0xFFFFFFFF
    return h


class BloomFilter:
    def __init__(self, size=64, hashes=3):
        self.bits = BitSet(size)
        self.size, self.hashes = size, hashes

    def _positions(self, item):
        return [fnv1a(item, seed) % self.size for seed in range(self.hashes)]

    def add(self, item):
        for p in self._positions(item):
            self.bits.set(p)

    def __contains__(self, item):
        return all(self.bits.test(p) for p in self._positions(item))


a, b = BitSet(16), BitSet(16)
for i in (1, 3, 5, 7, 9):
    a.set(i)
for i in (3, 4, 5, 6):
    b.set(i)
print("a     :", a, "count", a.count())
print("b     :", b, "count", b.count())
print("a | b :", a | b)
print("a & b :", a & b)
a.clear(3)
print("a without 3:", a, "test(3):", a.test(3))

bloom = BloomFilter(size=24, hashes=3)
members = ["apple", "banana", "cherry", "date", "elderberry"]
for m in members:
    bloom.add(m)
print("all members found:", all(m in bloom for m in members))
probes = ["fig", "grape", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya"]
false_pos = [p for p in probes if p in bloom]
print("non-members reported present (false positives):", false_pos)
print("bits set:", bloom.bits.count(), "of", bloom.size)
