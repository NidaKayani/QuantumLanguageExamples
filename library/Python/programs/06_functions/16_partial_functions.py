"""Partial application with functools.partial and partialmethod."""
from functools import partial, partialmethod


def power(base, exponent):
    return base ** exponent


def format_money(amount, currency="USD", places=2):
    return f"{amount:,.{places}f} {currency}"


class Light:
    def __init__(self):
        self.state = "off"

    def set_state(self, state):
        self.state = state
        return self

    turn_on = partialmethod(set_state, "on")
    turn_off = partialmethod(set_state, "off")


square = partial(power, exponent=2)
cube = partial(power, exponent=3)
two_to = partial(power, 2)

print("square(9) =", square(9))
print("cube(4) =", cube(4))
print("two_to(16) =", two_to(16))
print("partial info:", square.func.__name__, square.args, square.keywords)

euro = partial(format_money, currency="EUR")
yen = partial(format_money, currency="JPY", places=0)
print(euro(1234.5))
print(yen(98765.4))
print(euro(10, places=4))

parse_binary = partial(int, base=2)
parse_hex = partial(int, base=16)
print("binary 101101 ->", parse_binary("101101"))
print("hex ff ->", parse_hex("ff"))

lamp = Light()
print("lamp:", lamp.turn_on().state, "->", lamp.turn_off().state)

adders = [partial(lambda a, b: a + b, n) for n in range(4)]
print("adders applied to 10:", [f(10) for f in adders])
