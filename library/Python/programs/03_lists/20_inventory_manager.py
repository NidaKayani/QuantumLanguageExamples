"""Manage a small inventory with lists of tuples and list operations."""

inventory = [
    ("bolt", 120, 0.10),
    ("nut", 200, 0.05),
    ("washer", 15, 0.02),
    ("screw", 0, 0.08),
    ("bracket", 8, 2.50),
]


def report(items, title):
    print(f"-- {title} --")
    for name, qty, price in items:
        flag = " LOW" if qty < 20 else ""
        print(f"  {name:<8}{qty:>5} @ {price:>5.2f} = {qty * price:>7.2f}{flag}")
    print(f"  total value: {sum(q * p for _, q, p in items):.2f}")


report(inventory, "initial")

orders = [("bolt", 50), ("washer", 20), ("bracket", 3), ("gear", 1)]
for name, wanted in orders:
    for i, (item, qty, price) in enumerate(inventory):
        if item == name:
            if qty >= wanted:
                inventory[i] = (item, qty - wanted, price)
                print(f"shipped {wanted} {name}")
            else:
                print(f"backorder {name}: have {qty}, need {wanted}")
            break
    else:
        print(f"unknown item {name}")

inventory = [item for item in inventory if item[1] > 0]
inventory.append(("gear", 40, 1.25))
inventory.sort(key=lambda t: t[1] * t[2], reverse=True)
report(inventory, "after orders")

restock = [name for name, qty, _ in inventory if qty < 20]
print("needs restock:", restock)
