"""Linear search variants: first match, all matches, sentinel and predicates."""

from typing import Callable, Iterable, Optional, Sequence, TypeVar

T = TypeVar("T")


def linear_search(seq: Sequence[T], target: T) -> int:
    for i, item in enumerate(seq):
        if item == target:
            return i
    return -1


def find_all(seq: Sequence[T], target: T) -> list[int]:
    return [i for i, item in enumerate(seq) if item == target]


def sentinel_search(arr: list, target) -> int:
    n = len(arr)
    if n == 0:
        return -1
    last = arr[-1]
    arr[-1] = target
    i = 0
    while arr[i] != target:
        i += 1
    arr[-1] = last
    return i if i < n - 1 or last == target else -1


def find_first(items: Iterable[T], pred: Callable[[T], bool]) -> Optional[T]:
    return next((x for x in items if pred(x)), None)


data = [17, 4, 23, 8, 42, 15, 8, 16, 4, 8]
for target in [42, 8, 99]:
    print(f"search {target:>2}: index={linear_search(data, target):>2} "
          f"all={find_all(data, target)} sentinel={sentinel_search(data, target)}")
print("data unchanged after sentinel search:", data)

print("first > 20:", find_first(data, lambda x: x > 20))
print("first negative:", find_first(data, lambda x: x < 0))
print("list.index(15):", data.index(15), "| 'in' operator:", 23 in data)

inventory = [("bolt", 120), ("nut", 0), ("screw", 45), ("rivet", 0)]
out_of_stock = [name for name, qty in inventory if qty == 0]
print("out of stock:", out_of_stock)
print("any stock above 100:", any(q > 100 for _, q in inventory))
print("all named items:", all(name for name, _ in inventory))
