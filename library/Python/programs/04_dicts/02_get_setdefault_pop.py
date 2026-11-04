"""Use get, setdefault, pop and popitem for safe dictionary access."""

stock = {"apples": 10, "pears": 0, "plums": 7}

print("get existing:", stock.get("apples"))
print("get missing:", stock.get("kiwis"))
print("get with default:", stock.get("kiwis", 0))
print("get falsy value:", stock.get("pears", "n/a"))

print("setdefault existing:", stock.setdefault("apples", 99))
print("setdefault new:", stock.setdefault("kiwis", 5))
print("stock now:", stock)

# grouping with setdefault
words = ["apple", "avocado", "banana", "blueberry", "cherry", "apricot"]
by_letter = {}
for w in words:
    by_letter.setdefault(w[0], []).append(w)
print("grouped:", by_letter)

print("pop existing:", stock.pop("pears"))
print("pop missing with default:", stock.pop("mangos", "none"))
try:
    stock.pop("mangos")
except KeyError as e:
    print("pop missing raises KeyError:", e)

print("popitem (LIFO):", stock.popitem())
print("remaining:", stock)

# counting with get
text = "mississippi"
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1
print("letter counts:", counts)

# draining a dict with popitem
queue = {"first": 1, "second": 2, "third": 3}
while queue:
    key, value = queue.popitem()
    print(f"  processed {key}={value}")
try:
    queue.popitem()
except KeyError as e:
    print("empty popitem:", e)
