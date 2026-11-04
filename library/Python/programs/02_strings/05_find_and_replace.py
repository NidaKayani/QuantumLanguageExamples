"""Search within strings using find, index, count, startswith and replace."""

text = "the cat sat on the mat with the hat"

print("find 'the':", text.find("the"))
print("rfind 'the':", text.rfind("the"))
print("find 'dog':", text.find("dog"))
print("count 'the':", text.count("the"))
print("count 'at':", text.count("at"))
print("'mat' in text:", "mat" in text)

try:
    text.index("dog")
except ValueError as e:
    print("index error:", e)

# find all occurrences
positions = []
start = 0
while (pos := text.find("at", start)) != -1:
    positions.append(pos)
    start = pos + 1
print("all 'at' positions:", positions)

print(text.replace("the", "a"))
print(text.replace("the", "THE", 2))

# chained replacements via a table
table = {"cat": "dog", "mat": "rug", "hat": "cap"}
result = text
for old, new in table.items():
    result = result.replace(old, new)
print(result)

filenames = ["report.pdf", "image.PNG", "notes.txt", "photo.jpg", "draft.doc"]
images = [f for f in filenames if f.lower().endswith((".png", ".jpg", ".gif"))]
print("images:", images)
print("starts with 'no':", [f for f in filenames if f.startswith("no")])
print("startswith at offset:", "xxabc".startswith("abc", 2))
