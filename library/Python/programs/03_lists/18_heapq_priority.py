"""Use heapq to maintain priority queues and find smallest and largest items."""

import heapq

nums = [29, 3, 17, 8, 42, 1, 23, 11]
heap = nums[:]
heapq.heapify(heap)
print("heap[0] (smallest):", heap[0])
print("3 smallest:", heapq.nsmallest(3, nums))
print("3 largest:", heapq.nlargest(3, nums))

ordered = [heapq.heappop(heap) for _ in range(len(heap))]
print("heap sort:", ordered)

# priority queue of tasks
tasks = []
heapq.heappush(tasks, (3, "write report"))
heapq.heappush(tasks, (1, "fix outage"))
heapq.heappush(tasks, (2, "review PR"))
heapq.heappush(tasks, (1, "call customer"))
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"  p{priority}: {task}")

# merge sorted lists lazily
a, b, c = [1, 4, 9], [2, 3, 10], [0, 5, 6, 7]
print("merged:", list(heapq.merge(a, b, c)))

# running median with two heaps
low, high = [], []
medians = []
for x in [5, 15, 1, 3, 8, 7, 9, 10]:
    heapq.heappush(low, -x)
    heapq.heappush(high, -heapq.heappop(low))
    if len(high) > len(low):
        heapq.heappush(low, -heapq.heappop(high))
    medians.append(-low[0] if len(low) > len(high) else (-low[0] + high[0]) / 2)
print("running medians:", medians)

products = [("laptop", 999), ("mouse", 25), ("monitor", 199), ("cable", 9)]
print("cheapest two:", heapq.nsmallest(2, products, key=lambda p: p[1]))
print("pushpop:", heapq.heappushpop([4, 6, 8], 5))
