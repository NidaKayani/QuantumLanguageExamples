"""A simple BankAccount class with __init__, instance methods, and state changes."""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f"cannot withdraw {amount}; balance is {self.balance}")
        self.balance -= amount
        self.history.append(("withdraw", amount))

    def statement(self):
        lines = [f"Statement for {self.owner}"]
        for kind, amount in self.history:
            sign = "+" if kind == "deposit" else "-"
            lines.append(f"  {kind:<9}{sign}{amount:>8.2f}")
        lines.append(f"  balance   {self.balance:>9.2f}")
        return "\n".join(lines)


alice = BankAccount("Alice", 100)
bob = BankAccount("Bob")
alice.deposit(50)
alice.withdraw(30)
bob.deposit(200)
try:
    bob.withdraw(500)
except ValueError as exc:
    print("Error:", exc)
try:
    alice.deposit(-5)
except ValueError as exc:
    print("Error:", exc)

print(alice.statement())
print(bob.statement())
print("attributes:", sorted(vars(alice)))
print("same class:", type(alice) is type(bob), type(alice).__name__)
