"""Process a list of dictionaries as a small in-memory table."""

books = [
    {"title": "Dune", "author": "Herbert", "year": 1965, "rating": 4.3, "pages": 412},
    {"title": "Neuromancer", "author": "Gibson", "year": 1984, "rating": 3.9, "pages": 271},
    {"title": "Foundation", "author": "Asimov", "year": 1951, "rating": 4.2, "pages": 255},
    {"title": "I, Robot", "author": "Asimov", "year": 1950, "rating": 4.1, "pages": 253},
    {"title": "Hyperion", "author": "Simmons", "year": 1989, "rating": 4.2, "pages": 482},
    {"title": "Snow Crash", "author": "Stephenson", "year": 1992, "rating": 4.0, "pages": 480},
]

print(f"{'Title':<14}{'Author':<12}{'Year':>6}{'Rating':>8}")
for b in sorted(books, key=lambda b: b["year"]):
    print(f"{b['title']:<14}{b['author']:<12}{b['year']:>6}{b['rating']:>8.1f}")

classics = [b["title"] for b in books if b["year"] < 1970]
print("\nbefore 1970:", classics)

top = max(books, key=lambda b: (b["rating"], -b["pages"]))
print("top rated:", top["title"])

total_pages = sum(b["pages"] for b in books)
print("total pages:", total_pages, "| average:", round(total_pages / len(books), 1))

by_decade = {}
for b in books:
    decade = b["year"] // 10 * 10
    by_decade.setdefault(decade, []).append(b["title"])
for decade in sorted(by_decade):
    print(f"{decade}s: {', '.join(by_decade[decade])}")

authors = sorted({b["author"] for b in books})
print("authors:", authors)

for b in books:
    b["long"] = b["pages"] > 400
print("long books:", [b["title"] for b in books if b["long"]])

ranked = sorted(books, key=lambda b: b["rating"], reverse=True)
for rank, b in enumerate(ranked[:3], 1):
    print(f"#{rank} {b['title']} ({b['rating']})")
