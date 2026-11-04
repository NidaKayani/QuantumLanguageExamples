"""Model records with TypedDict and validate dictionaries against a schema."""

from typing import TypedDict, NotRequired


class Product(TypedDict):
    sku: str
    name: str
    price: float
    tags: NotRequired[list[str]]


catalog: list[Product] = [
    {"sku": "A-1", "name": "Lamp", "price": 29.99, "tags": ["home"]},
    {"sku": "B-7", "name": "Desk", "price": 149.0},
    {"sku": "C-3", "name": "Chair", "price": 89.5, "tags": ["home", "office"]},
]

SCHEMA = {"sku": str, "name": str, "price": (int, float)}


def validate(record):
    errors = []
    for field, kind in SCHEMA.items():
        if field not in record:
            errors.append(f"missing {field}")
        elif not isinstance(record[field], kind):
            errors.append(f"{field} has wrong type {type(record[field]).__name__}")
    extra = record.keys() - SCHEMA.keys() - {"tags"}
    if extra:
        errors.append(f"unexpected {sorted(extra)}")
    return errors


for p in catalog:
    print(f"{p['sku']}: {p['name']:<6} ${p['price']:>7.2f} tags={p.get('tags', [])}")

bad_records = [
    {"sku": "X", "name": "Thing"},
    {"sku": 9, "name": "Nine", "price": "free"},
    {"sku": "Y", "name": "Why", "price": 1, "color": "red"},
]
for r in bad_records + catalog[:1]:
    problems = validate(r)
    print(f"{r.get('sku')!r}: {'OK' if not problems else '; '.join(problems)}")

print("TypedDict is a dict at runtime:", type(catalog[0]) is dict)
print("required keys:", sorted(Product.__required_keys__))
print("optional keys:", sorted(Product.__optional_keys__))
print("total value:", round(sum(p["price"] for p in catalog), 2))
