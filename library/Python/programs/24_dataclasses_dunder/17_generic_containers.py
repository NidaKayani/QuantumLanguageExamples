"""Generic container classes with TypeVar and Generic: a typed stack, a bounded queue and a registry."""
from collections import deque
from dataclasses import dataclass, field
from typing import Callable, Generic, Iterator, Optional, TypeVar

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> Optional[T]:
        return self._items[-1] if self._items else None

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return reversed(self._items)


@dataclass
class BoundedQueue(Generic[T]):
    capacity: int
    dropped: list[T] = field(default_factory=list)
    _items: deque = field(default_factory=deque, repr=False)

    def put(self, item: T) -> None:
        if len(self._items) == self.capacity:
            self.dropped.append(self._items.popleft())
        self._items.append(item)

    def items(self) -> list[T]:
        return list(self._items)


class Registry(Generic[K, V]):
    def __init__(self, key_func: Callable[[V], K]):
        self._key = key_func
        self._data: dict[K, V] = {}

    def add(self, value: V) -> K:
        key = self._key(value)
        self._data[key] = value
        return key

    def get(self, key: K, default: Optional[V] = None) -> Optional[V]:
        return self._data.get(key, default)


def balanced(text: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: Stack[str] = Stack()
    for ch in text:
        if ch in "([{":
            stack.push(ch)
        elif ch in pairs:
            if not len(stack) or stack.pop() != pairs[ch]:
                return False
    return len(stack) == 0


for expr in ["(a[b]{c})", "([)]", "((()", "{[()()]}"]:
    print(f"{expr:<10} balanced={balanced(expr)}")

s: Stack[int] = Stack()
for n in (1, 2, 3):
    s.push(n * 10)
print("stack top-down:", list(s), "| peek:", s.peek(), "| pop:", s.pop(), "| len:", len(s))

q: BoundedQueue[str] = BoundedQueue(3)
for event in "abcdef":
    q.put(event)
print("queue:", q.items(), "| dropped:", q.dropped, "|", q)

users: Registry[str, dict] = Registry(lambda u: u["email"].lower())
for u in [{"email": "Ann@X.io", "age": 30}, {"email": "bob@y.io", "age": 25}]:
    print("registered key:", users.add(u))
print("lookup:", users.get("ann@x.io"), "| missing:", users.get("zed@z.io", {}))
print("generic alias:", Stack[int].__origin__.__name__, [p.__name__ for p in Registry.__parameters__])
