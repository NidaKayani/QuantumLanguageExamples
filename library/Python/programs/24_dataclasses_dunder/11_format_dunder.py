"""Custom __format__, __str__ and __repr__ for money, durations and temperatures in f-strings."""
from decimal import Decimal


class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = Decimal(str(amount))
        self.currency = currency

    def __repr__(self):
        return f"Money({str(self.amount)!r}, {self.currency!r})"

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"

    def __format__(self, spec):
        symbols = {"USD": "$", "EUR": "EUR ", "JPY": "JPY "}
        if spec == "":
            return str(self)
        if spec == "sym":
            return f"{symbols.get(self.currency, '')}{self.amount:,.2f}"
        if spec == "acct":
            text = f"{abs(self.amount):,.2f}"
            return f"({text})" if self.amount < 0 else f" {text} "
        return format(self.amount, spec)


class Duration:
    def __init__(self, seconds):
        self.seconds = int(seconds)

    def __format__(self, spec):
        h, rem = divmod(self.seconds, 3600)
        m, s = divmod(rem, 60)
        if spec == "clock":
            return f"{h:02d}:{m:02d}:{s:02d}"
        if spec == "short":
            return " ".join(f"{v}{u}" for v, u in ((h, "h"), (m, "m"), (s, "s")) if v) or "0s"
        width = int(spec) if spec.isdigit() else 0
        return f"{self.seconds} seconds".rjust(width)

    def __repr__(self):
        return f"Duration({self.seconds})"


class Celsius:
    def __init__(self, degrees):
        self.degrees = degrees

    def __format__(self, spec):
        unit = spec[-1] if spec and spec[-1] in "CFK" else "C"
        number_spec = spec[:-1] if spec and spec[-1] in "CFK" else spec
        value = {"C": self.degrees, "F": self.degrees * 9 / 5 + 32, "K": self.degrees + 273.15}[unit]
        suffix = " K" if unit == "K" else f" deg{unit}"
        return format(value, number_spec or ".1f") + suffix


m = Money(-1234.5)
print(f"str: {m} | repr: {m!r} | sym: {m:sym} | acct: [{m:acct}] | raw: {m:>12.3f}")
for amount, cur in [(19.99, "USD"), (2500, "EUR"), (120000, "JPY")]:
    print(f"  {Money(amount, cur):sym}")
print("format() builtin:", format(Money(5), "acct"), "| str.format:", "{:sym}".format(Money(7.5)))

for secs in (0, 59, 3725, 86399):
    d = Duration(secs)
    print(f"{d!r:<16} clock={d:clock} short={format(d, 'short'):<10} padded=[{d:16}]")

t = Celsius(21.456)
print(f"{t} | {t:.2fC} | {t:F} | {t:.0fF} | {t:.3fK}")

rows = [("Coffee", Money(3.5)), ("Bagel", Money(2.25)), ("Refund", Money(-1.75))]
print(f"{'Item':<8}{'Amount':>12}")
for name, price in rows:
    print(f"{name:<8}{format(price, 'acct'):>12}")
