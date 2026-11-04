"""A fixed-capacity circular buffer (ring buffer) with overwrite support."""


class RingBuffer:
    def __init__(self, capacity, overwrite=True):
        self._data = [None] * capacity
        self._head = 0      # index of oldest element
        self._count = 0
        self.overwrite = overwrite

    @property
    def capacity(self):
        return len(self._data)

    def push(self, item):
        tail = (self._head + self._count) % self.capacity
        if self._count == self.capacity:
            if not self.overwrite:
                raise OverflowError("buffer full")
            self._data[tail] = item
            self._head = (self._head + 1) % self.capacity
        else:
            self._data[tail] = item
            self._count += 1

    def pop(self):
        if not self._count:
            raise IndexError("buffer empty")
        item = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self.capacity
        self._count -= 1
        return item

    def __iter__(self):
        for i in range(self._count):
            yield self._data[(self._head + i) % self.capacity]

    def __len__(self):
        return self._count

    def __getitem__(self, i):
        if not -self._count <= i < self._count:
            raise IndexError("index out of range")
        return self._data[(self._head + i % self._count) % self.capacity]

    def __repr__(self):
        return f"RingBuffer({list(self)}, raw={self._data}, head={self._head})"


rb = RingBuffer(4)
for x in range(1, 7):
    rb.push(x)
    print(f"push {x}: {rb}")
print("oldest:", rb[0], "newest:", rb[-1])
print("pop:", rb.pop(), rb.pop(), "->", list(rb))

strict = RingBuffer(2, overwrite=False)
strict.push("a")
strict.push("b")
try:
    strict.push("c")
except OverflowError as exc:
    print("strict buffer:", exc)

readings = [20, 22, 21, 25, 30, 28, 27, 35, 33]
window = RingBuffer(3)
averages = []
for r in readings:
    window.push(r)
    averages.append(round(sum(window) / len(window), 2))
print("moving averages (3):", averages)
