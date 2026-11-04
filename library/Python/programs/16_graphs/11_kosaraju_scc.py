"""Kosaraju's two-pass algorithm for strongly connected components on a call graph."""
from collections import defaultdict

CALLS = [
    ("main", "parse"), ("parse", "lex"), ("lex", "parse"), ("parse", "eval"),
    ("eval", "apply"), ("apply", "eval"), ("apply", "lookup"),
    ("eval", "lookup"), ("lookup", "hash"), ("main", "report"),
    ("report", "format"), ("format", "report"), ("report", "hash"),
]


def build(edges):
    forward, backward = defaultdict(list), defaultdict(list)
    nodes = []
    for a, b in edges:
        forward[a].append(b)
        backward[b].append(a)
        for n in (a, b):
            if n not in nodes:
                nodes.append(n)
    return nodes, forward, backward


def kosaraju(nodes, forward, backward):
    visited, finish = set(), []
    for start in nodes:
        if start in visited:
            continue
        stack = [(start, iter(forward[start]))]
        visited.add(start)
        while stack:
            node, it = stack[-1]
            for nxt in it:
                if nxt not in visited:
                    visited.add(nxt)
                    stack.append((nxt, iter(forward[nxt])))
                    break
            else:
                stack.pop()
                finish.append(node)
    assigned = {}
    components = []
    for node in reversed(finish):
        if node in assigned:
            continue
        comp, stack = [], [node]
        assigned[node] = len(components)
        while stack:
            cur = stack.pop()
            comp.append(cur)
            for prev in backward[cur]:
                if prev not in assigned:
                    assigned[prev] = len(components)
                    stack.append(prev)
        components.append(sorted(comp))
    return components


def main():
    nodes, forward, backward = build(CALLS)
    comps = kosaraju(nodes, forward, backward)
    print("Functions:", ", ".join(nodes))
    print("Strongly connected groups in topological order:")
    for comp in comps:
        tag = "recursive group" if len(comp) > 1 else "single"
        print(f"  {comp!s:<22} {tag}")
    mutual = [c for c in comps if len(c) > 1]
    print("Mutually recursive sets:", len(mutual))
    largest = max(comps, key=len)
    print("Largest group:", largest)


if __name__ == "__main__":
    main()
