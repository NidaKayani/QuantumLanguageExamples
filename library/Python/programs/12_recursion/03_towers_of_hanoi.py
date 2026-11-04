"""Towers of Hanoi: recursive move generation with peg state tracking."""

from typing import Iterator


def hanoi(n: int, src: str, dst: str, via: str) -> Iterator[tuple[int, str, str]]:
    if n == 0:
        return
    yield from hanoi(n - 1, src, via, dst)
    yield n, src, dst
    yield from hanoi(n - 1, via, dst, src)


def solve(n: int, verbose: bool = True) -> int:
    pegs = {"A": list(range(n, 0, -1)), "B": [], "C": []}
    count = 0
    for disk, src, dst in hanoi(n, "A", "C", "B"):
        moved = pegs[src].pop()
        assert moved == disk
        assert not pegs[dst] or pegs[dst][-1] > disk, "illegal move"
        pegs[dst].append(disk)
        count += 1
        if verbose:
            state = "  ".join(f"{p}:{''.join(map(str, s)) or '-'}" for p, s in pegs.items())
            print(f"{count:2d}. disk {disk} {src}->{dst}   {state}")
    assert pegs["C"] == list(range(n, 0, -1))
    return count


solve(3)
print()
for n in range(1, 11):
    moves = solve(n, verbose=False)
    print(f"{n:2d} disks: {moves:4d} moves (2^n - 1 = {2 ** n - 1})")
