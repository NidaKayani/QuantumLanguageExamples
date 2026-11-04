"""A bank account hierarchy with overridden withdrawal rules and interest policies."""


class InsufficientFunds(Exception):
    pass


class Account:
    interest_rate = 0.0

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def can_withdraw(self, amount):
        return amount <= self.balance

    def withdraw(self, amount):
        if not self.can_withdraw(amount):
            raise InsufficientFunds(f"{type(self).__name__} of {self.owner}: cannot withdraw {amount:.2f}")
        self.balance -= amount
        return self.balance

    def month_end(self):
        self.balance += self.balance * self.interest_rate / 12

    def __str__(self):
        return f"{type(self).__name__:<16}{self.owner:<6}{self.balance:>10.2f}"


class Savings(Account):
    interest_rate = 0.04
    min_balance = 100

    def can_withdraw(self, amount):
        return self.balance - amount >= self.min_balance


class Checking(Account):
    def __init__(self, owner, balance=0.0, overdraft=200):
        super().__init__(owner, balance)
        self.overdraft = overdraft

    def can_withdraw(self, amount):
        return amount <= self.balance + self.overdraft


class PremiumChecking(Checking):
    interest_rate = 0.01

    def month_end(self):
        super().month_end()
        if self.balance < 0:
            self.balance -= 5  # overdraft fee


accounts = [Account("Ann", 500), Savings("Ben", 1000), Checking("Cat", 50), PremiumChecking("Dan", 0, 500)]
requests = [("Ann", 600), ("Ben", 950), ("Ben", 800), ("Cat", 220), ("Dan", 300)]
lookup = {a.owner: a for a in accounts}
for owner, amount in requests:
    try:
        lookup[owner].withdraw(amount)
        print(f"{owner} withdrew {amount}")
    except InsufficientFunds as exc:
        print("denied:", exc)
for acct in accounts:
    acct.month_end()
print("\nMonth-end balances:")
for acct in accounts:
    print(acct)
