"""Class decorators that add methods, auto-generate __repr__/__eq__, and enforce singletons."""


def auto_repr(*fields):
    def decorator(cls):
        def __repr__(self):
            args = ", ".join(f"{f}={getattr(self, f)!r}" for f in fields)
            return f"{cls.__name__}({args})"

        def __eq__(self, other):
            return type(self) is type(other) and all(getattr(self, f) == getattr(other, f) for f in fields)

        cls.__repr__ = __repr__
        cls.__eq__ = __eq__
        cls.__hash__ = None
        cls.fields = fields
        return cls
    return decorator


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    get_instance.__name__ = cls.__name__
    return get_instance


def add_comparisons(key):
    def decorator(cls):
        for name, op in [("__lt__", lambda a, b: a < b), ("__le__", lambda a, b: a <= b),
                         ("__gt__", lambda a, b: a > b), ("__ge__", lambda a, b: a >= b)]:
            setattr(cls, name, lambda self, other, op=op: op(key(self), key(other)))
        return cls
    return decorator


@add_comparisons(key=lambda p: (p.price, p.name))
@auto_repr("name", "price", "tags")
class Product:
    def __init__(self, name, price, tags=()):
        self.name = name
        self.price = price
        self.tags = tags


@singleton
class Settings:
    def __init__(self, theme="dark"):
        self.theme = theme
        self.loaded = 1


items = [Product("pen", 1.5), Product("book", 12.0, ("paper",)), Product("bag", 12.0)]
print(items)
print("fields:", Product.fields)
print("equal:", Product("pen", 1.5) == items[0], "| not equal:", items[1] == items[2])
print("sorted:", [p.name for p in sorted(items)])
print("pen < book:", items[0] < items[1], "| bag >= book:", items[2] >= items[1])

s1 = Settings("light")
s2 = Settings("ignored")
s2.loaded += 1
print("singleton same instance:", s1 is s2, "| theme:", s1.theme, "| loaded:", s1.loaded)
print("decorated class name:", Settings.__name__)
