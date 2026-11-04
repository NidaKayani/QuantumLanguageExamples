"""A priority queue on heapq with insertion order tie-breaks and lazy removal."""

import heapq
import itertools


class PriorityQueue:
    REMOVED = "<removed>"

    def __init__(self):
        self._heap = []
        self._entries = {}
        self._counter = itertools.count()

    def push(self, task, priority=0):
        if task in self._entries:
            self.remove(task)
        entry = [priority, next(self._counter), task]
        self._entries[task] = entry
        heapq.heappush(self._heap, entry)

    def remove(self, task):
        entry = self._entries.pop(task)
        entry[-1] = self.REMOVED

    def pop(self):
        while self._heap:
            priority, _, task = heapq.heappop(self._heap)
            if task is not self.REMOVED:
                del self._entries[task]
                return task, priority
        raise KeyError("pop from empty priority queue")

    def __len__(self):
        return len(self._entries)


pq = PriorityQueue()
for task, prio in [("write tests", 2), ("fix prod bug", 0), ("refactor", 3),
                   ("code review", 2), ("deploy", 1), ("lunch", 2)]:
    pq.push(task, prio)
pq.push("refactor", 1)   # reprioritise
pq.remove("lunch")
print("tasks queued:", len(pq))
while pq:
    task, prio = pq.pop()
    print(f"  p{prio}: {task}")

nums = [9, 4, 7, 1, 8, 2]
heapq.heapify(nums)
print("heapified:", nums)
heapq.heappush(nums, 0)
print("pushpop(5):", heapq.heappushpop(nums, 5), "replace(6):", heapq.heapreplace(nums, 6))
print("drain:", [heapq.heappop(nums) for _ in range(len(nums))])

maxheap = []
for x in [3, 10, 1, 7]:
    heapq.heappush(maxheap, -x)
print("max-heap via negation:", [-heapq.heappop(maxheap) for _ in range(len(maxheap))])
