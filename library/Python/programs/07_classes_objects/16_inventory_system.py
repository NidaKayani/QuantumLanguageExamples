"""A small inventory system combining several cooperating classes."""
from collections import defaultdict


class Product:
    def __init__(self, sku, name, price, category):
        self.sku, self.name, self.price, self.category = sku, name, price, category

    def __repr__(self):
        return f"Product({self.sku!r}, {self.name!r}, {self.price:.2f})"


class Inventory:
    def __init__(self):
        self._products = {}
        self._stock = defaultdict(int)

    def add_product(self, product, quantity=0):
        self._products[product.sku] = product
        self._stock[product.sku] += quantity

    def remove_stock(self, sku, quantity):
        if self._stock[sku] < quantity:
            raise ValueError(f"only {self._stock[sku]} of {sku} in stock")
        self._stock[sku] -= quantity

    def total_value(self):
        return sum(p.price * self._stock[sku] for sku, p in self._products.items())

    def by_category(self):
        groups = defaultdict(list)
        for p in self._products.values():
            groups[p.category].append(p.name)
        return {k: sorted(v) for k, v in sorted(groups.items())}

    def low_stock(self, threshold=5):
        return sorted(sku for sku, q in self._stock.items() if q < threshold)

    def __len__(self):
        return len(self._products)


inv = Inventory()
inv.add_product(Product("A1", "Keyboard", 49.99, "peripherals"), 10)
inv.add_product(Product("A2", "Mouse", 19.50, "peripherals"), 25)
inv.add_product(Product("B1", "Monitor", 189.00, "displays"), 4)
inv.add_product(Product("C1", "USB Cable", 5.25, "accessories"), 100)
inv.add_product(Product("C2", "Adapter", 12.00, "accessories"), 3)

print("products:", len(inv))
print(f"total value: {inv.total_value():.2f}")
print("by category:", inv.by_category())
print("low stock:", inv.low_stock())
inv.remove_stock("A1", 7)
print("after selling 7 keyboards, low stock:", inv.low_stock())
try:
    inv.remove_stock("B1", 10)
except ValueError as exc:
    print("error:", exc)
print(f"final value: {inv.total_value():.2f}")
