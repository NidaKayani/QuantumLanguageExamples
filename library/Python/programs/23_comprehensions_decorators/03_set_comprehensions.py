"""Set comprehensions and set algebra for deduplication and membership questions."""

emails = ["Ann@Example.com", "bob@example.com", "ann@example.com ", "CAROL@test.org",
          "bob@Example.com", "dave@test.org", "eve@sample.net"]

unique = {e.strip().lower() for e in emails}
print("unique emails:", sorted(unique))

domains = {e.split("@")[1] for e in unique}
print("domains:", sorted(domains))

sentence = "she sells sea shells by the sea shore"
print("distinct letters:", "".join(sorted({c for c in sentence if c.isalpha()})))
print("word lengths present:", sorted({len(w) for w in sentence.split()}))
print("words starting with s:", sorted({w for w in sentence.split() if w.startswith("s")}))

multiples_of_3 = {n for n in range(1, 50) if n % 3 == 0}
multiples_of_5 = {n for n in range(1, 50) if n % 5 == 0}
squares = {n * n for n in range(1, 8)}
print("multiples of 3 and 5:", sorted(multiples_of_3 & multiples_of_5))
print("3 or 5 count:", len(multiples_of_3 | multiples_of_5))
print("3 but not 5:", sorted(multiples_of_3 - multiples_of_5)[:8], "...")
print("exactly one of them:", len(multiples_of_3 ^ multiples_of_5))
print("squares that are multiples of 3:", sorted(squares & multiples_of_3))

courses = {
    "ann": {"math", "physics", "art"},
    "bob": {"math", "history"},
    "cat": {"art", "history", "music"},
    "dan": {"math", "physics"},
}
all_courses = {c for taken in courses.values() for c in taken}
print("all courses:", sorted(all_courses))
popular = {c for c in all_courses if sum(c in taken for taken in courses.values()) >= 2}
print("taken by 2+ students:", sorted(popular))
pairs_sharing = {frozenset((a, b)) for a in courses for b in courses
                 if a < b and courses[a] & courses[b]}
print("student pairs sharing a course:", sorted(tuple(sorted(p)) for p in pairs_sharing))
print("is dan's set a subset of ann's?", courses["dan"] <= courses["ann"])
print("disjoint bob/dan?", courses["bob"].isdisjoint(courses["dan"]))

sums = {a + b for a in range(1, 7) for b in range(1, 7)}
print("possible dice sums:", sorted(sums))
anagrams = {frozenset(w) for w in ["listen", "silent", "enlist", "google", "tinsel"]}
print("distinct letter-sets:", len(anagrams))
