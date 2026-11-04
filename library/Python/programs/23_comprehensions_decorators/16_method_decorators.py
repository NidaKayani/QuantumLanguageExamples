"""staticmethod, classmethod and custom decorators applied to methods, including alternate constructors."""
from functools import wraps


def requires_open(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.is_open:
            raise RuntimeError(f"{method.__name__}() on closed {type(self).__name__}")
        return method(self, *args, **kwargs)
    return wrapper


def chainable(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        method(self, *args, **kwargs)
        return self
    return wrapper


class Date:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_iso(cls, text):
        return cls(*map(int, text.split("-")))

    @classmethod
    def from_ordinal_day(cls, year, n):
        month = 1
        while n > cls.days_in_month(year, month):
            n -= cls.days_in_month(year, month)
            month += 1
        return cls(year, month, n)

    @staticmethod
    def is_leap(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def days_in_month(year, month):
        if month == 2:
            return 29 if Date.is_leap(year) else 28
        return 30 if month in (4, 6, 9, 11) else 31

    def __repr__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"


class Ledger:
    def __init__(self):
        self.entries = []
        self.is_open = True

    @chainable
    @requires_open
    def add(self, label, amount):
        self.entries.append((label, amount))

    @requires_open
    def close(self):
        self.is_open = False
        return sum(a for _, a in self.entries)


print(Date.from_iso("2024-02-29"), Date.from_ordinal_day(2024, 60), Date.from_ordinal_day(2023, 60))
print("leap years:", [y for y in (1900, 2000, 2023, 2024, 2100) if Date.is_leap(y)])
print("February days:", {y: Date.days_in_month(y, 2) for y in (2023, 2024)})
print("called on instance:", Date(2020, 1, 1).is_leap(2020))

ledger = Ledger().add("rent", -1200).add("salary", 3000).add("food", -350)
print("entries:", ledger.entries)
print("closing balance:", ledger.close())
try:
    ledger.add("late", 5)
except RuntimeError as exc:
    print("error:", exc)
print("method names kept:", Ledger.add.__name__, Ledger.close.__name__)
print("types:", type(Date.__dict__["from_iso"]).__name__, type(Date.__dict__["is_leap"]).__name__)
