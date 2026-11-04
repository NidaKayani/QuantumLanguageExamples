"""Ordered dataclasses: order=True, field(compare=False), sort_index tricks and heap usage."""
import heapq
from dataclasses import dataclass, field


@dataclass(order=True)
class Task:
    priority: int
    deadline: int
    name: str = field(compare=False)
    tags: list = field(default_factory=list, compare=False, repr=False)


@dataclass(order=True)
class Player:
    sort_key: tuple = field(init=False, repr=False)
    name: str
    wins: int
    losses: int

    def __post_init__(self):
        self.sort_key = (-self.wins, self.losses, self.name)


tasks = [
    Task(2, 30, "write report"),
    Task(1, 50, "fix outage", ["urgent"]),
    Task(2, 10, "review PR"),
    Task(3, 5, "lunch"),
    Task(1, 20, "call customer"),
]
print("sorted tasks:")
for t in sorted(tasks):
    print("  ", t)

print("min:", min(tasks).name, "| max:", max(tasks).name)
print("compare ignores name:", Task(1, 1, "a") == Task(1, 1, "b"))
print("comparison operators:", Task(1, 5, "x") < Task(1, 6, "y"), Task(2, 0, "x") >= Task(1, 99, "y"))

queue = []
for t in tasks:
    heapq.heappush(queue, t)
print("heap pop order:", [heapq.heappop(queue).name for _ in range(len(tasks))])

players = [Player("zed", 5, 2), Player("amy", 7, 3), Player("bob", 5, 1), Player("cat", 7, 3)]
print("leaderboard:")
for rank, p in enumerate(sorted(players), 1):
    print(f"  {rank}. {p.name:<4} {p.wins}-{p.losses}")
print("repr hides sort key:", players[0])
