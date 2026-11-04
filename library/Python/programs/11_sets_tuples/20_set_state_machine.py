"""NFA simulation with sets of states and epsilon closures."""

EPS = ""

# NFA accepting strings over {a, b} that end in "ab" or contain "bb"
TRANSITIONS = {
    (0, EPS): {1, 4},
    (1, "a"): {1, 2}, (1, "b"): {1},
    (2, "b"): {3},
    (4, "a"): {4}, (4, "b"): {4, 5},
    (5, "b"): {6},
    (6, "a"): {6}, (6, "b"): {6},
}
START, ACCEPT = 0, frozenset({3, 6})


def closure(states: set[int]) -> frozenset[int]:
    stack, result = list(states), set(states)
    while stack:
        s = stack.pop()
        for nxt in TRANSITIONS.get((s, EPS), set()) - result:
            result.add(nxt)
            stack.append(nxt)
    return frozenset(result)


def step(states: frozenset[int], symbol: str) -> frozenset[int]:
    moved = set().union(*(TRANSITIONS.get((s, symbol), set()) for s in states))
    return closure(moved)


def accepts(word: str) -> bool:
    current = closure({START})
    for ch in word:
        current = step(current, ch)
        if not current:
            return False
    return bool(current & ACCEPT)


for word in ["ab", "aab", "ba", "bb", "abba", "babab", "aaaa", ""]:
    print(f"{word!r:>8}: {'accept' if accepts(word) else 'reject'}")

# Subset construction: enumerate reachable DFA states
start = closure({START})
seen, queue = {start}, [start]
while queue:
    cur = queue.pop(0)
    for sym in "ab":
        nxt = step(cur, sym)
        if nxt and nxt not in seen:
            seen.add(nxt)
            queue.append(nxt)
print("\nDFA states from subset construction:", len(seen))
for st in sorted(seen, key=lambda s: (len(s), sorted(s))):
    print("  ", sorted(st), "accepting" if st & ACCEPT else "")
