"""0/1 knapsack: full table with item reconstruction and a 1-D space-optimised version."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    name: str
    weight: int
    value: int


ITEMS = [
    Item("tent", 5, 60), Item("stove", 3, 40), Item("camera", 2, 50),
    Item("book", 1, 10), Item("laptop", 4, 70), Item("water", 3, 30),
    Item("snacks", 1, 15), Item("jacket", 2, 35),
]


def knapsack_table(items, capacity):
    n = len(items)
    table = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i, item in enumerate(items, start=1):
        for w in range(capacity + 1):
            table[i][w] = table[i - 1][w]
            if item.weight <= w:
                table[i][w] = max(table[i][w], table[i - 1][w - item.weight] + item.value)
    chosen, w = [], capacity
    for i in range(n, 0, -1):
        if table[i][w] != table[i - 1][w]:
            chosen.append(items[i - 1])
            w -= items[i - 1].weight
    return table[n][capacity], chosen[::-1]


def knapsack_1d(items, capacity):
    best = [0] * (capacity + 1)
    for item in items:
        for w in range(capacity, item.weight - 1, -1):
            best[w] = max(best[w], best[w - item.weight] + item.value)
    return best


def main():
    for cap in (5, 10, 15):
        value, chosen = knapsack_table(ITEMS, cap)
        names = ", ".join(i.name for i in chosen)
        weight = sum(i.weight for i in chosen)
        print(f"Capacity {cap:2d}: value {value:3d}, weight {weight:2d} -> {names}")
    curve = knapsack_1d(ITEMS, 21)
    print("Best value by capacity:", curve)
    assert curve[10] == knapsack_table(ITEMS, 10)[0]
    ratio = sorted(ITEMS, key=lambda i: i.value / i.weight, reverse=True)
    print("Greedy ratio order:", [i.name for i in ratio])
    greedy, room = 0, 10
    for item in ratio:
        if item.weight <= room:
            greedy += item.value
            room -= item.weight
    print(f"Greedy at capacity 10 gives {greedy} vs optimal {curve[10]}")


if __name__ == "__main__":
    main()
