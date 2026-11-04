"""Egg drop puzzle: classic DP, the moves-based formulation, and a decision strategy."""
from functools import lru_cache
from math import comb


@lru_cache(maxsize=None)
def worst_case_drops(eggs, floors):
    if floors <= 1 or eggs == 1:
        return floors
    best = floors
    lo, hi = 1, floors
    while lo <= hi:
        mid = (lo + hi) // 2
        breaks = worst_case_drops(eggs - 1, mid - 1)
        survives = worst_case_drops(eggs, floors - mid)
        best = min(best, 1 + max(breaks, survives))
        if breaks < survives:
            lo = mid + 1
        else:
            hi = mid - 1
    return best


def floors_coverable(eggs, moves):
    return sum(comb(moves, i) for i in range(1, eggs + 1))


def min_moves(eggs, floors):
    moves = 0
    while floors_coverable(eggs, moves) < floors:
        moves += 1
    return moves


def strategy(eggs, floors, base=0):
    """First floor to try with `eggs` eggs over floors base+1..base+floors."""
    moves = min_moves(eggs, floors)
    return base + floors_coverable(eggs - 1, moves - 1) + 1 if eggs > 1 else base + 1


def simulate(eggs, floors, critical):
    low, span, drops, log = 0, floors, 0, []
    while span > 0:
        floor = min(strategy(eggs, span, low), low + span)
        drops += 1
        broke = floor > critical
        log.append(f"{floor}{'x' if broke else 'o'}")
        if broke:
            eggs -= 1
            span = floor - low - 1
        else:
            span -= floor - low
            low = floor
    return low, drops, log


def main():
    print("Worst-case drops (rows = eggs, cols = floors):")
    floor_list = [10, 36, 100, 200]
    print("eggs " + "".join(f"{f:>6}" for f in floor_list))
    for eggs in range(1, 5):
        row = [worst_case_drops(eggs, f) for f in floor_list]
        assert row == [min_moves(eggs, f) for f in floor_list]
        print(f"{eggs:>4} " + "".join(f"{v:>6}" for v in row))
    print("Floors coverable with 3 eggs and k moves:",
          [floors_coverable(3, k) for k in range(1, 11)])
    for critical in (0, 14, 57, 99, 100):
        found, drops, log = simulate(2, 100, critical)
        print(f"Critical floor {critical:3d}: found {found:3d} in {drops:2d} drops {' '.join(log)}")


if __name__ == "__main__":
    main()
