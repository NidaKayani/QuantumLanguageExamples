"""Mixin classes that add reusable behavior (serialization, comparison, repr) to models."""
import json


class ReprMixin:
    def __repr__(self):
        fields = ", ".join(f"{k}={v!r}" for k, v in vars(self).items())
        return f"{type(self).__name__}({fields})"


class JsonMixin:
    def to_json(self):
        return json.dumps(vars(self), sort_keys=True)

    @classmethod
    def from_json(cls, text):
        return cls(**json.loads(text))


class CompareByKeyMixin:
    sort_key = ()

    def _key(self):
        return tuple(getattr(self, f) for f in self.sort_key)

    def __lt__(self, other):
        return self._key() < other._key()

    def __eq__(self, other):
        return type(self) is type(other) and vars(self) == vars(other)


class Book(ReprMixin, JsonMixin, CompareByKeyMixin):
    sort_key = ("author", "year")

    def __init__(self, title, author, year):
        self.title, self.author, self.year = title, author, year


class Song(ReprMixin, JsonMixin):
    def __init__(self, title, seconds):
        self.title, self.seconds = title, seconds


books = [
    Book("Dune", "Herbert", 1965),
    Book("Emma", "Austen", 1815),
    Book("Persuasion", "Austen", 1817),
    Book("Children of Dune", "Herbert", 1976),
]
for b in sorted(books):
    print(b)

text = books[0].to_json()
print("json:", text)
clone = Book.from_json(text)
print("round trip equal:", clone == books[0], "| same object:", clone is books[0])

song = Song("Blue in Green", 337)
print(song, song.to_json())
print("Song comparable?", hasattr(song, "__lt__") and Song.__lt__ is not object.__lt__)
print("Book MRO:", [c.__name__ for c in Book.__mro__])
