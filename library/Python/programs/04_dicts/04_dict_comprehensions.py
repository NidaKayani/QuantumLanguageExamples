"""Transform and filter data with dictionary comprehensions."""

squares = {n: n * n for n in range(1, 8)}
print("squares:", squares)

odd_squares = {n: sq for n, sq in squares.items() if n % 2}
print("odd squares:", odd_squares)

prices = {"coffee": 3.5, "tea": 2.75, "cake": 4.25, "water": 1.0}
with_tax = {item: round(price * 1.08, 2) for item, price in prices.items()}
print("with tax:", with_tax)

inverted = {v: k for k, v in {"a": 1, "b": 2, "c": 3}.items()}
print("inverted:", inverted)

words = ["level", "python", "kayak", "data", "noon"]
info = {w: {"len": len(w), "palindrome": w == w[::-1]} for w in words}
for w, d in info.items():
    print(f"  {w:<7} {d}")

category = {item: ("cheap" if p < 3 else "pricey") for item, p in prices.items()}
print("categories:", category)

# nested comprehension: multiplication table as dict of dicts
table = {i: {j: i * j for j in range(1, 4)} for i in range(1, 4)}
print("table:", table)
print("table[3][2] =", table[3][2])

# from two lists, keeping only matched pairs
keys = ["id", "name", "email", "phone"]
values = [7, "Lin", None, "555-0100"]
record = {k: v for k, v in zip(keys, values) if v is not None}
print("record:", record)

# character positions
text = "banana"
positions = {ch: [i for i, c in enumerate(text) if c == ch] for ch in sorted(set(text))}
print("positions:", positions)

lengths = {len(w) for w in words}
by_len = {n: sorted(w for w in words if len(w) == n) for n in sorted(lengths)}
print("by length:", by_len)
