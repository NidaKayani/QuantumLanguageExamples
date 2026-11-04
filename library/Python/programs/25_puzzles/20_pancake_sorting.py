"""Pancake sorting: greedy flips versus optimal BFS, and the hardest stacks for small sizes."""
from collections import deque
from itertools import permutations


def flip(stack, k):
    """Reverse the top k pancakes (index 0 is the top)."""
    return stack[:k][::-1] + stack[k:]


def greedy(stack):
    stack = list(stack)
    flips = []
    for size in range(len(stack), 1, -1):
        biggest = stack.index(max(stack[:size]))
        if biggest == size - 1:
            continue
        if biggest != 0:
            stack = flip(stack, biggest + 1)
            flips.append(biggest + 1)
        stack = flip(stack, size)
        flips.append(size)
    return flips, stack


def optimal_distances(n):
    """BFS from the sorted stack; flips are self-inverse so distances are symmetric."""
    goal = tuple(range(1, n + 1))
    dist = {goal: 0}
    queue = deque([goal])
    while queue:
        s = queue.popleft()
        for k in range(2, n + 1):
            t = flip(s, k)
            if t not in dist:
                dist[t] = dist[s] + 1
                queue.append(t)
    return dist


def draw(stack):
    width = max(stack)
    return "\n".join(("=" * (2 * p - 1)).center(2 * width + 1) for p in stack)


stack = [3, 6, 1, 5, 2, 4]
flips, result = greedy(stack)
print("Stack (top first):", stack)
print(draw(stack))
print("Greedy flips:", flips, "->", result, f"({len(flips)} flips)")

current = stack
for k in flips:
    current = flip(current, k)
    print(f"  flip top {k}: {current}")

for n in range(3, 8):
    dist = optimal_distances(n)
    worst = max(dist.values())
    hardest = sorted(s for s, d in dist.items() if d == worst)
    greedy_total = sum(len(greedy(p)[0]) for p in permutations(range(1, n + 1)))
    optimal_total = sum(dist.values())
    print(f"n={n}: max flips needed {worst} (e.g. {hardest[0]}, {len(hardest)} such stacks); "
          f"greedy avg {greedy_total / len(dist):.2f} vs optimal avg {optimal_total / len(dist):.2f}")
