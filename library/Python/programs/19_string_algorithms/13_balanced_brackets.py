"""Balanced bracket checking with error positions, minimum fixes, and generation."""
from dataclasses import dataclass
from typing import Optional

PAIRS = {")": "(", "]": "[", "}": "{", ">": "<"}
OPENERS = set(PAIRS.values())


@dataclass
class Result:
    ok: bool
    position: Optional[int] = None
    message: str = "balanced"


def check(text):
    stack = []
    for i, ch in enumerate(text):
        if ch in OPENERS:
            stack.append((ch, i))
        elif ch in PAIRS:
            if not stack:
                return Result(False, i, f"unexpected {ch!r}")
            opener, where = stack.pop()
            if opener != PAIRS[ch]:
                return Result(False, i, f"{ch!r} closes {opener!r} opened at {where}")
    if stack:
        opener, where = stack[-1]
        return Result(False, where, f"{opener!r} never closed")
    return Result(True)


def min_additions(parens):
    need_open = balance = 0
    for ch in parens:
        balance += 1 if ch == "(" else -1
        if balance < 0:
            need_open += 1
            balance = 0
    return need_open + balance


def max_depth(text):
    depth = best = 0
    for ch in text:
        if ch in OPENERS:
            depth += 1
            best = max(best, depth)
        elif ch in PAIRS:
            depth -= 1
    return best


def generate(n, prefix="", opened=0, closed=0):
    if len(prefix) == 2 * n:
        yield prefix
        return
    if opened < n:
        yield from generate(n, prefix + "(", opened + 1, closed)
    if closed < opened:
        yield from generate(n, prefix + ")", opened, closed + 1)


def main():
    samples = ["{[()()]}", "if (a[i] > b{c}) { run(); }", "([)]", "((())", "())",
               "vector<map<int, list<int>>>", "", "}{"]
    for s in samples:
        r = check(s)
        where = "" if r.ok else f" at index {r.position}"
        print(f"{s!r:<34} {r.message}{where}  depth={max_depth(s)}")
    for p in ("())", "(((", "()))((", "()()"):
        print(f"Additions needed for {p!r}: {min_additions(p)}")
    combos = list(generate(4))
    print(f"{len(combos)} balanced strings of 4 pairs; first five: {combos[:5]}")
    assert all(check(c).ok for c in combos)


if __name__ == "__main__":
    main()
