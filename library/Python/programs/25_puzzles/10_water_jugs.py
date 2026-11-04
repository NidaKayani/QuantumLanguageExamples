"""Water jug puzzles solved by BFS over (a, b, ...) volume states, with a gcd solvability check."""
from collections import deque
from functools import reduce
from math import gcd


def moves(state, caps):
    n = len(state)
    for i in range(n):
        if state[i] < caps[i]:
            yield f"fill {caps[i]}L", state[:i] + (caps[i],) + state[i + 1:]
        if state[i] > 0:
            yield f"empty {caps[i]}L", state[:i] + (0,) + state[i + 1:]
        for j in range(n):
            if i != j and state[i] > 0 and state[j] < caps[j]:
                amount = min(state[i], caps[j] - state[j])
                s = list(state)
                s[i] -= amount
                s[j] += amount
                yield f"pour {caps[i]}L->{caps[j]}L", tuple(s)


def solve(caps, target, start=None, allow_fill=True):
    start = start or tuple(0 for _ in caps)
    prev = {start: None}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        if target in state:
            steps = []
            while prev[state]:
                action, before = prev[state]
                steps.append((action, state))
                state = before
            return steps[::-1]
        for action, nxt in moves(state, caps):
            if not allow_fill and not action.startswith("pour"):
                continue
            if nxt not in prev:
                prev[nxt] = (action, state)
                queue.append(nxt)
    return None


cases = [((3, 5), 4, None, True), ((4, 9), 6, None, True), ((6, 9), 4, None, True),
         ((8, 5, 3), 4, (8, 0, 0), False), ((12, 7, 5), 6, (12, 0, 0), False)]
for caps, target, start, allow_fill in cases:
    feasible = target % reduce(gcd, caps) == 0 and target <= max(caps)
    label = f"jugs {caps}, measure {target}L" + ("" if allow_fill else f", pour only from {start}")
    steps = solve(caps, target, start, allow_fill)
    if steps is None:
        print(f"{label}: impossible (gcd test says {'possible' if feasible else 'impossible'})")
        continue
    print(f"{label}: {len(steps)} steps")
    for action, state in steps:
        print(f"    {action:<14} -> {state}")
