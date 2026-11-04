"""Infinite iterators from itertools: count, cycle, repeat, bounded with islice."""
from itertools import count, cycle, repeat, islice

print("count(10):", list(islice(count(10), 5)))
print("count(0, 0.25):", list(islice(count(0, 0.25), 6)))
print("count(100, -7):", list(islice(count(100, -7), 5)))

colors = cycle(["red", "green", "blue"])
print("cycle:", [next(colors) for _ in range(7)])

print("repeat:", list(repeat("ab", 4)))
print("map with repeat:", list(map(pow, range(6), repeat(2))))

players = ["Ann", "Bob", "Cid"]
turns = zip(count(1), cycle(players))
for turn, player in islice(turns, 7):
    print(f"turn {turn}: {player}")

print("islice(start, stop, step):", list(islice("abcdefghijklmnop", 2, 12, 3)))

ids = (f"ID-{n:04d}" for n in count(1))
print("generated ids:", list(islice(ids, 3)), "| next:", next(ids))

squares = (n * n for n in count(1))
first_big = next(n for n in squares if n > 500)
print("first square > 500:", first_big)
