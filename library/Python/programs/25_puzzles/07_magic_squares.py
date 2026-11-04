"""Construct magic squares (Siamese odd order, doubly-even order) and enumerate all 3x3 ones."""
from itertools import permutations


def siamese(n):
    square = [[0] * n for _ in range(n)]
    r, c = 0, n // 2
    for k in range(1, n * n + 1):
        square[r][c] = k
        nr, nc = (r - 1) % n, (c + 1) % n
        if square[nr][nc]:
            nr, nc = (r + 1) % n, c
        r, c = nr, nc
    return square


def doubly_even(n):
    square = [[r * n + c + 1 for c in range(n)] for r in range(n)]
    for r in range(n):
        for c in range(n):
            if (r % 4 in (0, 3)) == (c % 4 in (0, 3)):
                square[r][c] = n * n + 1 - square[r][c]
    return square


def is_magic(sq):
    n = len(sq)
    target = n * (n * n + 1) // 2
    lines = [*sq, *zip(*sq), [sq[i][i] for i in range(n)], [sq[i][n - 1 - i] for i in range(n)]]
    return all(sum(line) == target for line in lines), target


def show(sq):
    w = len(str(len(sq) ** 2))
    return "\n".join(" ".join(f"{x:>{w}}" for x in row) for row in sq)


for n, builder in [(3, siamese), (5, siamese), (4, doubly_even), (8, doubly_even)]:
    sq = builder(n)
    ok, target = is_magic(sq)
    print(f"{n}x{n} via {builder.__name__}: magic={ok}, constant={target}")
    print(show(sq))
    print()


def all_3x3():
    found = []
    for center_free in permutations([1, 2, 3, 4, 6, 7, 8, 9]):
        a, b, c, d, f, g, h, i = center_free
        e = 5  # the center of any 3x3 magic square must be 5
        if a + b + c == 15 and d + e + f == 15 and a + d + g == 15 and b + e + h == 15 \
                and a + e + i == 15 and c + e + g == 15:
            found.append(((a, b, c), (d, e, f), (g, h, i)))
    return found


squares = all_3x3()
print(f"All 3x3 magic squares: {len(squares)} (one up to rotation/reflection)")
for sq in squares[:2]:
    print(" | ".join(" ".join(map(str, row)) for row in sq))
print("Corners are always even:", all({sq[0][0], sq[0][2], sq[2][0], sq[2][2]} == {2, 4, 6, 8} for sq in squares))
