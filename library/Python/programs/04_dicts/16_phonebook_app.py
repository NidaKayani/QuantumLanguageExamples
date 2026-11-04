"""Implement a small phonebook with add, search, update and delete operations."""


class PhoneBook:
    def __init__(self):
        self.entries = {}

    def add(self, name, number, tags=()):
        if name in self.entries:
            raise ValueError(f"{name} already exists")
        self.entries[name] = {"number": number, "tags": set(tags)}

    def update(self, name, **changes):
        entry = self.entries[name]
        if "number" in changes:
            entry["number"] = changes["number"]
        if "tag" in changes:
            entry["tags"].add(changes["tag"])

    def remove(self, name):
        return self.entries.pop(name, None) is not None

    def search(self, text):
        text = text.lower()
        return {n: e for n, e in self.entries.items() if text in n.lower() or text in e["number"]}

    def by_tag(self, tag):
        return sorted(n for n, e in self.entries.items() if tag in e["tags"])

    def show(self):
        for name in sorted(self.entries):
            e = self.entries[name]
            tags = ",".join(sorted(e["tags"])) or "-"
            print(f"  {name:<14}{e['number']:<14}{tags}")


book = PhoneBook()
book.add("Ada Lovelace", "555-0101", ["work", "math"])
book.add("Alan Turing", "555-0199", ["work"])
book.add("Grace Hopper", "555-0142", ["navy"])
book.add("Ada Yonath", "555-0177")

try:
    book.add("Alan Turing", "000")
except ValueError as err:
    print("error:", err)

book.update("Ada Yonath", tag="science", number="555-0178")
print("all entries:")
book.show()
print("search 'ada':", sorted(book.search("ada")))
print("search '01':", sorted(book.search("01")))
print("tag work:", book.by_tag("work"))
print("removed Grace:", book.remove("Grace Hopper"), "| again:", book.remove("Grace Hopper"))
print("count:", len(book.entries))
