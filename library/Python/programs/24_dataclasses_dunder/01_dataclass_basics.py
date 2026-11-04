"""Dataclass fundamentals: defaults, default_factory, generated __repr__/__eq__, and methods."""
from dataclasses import MISSING, dataclass, field, fields


@dataclass
class LineItem:
    sku: str
    description: str
    unit_price: float
    quantity: int = 1

    @property
    def total(self):
        return round(self.unit_price * self.quantity, 2)


@dataclass
class Order:
    order_id: int
    customer: str
    items: list[LineItem] = field(default_factory=list)
    tags: set[str] = field(default_factory=set)
    notes: str = ""

    def add(self, item: LineItem) -> "Order":
        self.items.append(item)
        return self

    @property
    def total(self):
        return round(sum(i.total for i in self.items), 2)


o1 = Order(1, "ann")
o1.add(LineItem("A1", "notebook", 3.25, 4)).add(LineItem("B7", "pen", 1.10, 10))
o1.tags.add("priority")
o2 = Order(2, "bob", notes="leave at door")

print(o1.items[0])
print(o2)
print("o1 total:", o1.total, "| item count:", len(o1.items))
print("o2 items list is independent:", o2.items, o1.items is not o2.items)

same = LineItem("A1", "notebook", 3.25, 4)
print("value equality:", same == o1.items[0], "| identity:", same is o1.items[0])
print("unequal when a field differs:", same == LineItem("A1", "notebook", 3.25, 5))

print("fields of Order:")
for f in fields(Order):
    if f.default is not MISSING:
        default = repr(f.default)
    elif f.default_factory is not MISSING:
        default = f"{f.default_factory.__name__}()"
    else:
        default = "required"
    print(f"  {f.name:<9} default={default}")

o2.items.append(LineItem("C3", "stapler", 12.0))
o2.customer = "robert"
print("mutated:", o2.customer, o2.total)
try:
    Order()
except TypeError as exc:
    print("missing args:", exc)
