"""Collecting validation errors across many records instead of failing on the first."""
from dataclasses import dataclass


class FieldError(ValueError):
    def __init__(self, field, message):
        super().__init__(f"{field}: {message}")
        self.field = field


@dataclass
class Order:
    order_id: str
    quantity: int
    unit_price: float
    country: str


def check_order(raw):
    errors = []
    def attempt(field, convert, check=None, message="invalid"):
        try:
            value = convert(raw[field])
        except KeyError:
            errors.append(FieldError(field, "missing"))
            return None
        except (TypeError, ValueError) as exc:
            errors.append(FieldError(field, f"cannot convert ({exc})"))
            return None
        if check and not check(value):
            errors.append(FieldError(field, message))
        return value

    oid = attempt("id", str, lambda s: s.startswith("ORD"), "must start with ORD")
    qty = attempt("qty", int, lambda q: q > 0, "must be positive")
    price = attempt("price", float, lambda p: p >= 0, "must not be negative")
    country = attempt("country", str.upper, lambda c: len(c) == 2, "must be a 2-letter code")
    if errors:
        return None, errors
    return Order(oid, qty, price, country), []


rows = [
    {"id": "ORD-1", "qty": "3", "price": "9.99", "country": "us"},
    {"id": "X-2", "qty": "0", "price": "5", "country": "DE"},
    {"id": "ORD-3", "qty": "two", "price": "-1", "country": "France"},
    {"id": "ORD-4", "price": "1.50"},
]
valid = []
for i, row in enumerate(rows, 1):
    order, errors = check_order(row)
    if errors:
        print(f"row {i}: {len(errors)} error(s)")
        for e in errors:
            print("   -", e)
    else:
        valid.append(order)
        print(f"row {i}: OK {order}")
print("valid totals:", [round(o.quantity * o.unit_price, 2) for o in valid])
