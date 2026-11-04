"""Matchstick equations: fix a false equation by moving exactly one stick, using seven-segment digits."""
import re

SEGMENTS = {
    "0": "abcdef", "1": "bc", "2": "abdeg", "3": "abcdg", "4": "bcfg",
    "5": "acdfg", "6": "acdefg", "7": "abc", "8": "abcdefg", "9": "abcdfg",
    "+": "HV", "-": "H", "=": "EE",
}
SHAPES = {frozenset(v): k for k, v in SEGMENTS.items() if k not in "="}


def sticks(ch):
    return len(SEGMENTS[ch])


def transforms(ch):
    """Characters reachable by removing one stick, adding one, or moving one within the symbol."""
    segs = set(SEGMENTS[ch])
    removed, added, moved = set(), set(), set()
    universe = set("abcdefg") if ch.isdigit() else {"H", "V"}
    for s in segs:
        r = SHAPES.get(frozenset(segs - {s}))
        if r:
            removed.add(r)
        for t in universe - segs:
            m = SHAPES.get(frozenset(segs - {s} | {t}))
            if m and m != ch:
                moved.add(m)
    for t in universe - segs:
        a = SHAPES.get(frozenset(segs | {t}))
        if a:
            added.add(a)
    return removed, added, moved


def is_true(eq):
    left, right = eq.split("=")
    if not re.fullmatch(r"\d+([+-]\d+)*", left) or not right.isdigit():
        return False
    return eval_simple(left) == int(right)


def eval_simple(expr):
    return sum(int(tok) for tok in re.findall(r"[+-]?\d+", expr))


def fixes(eq):
    out = set()
    chars = list(eq)
    table = {i: transforms(c) for i, c in enumerate(chars) if c != "="}
    for i, (removed, added, moved) in table.items():
        for m in moved:
            cand = chars[:i] + [m] + chars[i + 1:]
            out.add("".join(cand))
        for r in removed:
            for j, (_, added_j, _) in table.items():
                if j == i:
                    continue
                for a in added_j:
                    cand = chars[:]
                    cand[i], cand[j] = r, a
                    out.add("".join(cand))
    return sorted(c for c in out if is_true(c))


print("Stick counts:", {d: sticks(d) for d in "0123456789"})
print("Transforms of 9 (remove/add/move):", [sorted(x) for x in transforms("9")])
for eq in ["6+4=4", "5+7=2", "3+3=5", "9-5=6", "1+1=3", "8+3=4", "10+10=8"]:
    found = fixes(eq)
    print(f"{eq:<8} -> {', '.join(found) if found else 'no single-move fix'}")
