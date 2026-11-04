"""Defining __eq__ and __hash__ so objects work as set members and dict keys."""


class Card:
    RANKS = "23456789TJQKA"

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)

    def __hash__(self):
        return hash((self.rank, self.suit))

    def __repr__(self):
        return f"{self.rank}{self.suit}"


class Mutable:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return isinstance(other, Mutable) and self.value == other.value


a = Card("A", "s")
b = Card("A", "s")
c = Card("K", "h")
print("a == b:", a == b, "| a is b:", a is b, "| a == c:", a == c)
print("a == 'As':", a == "As")

hand = {a, b, c, Card("K", "h"), Card("2", "d")}
print("unique cards:", sorted(hand, key=lambda x: (Card.RANKS.index(x.rank), x.suit)))
counts = {}
for card in [a, b, c, Card("A", "s")]:
    counts[card] = counts.get(card, 0) + 1
print("counts:", counts)
print("lookup by equal key:", counts[Card("A", "s")])

print("Mutable has __hash__:", Mutable.__hash__)
try:
    {Mutable(1)}
except TypeError as exc:
    print("TypeError:", exc)
print("Mutable equality:", Mutable(3) == Mutable(3), Mutable(3) != Mutable(4))
