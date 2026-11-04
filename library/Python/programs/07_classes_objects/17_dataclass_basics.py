"""Dataclasses: generated __init__/__repr__/__eq__, defaults, ordering, and frozen instances."""
from dataclasses import dataclass, field, asdict, replace, astuple


@dataclass
class Item:
    name: str
    price: float
    quantity: int = 1
    tags: list[str] = field(default_factory=list)

    @property
    def total(self):
        return self.price * self.quantity


@dataclass(order=True, frozen=True)
class Coordinate:
    lat: float
    lon: float


@dataclass
class Order:
    order_id: int
    items: list[Item] = field(default_factory=list)
    note: str = field(default="", repr=False)

    def __post_init__(self):
        if self.order_id <= 0:
            raise ValueError("order_id must be positive")

    def grand_total(self):
        return sum(item.total for item in self.items)


pen = Item("Pen", 1.5, 10, ["office"])
book = Item("Book", 12.0)
print(pen)
print(book, "| total:", book.total)
print("equal:", Item("Pen", 1.5, 10, ["office"]) == pen)
print("asdict:", asdict(pen))
print("astuple:", astuple(book))
print("replace:", replace(book, quantity=3))

order = Order(7, [pen, book], note="gift")
print(order)
print("grand total:", order.grand_total())
try:
    Order(0)
except ValueError as exc:
    print("error:", exc)

places = [Coordinate(51.5, -0.1), Coordinate(40.7, -74.0), Coordinate(51.5, -0.2)]
print("sorted coords:", sorted(places))
try:
    places[0].lat = 0
except AttributeError as exc:
    print("frozen:", type(exc).__name__)
print("hashable:", len(set(places + [Coordinate(40.7, -74.0)])))
