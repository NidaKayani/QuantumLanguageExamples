"""Polymorphism in a payroll system where each employee type computes pay differently."""


class Employee:
    def __init__(self, name):
        self.name = name

    def pay(self):
        raise NotImplementedError(f"{type(self).__name__} must implement pay()")

    def __str__(self):
        return f"{self.name:<8} {type(self).__name__:<14} {self.pay():>10.2f}"


class Salaried(Employee):
    def __init__(self, name, annual):
        super().__init__(name)
        self.annual = annual

    def pay(self):
        return self.annual / 12


class Hourly(Employee):
    def __init__(self, name, rate, hours):
        super().__init__(name)
        self.rate, self.hours = rate, hours

    def pay(self):
        overtime = max(0, self.hours - 160)
        return self.rate * (self.hours - overtime) + self.rate * 1.5 * overtime


class Commissioned(Salaried):
    def __init__(self, name, annual, sales, rate=0.05):
        super().__init__(name, annual)
        self.sales, self.rate = sales, rate

    def pay(self):
        return super().pay() + self.sales * self.rate


class Intern(Employee):
    pass


staff = [
    Salaried("Ana", 84000),
    Hourly("Ben", 25.0, 150),
    Hourly("Cleo", 30.0, 175),
    Commissioned("Dev", 48000, 120000),
]
print(f"{'Name':<8} {'Type':<14} {'Monthly':>10}")
for emp in staff:
    print(emp)
print(f"{'Total':<23} {sum(e.pay() for e in staff):>10.2f}")

try:
    print(Intern("Eve"))
except NotImplementedError as exc:
    print("error:", exc)

by_type = {}
for emp in staff:
    by_type.setdefault(type(emp).__name__, []).append(emp.name)
print("grouped:", by_type)
