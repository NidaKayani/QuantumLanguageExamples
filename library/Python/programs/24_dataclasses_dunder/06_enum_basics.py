"""enum.Enum with auto values, lookups, iteration, aliases, methods and the @unique decorator."""
from enum import Enum, auto, unique


@unique
class Suit(Enum):
    CLUBS = "C"
    DIAMONDS = "D"
    HEARTS = "H"
    SPADES = "S"

    @property
    def color(self):
        return "red" if self in (Suit.DIAMONDS, Suit.HEARTS) else "black"


class Status(Enum):
    PENDING = auto()
    ACTIVE = auto()
    SUSPENDED = auto()
    CLOSED = auto()
    DISABLED = 3  # alias of SUSPENDED

    def can_transition_to(self, other):
        allowed = {
            Status.PENDING: {Status.ACTIVE, Status.CLOSED},
            Status.ACTIVE: {Status.SUSPENDED, Status.CLOSED},
            Status.SUSPENDED: {Status.ACTIVE, Status.CLOSED},
            Status.CLOSED: set(),
        }
        return other in allowed[self]


class Planet(Enum):
    MERCURY = (3.303e23, 2.4397e6)
    EARTH = (5.976e24, 6.37814e6)
    JUPITER = (1.9e27, 7.1492e7)

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

    @property
    def surface_gravity(self):
        return 6.673e-11 * self.mass / self.radius ** 2


print("suits:", [s.name for s in Suit])
print("by value:", Suit("H"), "| by name:", Suit["SPADES"], "| color:", Suit.HEARTS.color)
print("member attributes:", Suit.CLUBS.name, Suit.CLUBS.value, repr(Suit.CLUBS))
print("membership:", Suit.HEARTS in Suit, "| count:", len(Suit))

print("statuses:", [(s.name, s.value) for s in Status])
print("alias resolves to:", Status.DISABLED, Status.DISABLED is Status.SUSPENDED)
print("all names incl. aliases:", list(Status.__members__))
for a, b in [(Status.PENDING, Status.ACTIVE), (Status.CLOSED, Status.ACTIVE), (Status.ACTIVE, Status.DISABLED)]:
    print(f"  {a.name} -> {b.name}: {a.can_transition_to(b)}")

for p in Planet:
    print(f"{p.name:<8} gravity={p.surface_gravity:6.2f} m/s^2")

try:
    Suit("X")
except ValueError as exc:
    print("bad lookup:", exc)
print("enum compare by identity:", Suit.HEARTS == Suit("H"), Suit.HEARTS != "H")
counts = {s: 0 for s in Suit}
for card in "AH KD 3S 9H QC 2H".split():
    counts[Suit(card[-1])] += 1
print("hand by suit:", {s.name: n for s, n in counts.items()})
