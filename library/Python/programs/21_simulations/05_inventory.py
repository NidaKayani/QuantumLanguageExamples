"""Warehouse inventory with FIFO cost lots, reorder points and a daily order stream."""
from collections import defaultdict, deque
from dataclasses import dataclass


@dataclass
class Lot:
    qty: int
    unit_cost: float


class Inventory:
    def __init__(self, reorder_points):
        self.lots = defaultdict(deque)
        self.reorder_points = reorder_points
        self.cogs = 0.0
        self.backorders = defaultdict(int)

    def receive(self, sku, qty, cost):
        self.lots[sku].append(Lot(qty, cost))

    def on_hand(self, sku):
        return sum(lot.qty for lot in self.lots[sku])

    def ship(self, sku, qty):
        lots = self.lots[sku]
        while qty and lots:
            lot = lots[0]
            take = min(qty, lot.qty)
            lot.qty -= take
            qty -= take
            self.cogs += take * lot.unit_cost
            if lot.qty == 0:
                lots.popleft()
        if qty:
            self.backorders[sku] += qty

    def needs_reorder(self):
        return sorted(s for s, point in self.reorder_points.items() if self.on_hand(s) <= point)


inv = Inventory({"bolt": 50, "nut": 40, "gear": 5})
inv.receive("bolt", 100, 0.10)
inv.receive("nut", 80, 0.05)
inv.receive("gear", 12, 2.50)

days = [
    {"bolt": 30, "nut": 20},
    {"gear": 4, "bolt": 15},
    {"nut": 35, "gear": 5},
    {"bolt": 40, "gear": 6},
]
for day, orders in enumerate(days, 1):
    for sku, qty in orders.items():
        inv.ship(sku, qty)
    reorder = inv.needs_reorder()
    print(f"Day {day}: on hand", {s: inv.on_hand(s) for s in ("bolt", "nut", "gear")}, "reorder:", reorder)
    for sku in reorder:
        inv.receive(sku, inv.reorder_points[sku] * 2, {"bolt": 0.12, "nut": 0.06, "gear": 2.75}[sku])

print(f"Cost of goods sold: {inv.cogs:.2f}")
print("Backorders:", dict(inv.backorders))
for sku in sorted(inv.lots):
    print(sku, [(lot.qty, lot.unit_cost) for lot in inv.lots[sku]])
