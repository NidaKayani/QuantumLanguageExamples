"""Tower of Hanoi: recursive generator, iterative solution, state display, and four-peg Frame-Stewart."""
from functools import lru_cache


def hanoi(n, src="A", dst="C", via="B"):
    if n == 0:
        return
    yield from hanoi(n - 1, src, via, dst)
    yield (n, src, dst)
    yield from hanoi(n - 1, via, dst, src)


def hanoi_iterative(n):
    """Smallest disk cycles in one direction; every other move is the only legal non-smallest move."""
    pegs = {"A": list(range(n, 0, -1)), "B": [], "C": []}
    cycle = ["A", "C", "B"] if n % 2 else ["A", "B", "C"]
    small_at = 0
    moves = []
    for k in range(1, 2 ** n):
        if k % 2:
            src, dst = cycle[small_at], cycle[(small_at + 1) % 3]
            small_at = (small_at + 1) % 3
        else:
            a, b = [p for p in "ABC" if p != cycle[small_at]]
            if not pegs[a] or (pegs[b] and pegs[b][-1] < pegs[a][-1]):
                a, b = b, a
            src, dst = a, b
        pegs[dst].append(pegs[src].pop())
        moves.append((pegs[dst][-1], src, dst))
    return moves


def simulate(n, moves):
    pegs = {"A": list(range(n, 0, -1)), "B": [], "C": []}
    for disk, src, dst in moves:
        assert pegs[src][-1] == disk, "moved a disk that is not on top"
        assert not pegs[dst] or pegs[dst][-1] > disk, "larger disk placed on smaller"
        pegs[dst].append(pegs[src].pop())
    return pegs


@lru_cache(maxsize=None)
def frame_stewart(n, pegs=4):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if pegs == 3:
        return 2 ** n - 1
    return min(2 * frame_stewart(k, pegs) + frame_stewart(n - k, pegs - 1) for k in range(1, n))


moves = list(hanoi(3))
print("3 disks:", len(moves), "moves")
pegs = {"A": [3, 2, 1], "B": [], "C": []}
for step, (disk, src, dst) in enumerate(moves, 1):
    pegs[dst].append(pegs[src].pop())
    state = "  ".join(f"{p}:{''.join(map(str, pegs[p])):<3}" for p in "ABC")
    print(f"  {step}. disk {disk} {src}->{dst}   {state}")

for n in (5, 10, 16):
    moves = list(hanoi(n))
    final = simulate(n, moves)
    print(f"{n} disks: {len(moves)} moves, all on C: {final['C'] == list(range(n, 0, -1))}")

disk_order = [d for d, _, _ in hanoi(5)]
print("Disk moved at each step (5 disks):", "".join(map(str, disk_order)))
print("Iterative solver gives identical moves:", all(list(hanoi(n)) == hanoi_iterative(n) for n in range(1, 9)))
print("Four pegs (Frame-Stewart) vs three:")
for n in (3, 5, 8, 10, 15, 20):
    print(f"  n={n:>2}: 4 pegs={frame_stewart(n):>6}  3 pegs={2 ** n - 1:>8}")
