"""Composition versus inheritance: a Stack built both ways and their differences."""


class InheritedStack(list):
    def push(self, item):
        self.append(item)

    def peek(self):
        return self[-1]


class ComposedStack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"ComposedStack({self._items})"


class Engine:
    def __init__(self, hp):
        self.hp = hp

    def start(self):
        return f"engine ({self.hp} hp) started"


class Car:
    def __init__(self, model, hp):
        self.model = model
        self.engine = Engine(hp)  # has-a relationship

    def drive(self):
        return f"{self.model}: {self.engine.start()}, driving"


a = InheritedStack()
b = ComposedStack()
for n in (1, 2, 3):
    a.push(n)
    b.push(n)
print("inherited:", a, "peek:", a.peek(), "pop:", a.pop())
print("composed:", b, "peek:", b.peek(), "pop:", b.pop())

a.insert(0, 99)  # inheritance leaks list API, breaking the stack abstraction
print("inherited after insert(0, 99):", a)
print("composed has insert:", hasattr(b, "insert"))
print("lengths:", len(a), len(b))
try:
    ComposedStack().pop()
except IndexError as exc:
    print("IndexError:", exc)

car = Car("Roadster", 300)
print(car.drive())
print("Car is an Engine?", isinstance(car, Engine), "| has an Engine?", isinstance(car.engine, Engine))
