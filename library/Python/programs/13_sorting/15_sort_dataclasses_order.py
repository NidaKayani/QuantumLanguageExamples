"""Ordering custom objects: dataclass(order=True) and functools.total_ordering."""

from dataclasses import dataclass, field
from functools import total_ordering


@dataclass(order=True)
class Task:
    priority: int
    due_day: int
    title: str = field(compare=False)


@total_ordering
class Money:
    def __init__(self, amount: float, currency: str):
        self.amount = amount
        self.currency = currency

    RATES = {"USD": 1.0, "EUR": 1.08, "GBP": 1.27, "JPY": 0.0067}

    def in_usd(self) -> float:
        return self.amount * self.RATES[self.currency]

    def __eq__(self, other):
        return self.in_usd() == other.in_usd()

    def __lt__(self, other):
        return self.in_usd() < other.in_usd()

    def __repr__(self):
        return f"{self.amount:g} {self.currency}"


tasks = [
    Task(2, 5, "write docs"),
    Task(1, 3, "fix crash"),
    Task(2, 1, "review PR"),
    Task(3, 2, "refactor"),
    Task(1, 3, "patch CVE"),
]
for t in sorted(tasks):
    print(f"p{t.priority} day{t.due_day}: {t.title}")
print("Task(1,3,'a') == Task(1,3,'b'):", Task(1, 3, "a") == Task(1, 3, "b"))

prices = [Money(100, "USD"), Money(90, "EUR"), Money(15000, "JPY"), Money(80, "GBP"), Money(50, "EUR")]
print("sorted money:", sorted(prices))
print("most valuable:", max(prices), "| cheapest:", min(prices))
print("total_ordering gives >=:", Money(1, "GBP") >= Money(1, "EUR"))
