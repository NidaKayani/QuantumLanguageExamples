"""Vending machine modeled as a finite state machine processing a stream of events."""
from enum import Enum, auto


class State(Enum):
    IDLE = auto()
    HAS_MONEY = auto()
    DISPENSING = auto()


class VendingMachine:
    PRODUCTS = {"A1": ("Cola", 125), "A2": ("Chips", 100), "B1": ("Candy", 65)}
    COINS = (25, 10, 5)

    def __init__(self):
        self.state = State.IDLE
        self.credit = 0
        self.stock = {code: 2 for code in self.PRODUCTS}
        self.sales = 0

    def insert(self, cents):
        if cents not in (5, 10, 25, 100):
            return f"rejected coin {cents}"
        self.credit += cents
        self.state = State.HAS_MONEY
        return f"credit {self.credit}"

    def select(self, code):
        if self.state is not State.HAS_MONEY:
            return "insert money first"
        if code not in self.PRODUCTS:
            return f"unknown product {code}"
        name, price = self.PRODUCTS[code]
        if self.stock[code] == 0:
            return f"{name} sold out"
        if self.credit < price:
            return f"{name} costs {price}, need {price - self.credit} more"
        self.state = State.DISPENSING
        self.stock[code] -= 1
        self.sales += price
        change = self._make_change(self.credit - price)
        self.credit = 0
        self.state = State.IDLE
        return f"dispensed {name}, change {change}"

    def refund(self):
        coins = self._make_change(self.credit)
        self.credit, self.state = 0, State.IDLE
        return f"refunded {coins}"

    def _make_change(self, amount):
        result = []
        for coin in self.COINS:
            count, amount = divmod(amount, coin)
            result.extend([coin] * count)
        return result


events = [
    ("select", "A1"), ("insert", 100), ("select", "A1"), ("insert", 25),
    ("insert", 25), ("select", "A1"), ("insert", 3), ("insert", 100),
    ("select", "B1"), ("insert", 100), ("select", "A1"), ("insert", 100),
    ("select", "A1"), ("refund", None), ("insert", 10), ("refund", None),
]

vm = VendingMachine()
for step, (action, arg) in enumerate(events, 1):
    handler = getattr(vm, action)
    message = handler(arg) if arg is not None else handler()
    print(f"{step:2d}. {action:<6} {str(arg or ''):>4} -> {message} [{vm.state.name}]")

print("Total sales (cents):", vm.sales)
print("Stock left:", vm.stock)
