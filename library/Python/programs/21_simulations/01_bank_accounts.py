"""Simulate bank accounts with deposits, withdrawals, transfers and monthly interest."""
from decimal import Decimal, ROUND_HALF_UP


class InsufficientFunds(Exception):
    pass


class Account:
    _next_number = 1000

    def __init__(self, owner, balance="0.00", rate="0.00"):
        self.owner = owner
        self.balance = Decimal(balance)
        self.rate = Decimal(rate)
        self.number = Account._next_number
        Account._next_number += 1
        self.history = []

    def deposit(self, amount):
        amount = Decimal(amount)
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        amount = Decimal(amount)
        if amount > self.balance:
            raise InsufficientFunds(f"{self.owner} cannot withdraw {amount}")
        self.balance -= amount
        self.history.append(("withdraw", amount))

    def apply_interest(self):
        interest = (self.balance * self.rate / 12).quantize(Decimal("0.01"), ROUND_HALF_UP)
        self.balance += interest
        self.history.append(("interest", interest))
        return interest

    def __repr__(self):
        return f"Account(#{self.number}, {self.owner!r}, {self.balance})"


class Bank:
    def __init__(self):
        self.accounts = {}

    def open(self, owner, balance="0.00", rate="0.00"):
        acct = Account(owner, balance, rate)
        self.accounts[owner] = acct
        return acct

    def transfer(self, src, dst, amount):
        self.accounts[src].withdraw(amount)
        self.accounts[dst].deposit(amount)

    def total(self):
        return sum((a.balance for a in self.accounts.values()), Decimal("0"))


bank = Bank()
bank.open("alice", "500.00", "0.03")
bank.open("bob", "120.50", "0.02")
bank.open("carol", "0.00")

bank.accounts["carol"].deposit("75.25")
bank.transfer("alice", "bob", "200")
try:
    bank.transfer("carol", "alice", "100")
except InsufficientFunds as exc:
    print("Error:", exc)

for month in range(1, 4):
    earned = {name: acct.apply_interest() for name, acct in bank.accounts.items()}
    print(f"Month {month} interest:", ", ".join(f"{k}={v}" for k, v in earned.items()))

for acct in sorted(bank.accounts.values(), key=lambda a: a.balance, reverse=True):
    print(acct, "transactions:", len(acct.history))
print("Bank total:", bank.total())
