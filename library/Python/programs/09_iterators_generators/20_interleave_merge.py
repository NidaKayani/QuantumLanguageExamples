"""Merging sorted streams lazily with heapq.merge and a hand-written round-robin."""
import heapq
from itertools import cycle, islice


def round_robin(*iterables):
    iterators = cycle(iter(it) for it in iterables)
    active = len(iterables)
    while active:
        try:
            for it in iterators:
                yield next(it)
        except StopIteration:
            active -= 1
            iterators = cycle(islice(iterators, active))


def merge_sorted(*streams):
    heap = []
    for idx, stream in enumerate(streams):
        it = iter(stream)
        first = next(it, None)
        if first is not None:
            heap.append((first, idx, it))
    heapq.heapify(heap)
    while heap:
        value, idx, it = heapq.heappop(heap)
        yield value
        nxt = next(it, None)
        if nxt is not None:
            heapq.heappush(heap, (nxt, idx, it))


def multiples(k, limit):
    return (k * i for i in range(1, limit // k + 1))


print("round robin:", list(round_robin("ABC", "D", "EF")))
print("heapq.merge:", list(heapq.merge([1, 4, 9], [2, 3, 10], [5])))
print("custom merge:", list(merge_sorted([1, 4, 9], [2, 3, 10], [5])))
merged = list(merge_sorted(multiples(3, 30), multiples(5, 30), multiples(7, 30)))
print("multiples of 3/5/7 up to 30:", merged)
print("deduplicated:", sorted(set(merged)))
events = heapq.merge([("09:00", "standup"), ("13:00", "review")],
                     [("10:30", "deploy"), ("12:00", "lunch")])
for time, name in events:
    print(f"  {time} {name}")
print("merge descending:", list(heapq.merge([9, 5, 1], [8, 2], reverse=True)))
