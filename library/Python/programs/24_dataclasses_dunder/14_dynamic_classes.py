"""Building classes at runtime with type(), setattr and getattr from a schema description."""

SCHEMA = {
    "Book": {"fields": ["title", "author", "pages"], "defaults": {"pages": 0}, "base": None},
    "EBook": {"fields": ["size_mb"], "defaults": {"size_mb": 1.0}, "base": "Book"},
    "Magazine": {"fields": ["title", "issue"], "defaults": {}, "base": None},
}


def make_init(field_names, defaults, parent_fields):
    all_fields = parent_fields + field_names

    def __init__(self, *args, **kwargs):
        values = dict(zip(all_fields, args))
        values.update(kwargs)
        for name in all_fields:
            if name in values:
                setattr(self, name, values[name])
            elif name in defaults or name in getattr(type(self), "_defaults", {}):
                setattr(self, name, {**type(self)._defaults, **defaults}[name])
            else:
                raise TypeError(f"{type(self).__name__} missing field {name!r}")
    return __init__


def make_repr():
    def __repr__(self):
        parts = ", ".join(f"{f}={getattr(self, f)!r}" for f in type(self)._all_fields)
        return f"{type(self).__name__}({parts})"
    return __repr__


classes = {}
for name, spec in SCHEMA.items():
    base = classes[spec["base"]] if spec["base"] else object
    parent_fields = list(getattr(base, "_all_fields", []))
    namespace = {
        "_all_fields": parent_fields + spec["fields"],
        "_defaults": {**getattr(base, "_defaults", {}), **spec["defaults"]},
        "__init__": make_init(spec["fields"], spec["defaults"], parent_fields),
        "__repr__": make_repr(),
    }
    classes[name] = type(name, (base,), namespace)

Book, EBook, Magazine = classes["Book"], classes["EBook"], classes["Magazine"]
b = Book("Dune", "Herbert", 412)
e = EBook("Neuromancer", "Gibson", size_mb=2.4)
m = Magazine(title="Byte", issue=42)
print(b)
print(e)
print(m)
print("EBook MRO:", [c.__name__ for c in EBook.__mro__])
print("isinstance(e, Book):", isinstance(e, Book), "| issubclass(Magazine, Book):", issubclass(Magazine, Book))

setattr(Book, "summary", lambda self: f"{self.title} by {self.author}")
print("method added later:", b.summary(), "|", e.summary())

for attr in ("title", "pages", "size_mb", "isbn"):
    print(f"getattr(e, {attr!r}):", getattr(e, attr, "<missing>"))

counter = type("Counter", (), {"count": 0, "bump": lambda self: setattr(self, "count", self.count + 1) or self})
c = counter().bump().bump().bump()
print(type(c).__name__, "count =", c.count, "| class attr still", counter.count)
try:
    Magazine("Wired")
except TypeError as exc:
    print("TypeError:", exc)
