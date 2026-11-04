"""Treating tuples as lightweight immutable records for reporting."""

from collections import defaultdict
from statistics import mean

ORDERS = (
    (1001, "alice", "widget", 3, 2.50),
    (1002, "bob", "gadget", 1, 12.00),
    (1003, "alice", "gadget", 2, 12.00),
    (1004, "carol", "widget", 10, 2.25),
    (1005, "bob", "doohickey", 5, 4.75),
    (1006, "carol", "gadget", 1, 11.50),
)

ID, CUSTOMER, ITEM, QTY, PRICE = range(5)

def line_total(order):
    return order[QTY] * order[PRICE]

print(f"{'id':>5} {'customer':<8} {'item':<10} {'qty':>3} {'total':>7}")
for order in ORDERS:
    print(f"{order[ID]:>5} {order[CUSTOMER]:<8} {order[ITEM]:<10} {order[QTY]:>3} {line_total(order):>7.2f}")

by_customer = defaultdict(list)
for order in ORDERS:
    by_customer[order[CUSTOMER]].append(order)

print()
for customer, orders in sorted(by_customer.items()):
    spent = sum(map(line_total, orders))
    items = tuple(sorted({o[ITEM] for o in orders}))
    print(f"{customer}: {len(orders)} orders, spent {spent:.2f}, items {items}")

biggest = max(ORDERS, key=line_total)
print("\nbiggest order:", biggest)
print("average unit price:", round(mean(o[PRICE] for o in ORDERS), 3))

item_totals = {}
for _, _, item, qty, _ in ORDERS:
    item_totals[item] = item_totals.get(item, 0) + qty
ranking = sorted(item_totals.items(), key=lambda kv: kv[1], reverse=True)
print("units by item:", ranking)
