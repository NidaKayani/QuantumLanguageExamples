"""Composite data structures: dataclasses with dict/set indexes for an inventory."""

from collections import Counter, defaultdict
from dataclasses import dataclass, field, asdict
from decimal import Decimal


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    category: str
    price: Decimal
    tags: frozenset = frozenset()


@dataclass
class Inventory:
    products: dict = field(default_factory=dict)
    stock: Counter = field(default_factory=Counter)
    by_category: defaultdict = field(default_factory=lambda: defaultdict(set))
    by_tag: defaultdict = field(default_factory=lambda: defaultdict(set))

    def add(self, product: Product, qty: int = 0):
        self.products[product.sku] = product
        self.stock[product.sku] += qty
        self.by_category[product.category].add(product.sku)
        for tag in product.tags:
            self.by_tag[tag].add(product.sku)

    def sell(self, sku: str, qty: int) -> Decimal:
        if self.stock[sku] < qty:
            raise ValueError(f"only {self.stock[sku]} of {sku} left")
        self.stock[sku] -= qty
        return self.products[sku].price * qty

    def value(self) -> Decimal:
        return sum((p.price * self.stock[s] for s, p in self.products.items()), Decimal("0"))

    def find(self, category=None, tag=None):
        skus = set(self.products)
        if category:
            skus &= self.by_category[category]
        if tag:
            skus &= self.by_tag[tag]
        return sorted(skus)


inv = Inventory()
inv.add(Product("K-01", "Chef knife", "kitchen", Decimal("39.90"), frozenset({"steel", "gift"})), 12)
inv.add(Product("K-02", "Cutting board", "kitchen", Decimal("18.50"), frozenset({"wood"})), 30)
inv.add(Product("G-01", "Trowel", "garden", Decimal("9.99"), frozenset({"steel"})), 40)
inv.add(Product("G-02", "Planter", "garden", Decimal("24.00"), frozenset({"wood", "gift"})), 8)

print("stock value:", inv.value())
print("revenue from sales:", inv.sell("K-01", 2) + inv.sell("G-02", 3))
print("stock value after sales:", inv.value())
print("kitchen items:", inv.find(category="kitchen"))
print("gift items:", inv.find(tag="gift"))
print("steel garden items:", inv.find(category="garden", tag="steel"))
print("lowest stock:", min(inv.stock.items(), key=lambda kv: kv[1]))
try:
    inv.sell("G-02", 10)
except ValueError as exc:
    print("error:", exc)
p = asdict(inv.products["K-02"])
print("as dict:", {k: (sorted(v) if isinstance(v, frozenset) else str(v)) for k, v in p.items()})
