"""Dict comprehensions for indexing, inverting, grouping and transforming mappings."""

products = [
    ("SKU-1", "keyboard", "peripherals", 49.99, 12),
    ("SKU-2", "mouse", "peripherals", 19.50, 40),
    ("SKU-3", "monitor", "displays", 189.00, 5),
    ("SKU-4", "webcam", "peripherals", 59.00, 0),
    ("SKU-5", "projector", "displays", 420.00, 2),
]

by_sku = {sku: name for sku, name, *_ in products}
print("by sku:", by_sku)

prices = {name: price for _, name, _, price, _ in products}
print("prices:", prices)

in_stock = {name: qty for _, name, _, _, qty in products if qty > 0}
print("in stock:", in_stock)

discounted = {name: round(p * 0.9, 2) if p > 50 else p for name, p in prices.items()}
print("discounted:", discounted)

inverted = {name: sku for sku, name in by_sku.items()}
print("inverted:", inverted)

categories = {cat for _, _, cat, *_ in products}
grouped = {cat: sorted(name for _, name, c, _, _ in products if c == cat) for cat in sorted(categories)}
print("grouped:", grouped)

stock_value = {cat: round(sum(p * q for _, _, c, p, q in products if c == cat), 2) for cat in grouped}
print("stock value per category:", stock_value)

text = "the rain in spain falls mainly on the plain"
letter_counts = {ch: text.count(ch) for ch in sorted(set(text)) if ch.isalpha()}
print("letter counts:", letter_counts)

squares = {n: n * n for n in range(1, 8)}
print("squares:", squares)
print("filtered by value:", {k: v for k, v in squares.items() if v % 2})

nested = {"a": {"x": 1, "y": 2}, "b": {"x": 3, "z": 4}}
flat = {f"{outer}.{inner}": v for outer, d in nested.items() for inner, v in d.items()}
print("flattened keys:", flat)

defaults = {"host": "localhost", "port": 8080, "debug": False}
overrides = {"port": 9000, "debug": True, "unused": 1}
merged = {k: overrides.get(k, v) for k, v in defaults.items()}
print("merged config:", merged)
print("position lookup:", {w: i for i, w in enumerate("alpha beta gamma delta".split())})
