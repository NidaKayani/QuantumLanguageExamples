"""Alternative constructors with @classmethod and utility helpers with @staticmethod."""
import json


class Date:
    def __init__(self, year, month, day):
        if not Date.is_valid(year, month, day):
            raise ValueError(f"invalid date {year}-{month}-{day}")
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_string(cls, text):
        year, month, day = map(int, text.split("-"))
        return cls(year, month, day)

    @classmethod
    def from_json(cls, payload):
        return cls(**json.loads(payload))

    @staticmethod
    def is_leap(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def is_valid(year, month, day):
        days = [31, 29 if Date.is_leap(year) else 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]
        return 1 <= month <= 12 and 1 <= day <= days[month - 1]

    def day_of_year(self):
        return sum(
            (31, 29 if self.is_leap(self.year) else 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31)[: self.month - 1]
        ) + self.day

    def __repr__(self):
        return f"Date({self.year:04d}-{self.month:02d}-{self.day:02d})"


class IsoDate(Date):
    def __repr__(self):
        return f"{self.year:04d}{self.month:02d}{self.day:02d}"


d1 = Date(2024, 3, 1)
d2 = Date.from_string("2023-12-31")
d3 = Date.from_json('{"year": 2000, "month": 2, "day": 29}')
for d in (d1, d2, d3):
    print(d, "day of year:", d.day_of_year())

print("leap years:", [y for y in range(1896, 1916) if Date.is_leap(y)])
print("valid 2023-02-29?", Date.is_valid(2023, 2, 29))
try:
    Date.from_string("2023-02-29")
except ValueError as exc:
    print("error:", exc)

iso = IsoDate.from_string("1969-07-20")
print("subclass constructor returns:", type(iso).__name__, iso)
print("static via instance:", d1.is_leap(1900))
