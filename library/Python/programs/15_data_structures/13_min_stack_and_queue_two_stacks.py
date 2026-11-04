"""Classic composite structures: a min-stack and a queue made of two stacks."""


class MinStack:
    def __init__(self):
        self._items = []   # (value, current_min)

    def push(self, x):
        current_min = min(x, self._items[-1][1]) if self._items else x
        self._items.append((x, current_min))

    def pop(self):
        return self._items.pop()[0]

    def top(self):
        return self._items[-1][0]

    def min(self):
        return self._items[-1][1]

    def __len__(self):
        return len(self._items)


class TwoStackQueue:
    def __init__(self):
        self._in, self._out = [], []
        self.transfers = 0

    def enqueue(self, x):
        self._in.append(x)

    def dequeue(self):
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())
                self.transfers += 1
        if not self._out:
            raise IndexError("dequeue from empty queue")
        return self._out.pop()

    def __len__(self):
        return len(self._in) + len(self._out)


ms = MinStack()
for x in [5, 3, 7, 3, 2, 8]:
    ms.push(x)
    print(f"push {x}: top={ms.top()} min={ms.min()}")
while len(ms) > 1:
    popped = ms.pop()
    print(f"pop {popped}: min now {ms.min()}")

q = TwoStackQueue()
for x in "ABC":
    q.enqueue(x)
out = [q.dequeue()]
q.enqueue("D")
q.enqueue("E")
while len(q):
    out.append(q.dequeue())
print("queue order:", "".join(out), "| element transfers:", q.transfers)
try:
    q.dequeue()
except IndexError as exc:
    print("error:", exc)
