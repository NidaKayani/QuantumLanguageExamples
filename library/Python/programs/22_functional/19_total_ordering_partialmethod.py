"""functools.total_ordering, partialmethod and cached_property on a small Money class."""
from functools import cached_property, partialmethod, total_ordering


@total_ordering
class Money:
    RATES = {"USD": 1.0, "EUR": 1.10, "GBP": 1.25}

    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    def in_usd(self):
        return self.amount * self.RATES[self.currency]

    def __eq__(self, other):
        return round(self.in_usd(), 6) == round(other.in_usd(), 6)

    def __lt__(self, other):
        return self.in_usd() < other.in_usd()

    def __repr__(self):
        return f"{self.amount:.2f} {self.currency}"

    def convert(self, currency):
        return Money(self.in_usd() / self.RATES[currency], currency)

    to_eur = partialmethod(convert, "EUR")
    to_gbp = partialmethod(convert, "GBP")


class Portfolio:
    def __init__(self, holdings):
        self.holdings = holdings
        self.computations = 0

    @cached_property
    def total_usd(self):
        self.computations += 1
        return sum(h.in_usd() for h in self.holdings)


wallet = [Money(100), Money(80, "EUR"), Money(50, "GBP"), Money(88), Money(70.4, "GBP")]
print("sorted:", sorted(wallet))
print("max:", max(wallet), "| min:", min(wallet))
a, b = Money(110), Money(100, "EUR")
print(f"{a} == {b}:", a == b, "| <=:", a <= b, "| >:", a > b, "| >=:", a >= b)
print("100 USD in EUR:", Money(100).to_eur(), "| in GBP:", Money(100).to_gbp())
print("88 USD vs 70.4 GBP equal?", Money(88) == Money(70.4, "GBP"))

portfolio = Portfolio(wallet)
print("total:", round(portfolio.total_usd, 2), round(portfolio.total_usd, 2))
print("computed", portfolio.computations, "time(s); cached in __dict__:", "total_usd" in vars(portfolio))
del portfolio.total_usd
print("after invalidation:", round(portfolio.total_usd, 2), "computations:", portfolio.computations)
