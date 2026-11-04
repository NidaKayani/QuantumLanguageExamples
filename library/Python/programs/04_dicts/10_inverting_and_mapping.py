"""Invert dictionaries, handle duplicate values, and map between key spaces."""

from collections import defaultdict

codes = {"US": "United States", "GB": "United Kingdom", "FR": "France", "DE": "Germany"}
names_to_codes = {name: code for code, name in codes.items()}
print("inverted:", names_to_codes)

# inversion with collisions groups keys into lists
fav_colors = {"ann": "blue", "ben": "green", "cat": "blue", "dan": "red", "eve": "green"}
by_color = defaultdict(list)
for person, color in fav_colors.items():
    by_color[color].append(person)
print("grouped inversion:", dict(by_color))

# naive inversion silently loses data
naive = {v: k for k, v in fav_colors.items()}
print("naive inversion (last wins):", naive)

# translation tables
morse = {"S": "...", "O": "---", "E": ".", "T": "-", "A": ".-", "N": "-."}
reverse_morse = {v: k for k, v in morse.items()}
encoded = " ".join(morse[c] for c in "SOS")
print("SOS ->", encoded, "->", "".join(reverse_morse[t] for t in encoded.split()))

# bidirectional lookups
status = {0: "pending", 1: "active", 2: "closed"}
status_ids = {v: k for k, v in status.items()}
print("status 1:", status[1], "| id of 'closed':", status_ids["closed"])

# map values through another dict (join)
orders = {101: "ann", 102: "ben", 103: "zed"}
emails = {"ann": "ann@example.com", "ben": "ben@example.com"}
for order_id, customer in orders.items():
    print(f"  order {order_id}: {emails.get(customer, '<no email>')}")

# compose two mappings
grade_points = {"A": 4, "B": 3, "C": 2}
student_grades = {"ann": "A", "ben": "C", "cat": "B"}
points = {s: grade_points[g] for s, g in student_grades.items()}
print("points:", points, "| GPA:", sum(points.values()) / len(points))
