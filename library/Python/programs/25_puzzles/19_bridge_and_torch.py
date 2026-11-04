"""Bridge and torch puzzle solved with Dijkstra's algorithm over (near-side, torch-side) states."""
import heapq
from itertools import combinations


def solve(times, capacity=2):
    people = frozenset(range(len(times)))
    start = (people, True)  # everyone on near side, torch near
    dist = {start: 0}
    prev = {}
    heap = [(0, 0, start)]
    counter = 1
    while heap:
        cost, _, state = heapq.heappop(heap)
        near, torch_near = state
        if not near:
            plan = []
            while state in prev:
                state, move = prev[state]
                plan.append(move)
            return cost, plan[::-1]
        if cost > dist[state]:
            continue
        side = near if torch_near else people - near
        for k in range(1, capacity + 1):
            for group in combinations(sorted(side), k):
                step = max(times[p] for p in group)
                new_near = near - set(group) if torch_near else near | set(group)
                nxt = (frozenset(new_near), not torch_near)
                if cost + step < dist.get(nxt, float("inf")):
                    dist[nxt] = cost + step
                    prev[nxt] = (state, (group, torch_near, step))
                    heapq.heappush(heap, (cost + step, counter, nxt))
                    counter += 1
    return None


def describe(times, plan, names):
    for group, forward, step in plan:
        who = " & ".join(names[p] for p in group)
        print(f"    {'cross ' if forward else 'return'} {who:<14} {step:>3} min")


names = ["Ann", "Ben", "Cat", "Dan", "Eve"]
for times in [(1, 2, 5, 10), (1, 2, 5, 8), (1, 3, 4, 5, 8), (2, 2, 2, 2)]:
    total, plan = solve(times)
    labelled = {i: f"{names[i]}({t})" for i, t in enumerate(times)}
    print(f"Crossing times {times}: optimal {total} minutes in {len(plan)} trips")
    describe(times, plan, labelled)

total, plan = solve((1, 2, 5, 10, 12, 15), capacity=3)
print(f"Six people, bridge holds three: {total} minutes, {len(plan)} trips")
