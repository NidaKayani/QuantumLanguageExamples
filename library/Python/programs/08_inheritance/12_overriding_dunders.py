"""Subclassing built-in types (dict, list, str) and overriding their special methods."""


class DefaultLowerDict(dict):
    """A case-insensitive dictionary with a default value for missing keys."""

    def __init__(self, default=None, **kwargs):
        super().__init__()
        self.default = default
        for k, v in kwargs.items():
            self[k] = v

    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)

    def __getitem__(self, key):
        return super().__getitem__(key.lower())

    def __missing__(self, key):
        return self.default

    def __contains__(self, key):
        return super().__contains__(key.lower())


class SortedList(list):
    def __init__(self, iterable=()):
        super().__init__(sorted(iterable))

    def append(self, item):
        import bisect
        bisect.insort(self, item)

    def extend(self, items):
        for item in items:
            self.append(item)


class Slug(str):
    def __new__(cls, text):
        slug = "-".join(text.lower().split())
        return super().__new__(cls, slug)

    def words(self):
        return self.split("-")


d = DefaultLowerDict(default=0, Apples=3)
d["BANANAS"] = 5
print("d['apples'] =", d["apples"], "| d['Bananas'] =", d["Bananas"], "| d['kiwi'] =", d["kiwi"])
print("'APPLES' in d:", "APPLES" in d, "| keys:", sorted(d))
print("isinstance dict:", isinstance(d, dict))

s = SortedList([5, 1, 4])
s.append(3)
s.extend([0, 9, 2])
print("sorted list:", s, "| len:", len(s), "| type:", type(s).__name__)

slug = Slug("  Hello Quantum   World ")
print("slug:", slug, "| words:", slug.words(), "| upper (plain str):", slug.upper())
print("is str:", isinstance(slug, str), "| type of slug.upper():", type(slug.upper()).__name__)
