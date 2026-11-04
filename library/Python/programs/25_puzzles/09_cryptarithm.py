"""Cryptarithm solver working column by column with carries, e.g. SEND + MORE = MONEY."""
import re


def solve(puzzle):
    left, right = puzzle.replace(" ", "").split("=")
    words = left.split("+")
    width = max(len(right), *(len(w) for w in words))
    leading = {w[0] for w in words + [right] if len(w) > 1}
    columns = []
    for i in range(width):
        adds = [w[-1 - i] for w in words if i < len(w)]
        res = right[-1 - i] if i < len(right) else None
        columns.append((adds, res))
    assignment, used = {}, set()
    solutions = []

    def assign_then(letters, k, then):
        if k == len(letters):
            then()
            return
        ch = letters[k]
        if ch in assignment:
            assign_then(letters, k + 1, then)
            return
        for d in range(10):
            if d in used or (d == 0 and ch in leading):
                continue
            assignment[ch] = d
            used.add(d)
            assign_then(letters, k + 1, then)
            used.discard(d)
            del assignment[ch]

    def column(i, carry):
        if i == width:
            if carry == 0:
                solutions.append(dict(assignment))
            return
        adds, res = columns[i]

        def check():
            total = carry + sum(assignment[a] for a in adds)
            digit = total % 10
            if res is None:
                return
            if res in assignment:
                if assignment[res] == digit:
                    column(i + 1, total // 10)
            elif digit not in used and not (digit == 0 and res in leading):
                assignment[res] = digit
                used.add(digit)
                column(i + 1, total // 10)
                used.discard(digit)
                del assignment[res]

        assign_then(adds, 0, check)

    column(0, 0)
    return solutions


def render(puzzle, sol):
    return re.sub(r"[A-Z]", lambda m: str(sol[m.group()]), puzzle)


for puzzle in ["SEND + MORE = MONEY", "TWO + TWO = FOUR", "BASE + BALL = GAMES",
               "CROSS + ROADS = DANGER", "AB + AB = BCC"]:
    sols = solve(puzzle)
    print(f"{puzzle}: {len(sols)} solution(s)")
    for sol in sols[:3]:
        print("   ", render(puzzle, sol), " ", "".join(f"{k}={v} " for k, v in sorted(sol.items())))
