"""Josephus problem: deque simulation, O(n) recurrence and the closed form for k = 2."""
from collections import deque


def simulate(n, k):
    circle = deque(range(1, n + 1))
    order = []
    while circle:
        circle.rotate(-(k - 1))
        order.append(circle.popleft())
    return order


def survivor_recurrence(n, k):
    pos = 0
    for size in range(2, n + 1):
        pos = (pos + k) % size
    return pos + 1


def survivor_k2(n):
    highest = 1 << (n.bit_length() - 1)
    return 2 * (n - highest) + 1


order = simulate(7, 3)
print("n=7, k=3 elimination order:", order, "-> survivor", order[-1])
order = simulate(41, 3)
print("Josephus' own case n=41, k=3: last two standing are", order[-2:])

print(f"{'n':>4} {'k=2':>5} {'k=3':>5} {'k=5':>5}")
for n in (5, 10, 16, 25, 50, 100):
    print(f"{n:>4} {survivor_recurrence(n, 2):>5} {survivor_recurrence(n, 3):>5} {survivor_recurrence(n, 5):>5}")

agree = all(simulate(n, k)[-1] == survivor_recurrence(n, k) for n in range(1, 60) for k in range(1, 8))
print("Simulation agrees with recurrence for n<60, k<8:", agree)
closed = all(survivor_k2(n) == survivor_recurrence(n, 2) for n in range(1, 2000))
print("Closed form 2(n - 2^m) + 1 matches for k=2, n<2000:", closed)
print("k=2 survivors n=1..16:", [survivor_k2(n) for n in range(1, 17)])
print("Bit rotation trick for n=41:", bin(41), "->", bin(survivor_k2(41)), "=", int(bin(41)[3:] + "1", 2))
print("Survivor for n=100000, k=7:", survivor_recurrence(100_000, 7))
