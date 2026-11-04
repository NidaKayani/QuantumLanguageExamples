"""Abstract base classes for containers, with two interchangeable implementations."""

from abc import ABC, abstractmethod
from collections.abc import Sequence


class Bag(ABC):
    @abstractmethod
    def add(self, item): ...

    @abstractmethod
    def __iter__(self): ...

    def __len__(self):
        return sum(1 for _ in self)

    def count(self, item):
        return sum(1 for x in self if x == item)

    def describe(self):
        return f"{type(self).__name__} with {len(self)} items: {sorted(self)}"


class ArrayBag(Bag):
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)


class LinkedBag(Bag):
    def __init__(self):
        self._head = None

    def add(self, item):
        self._head = (item, self._head)

    def __iter__(self):
        node = self._head
        while node:
            yield node[0]
            node = node[1]


class Range2(Sequence):
    """A Sequence implemented via __getitem__/__len__ gets index, count, in, reversed free."""
    def __init__(self, start, stop, step=1):
        self.start, self.stop, self.step = start, stop, step

    def __len__(self):
        return max(0, (self.stop - self.start + self.step - 1) // self.step)

    def __getitem__(self, i):
        if isinstance(i, slice):
            return [self[j] for j in range(*i.indices(len(self)))]
        if i < 0:
            i += len(self)
        if not 0 <= i < len(self):
            raise IndexError("Range2 index out of range")
        return self.start + i * self.step


for cls in (ArrayBag, LinkedBag):
    bag = cls()
    for word in "to be or not to be".split():
        bag.add(word)
    print(bag.describe(), "| count('be') =", bag.count("be"))

try:
    Bag()
except TypeError as exc:
    print("cannot instantiate abstract class:", "abstract" in str(exc))

r = Range2(3, 20, 4)
print("Range2:", list(r), "len", len(r), "r[-1]", r[-1], "r[1:3]", r[1:3])
print("index(11):", r.index(11), "15 in r:", 15 in r, "reversed:", list(reversed(r)))
print("isinstance Sequence:", isinstance(r, Sequence))
