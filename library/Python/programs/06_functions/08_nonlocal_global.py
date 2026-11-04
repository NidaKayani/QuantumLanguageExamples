"""The global and nonlocal statements and how Python resolves names (LEGB)."""

call_count = 0
level = "global"


def tracked(value):
    global call_count
    call_count += 1
    return value * 2


def outer():
    level = "enclosing"

    def inner():
        level = "local"
        return level

    def peek():
        return level

    def rebind():
        nonlocal level
        level = "rebound"

    results = [inner(), peek()]
    rebind()
    results.append(peek())
    return results


def bank_account(balance):
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            raise ValueError(f"insufficient funds: {balance} < {amount}")
        balance -= amount
        return balance

    return deposit, withdraw


def broken():
    print(call_count)
    call_count = 5


for n in range(4):
    tracked(n)
print("call_count:", call_count)
print("outer():", outer())
print("module level still:", level)

deposit, withdraw = bank_account(100)
print("deposit 50 ->", deposit(50))
print("withdraw 30 ->", withdraw(30))
try:
    withdraw(500)
except ValueError as exc:
    print("error:", exc)

try:
    broken()
except UnboundLocalError:
    print("UnboundLocalError: assignment makes call_count local in broken()")
