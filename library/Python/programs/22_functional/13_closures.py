"""Closures capturing state: counters, accumulators, late binding pitfalls and nonlocal."""


def make_counter(start=0, step=1):
    count = start - step

    def counter():
        nonlocal count
        count += step
        return count

    return counter


def make_averager():
    values = []

    def add(x):
        values.append(x)
        return sum(values) / len(values)

    return add


def make_account(balance):
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            raise ValueError("insufficient funds")
        balance -= amount
        return balance

    return {"deposit": deposit, "withdraw": withdraw, "balance": lambda: balance}


c1, c2 = make_counter(), make_counter(100, 10)
print("counter 1:", [c1() for _ in range(5)])
print("counter 2:", [c2() for _ in range(5)])
print("counter 1 again:", c1())

avg = make_averager()
print("running averages:", [round(avg(x), 2) for x in (10, 20, 30, 5)])
print("closure cell contents:", avg.__closure__[0].cell_contents)
print("free variables:", avg.__code__.co_freevars, make_counter().__code__.co_freevars)

acct = make_account(50)
acct["deposit"](25)
acct["withdraw"](30)
try:
    acct["withdraw"](500)
except ValueError as exc:
    print("withdraw failed:", exc)
print("balance:", acct["balance"]())

late = [lambda: i for i in range(4)]
early = [lambda i=i: i for i in range(4)]
print("late binding:", [f() for f in late])
print("default-arg binding:", [f() for f in early])


def multipliers():
    return [(lambda x, n=n: x * n) for n in range(1, 5)]


print("multipliers applied to 3:", [m(3) for m in multipliers()])


def outer():
    log = []

    def middle(tag):
        def inner(value):
            log.append(f"{tag}:{value}")
            return len(log)
        return inner

    return middle, log


middle, log = outer()
a, b = middle("a"), middle("b")
a(1); b(2); a(3)
print("shared log through nested closures:", log)
