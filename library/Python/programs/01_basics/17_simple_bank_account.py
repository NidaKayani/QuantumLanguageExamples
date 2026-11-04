"""Model a bank account with a small class, validation and a transaction log."""


class InsufficientFunds(Exception):
    pass


class Account:
    interest_rate = 0.02

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
            raise InsufficientFunds(f"cannot withdraw {amount}; balance is {self.balance}")
        self.balance -= amount
        self.history.append(("withdraw", amount))

    def add_interest(self):
        interest = round(self.balance * self.interest_rate, 2)
        self.balance += interest
        self.history.append(("interest", interest))

    def __repr__(self):
        return f"Account({self.owner!r}, balance={self.balance:.2f})"


acct = Account("Maria", 100)
acct.deposit(250)
acct.withdraw(75)
acct.add_interest()

for action in (lambda: acct.withdraw(1000), lambda: acct.deposit(-5)):
    try:
        action()
    except (InsufficientFunds, ValueError) as e:
        print(f"{type(e).__name__}: {e}")

print(acct)
print("transactions:")
for kind, amount in acct.history:
    print(f"  {kind:<9}{amount:>9.2f}")
deposits = sum(a for k, a in acct.history if k == "deposit")
print(f"total deposits: {deposits}")
