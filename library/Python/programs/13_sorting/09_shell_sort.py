"""Shell sort with Shell, Knuth and Ciura gap sequences."""


def shell_gaps(n):
    gap = n // 2
    while gap > 0:
        yield gap
        gap //= 2


def knuth_gaps(n):
    gaps = [1]
    while gaps[-1] * 3 + 1 < n:
        gaps.append(gaps[-1] * 3 + 1)
    return reversed(gaps)


def ciura_gaps(n):
    return [g for g in (701, 301, 132, 57, 23, 10, 4, 1) if g < n] or [1]


def shell_sort(arr, gaps):
    a = list(arr)
    moves = 0
    for gap in gaps:
        for i in range(gap, len(a)):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
                moves += 1
            a[j] = temp
    return a, moves


def lcg(seed):
    while True:
        seed = (1103515245 * seed + 12345) % 2 ** 31
        yield seed


gen = lcg(2024)
data = [next(gen) % 1000 for _ in range(200)]
print("first 12 inputs:", data[:12])

for name, gap_fn in [("shell", shell_gaps), ("knuth", knuth_gaps), ("ciura", ciura_gaps)]:
    gaps = list(gap_fn(len(data)))
    result, moves = shell_sort(data, gaps)
    assert result == sorted(data)
    print(f"{name:<6} gaps={gaps} moves={moves}")

plain, moves = shell_sort(data, [1])
print(f"gap=1 only (insertion sort) moves={moves}")
print("smallest ten:", plain[:10])
print("largest ten:", plain[-10:])
