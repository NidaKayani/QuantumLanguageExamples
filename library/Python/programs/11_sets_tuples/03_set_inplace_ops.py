"""In-place set updates: |=, &=, -=, ^= and their method forms."""

inventory = {"bolt", "nut", "screw", "washer"}
print("start:", sorted(inventory))

inventory |= {"rivet", "nail"}
print("after |=:", sorted(inventory))

inventory &= {"bolt", "nut", "rivet", "nail", "glue"}
print("after &=:", sorted(inventory))

inventory -= {"nail"}
print("after -=:", sorted(inventory))

inventory ^= {"nut", "clip"}
print("after ^=:", sorted(inventory))

tags = set()
for sentence in ["red fast car", "blue slow car", "red slow bike"]:
    tags.update(sentence.split())
print("all tags:", sorted(tags))

tags.intersection_update("red blue green car bike".split())
print("colors+vehicles:", sorted(tags))

tags.difference_update({"car"})
print("without car:", sorted(tags))

tags.symmetric_difference_update({"bike", "train"})
print("toggled bike/train:", sorted(tags))

# alias vs copy behaviour
a = {1, 2, 3}
b = a
c = a.copy()
a |= {4}
print("alias sees change:", sorted(b), "| copy does not:", sorted(c))
