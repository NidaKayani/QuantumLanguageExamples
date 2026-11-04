"""Reusable validating descriptors using __set_name__, __get__ and __set__."""


class Field:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name
        owner._fields = getattr(owner, "_fields", ()) + (name,)

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    def validate(self, value):
        pass


class Typed(Field):
    kind = object

    def validate(self, value):
        if not isinstance(value, self.kind):
            raise TypeError(f"{self.public_name} must be {self.kind.__name__}, got {type(value).__name__}")


class String(Typed):
    kind = str

    def __init__(self, min_len=0, max_len=None):
        self.min_len, self.max_len = min_len, max_len

    def validate(self, value):
        super().validate(value)
        if len(value) < self.min_len or (self.max_len and len(value) > self.max_len):
            raise ValueError(f"{self.public_name} length must be {self.min_len}..{self.max_len}")


class Number(Typed):
    kind = (int, float)

    def __init__(self, minimum=None, maximum=None):
        self.minimum, self.maximum = minimum, maximum

    def validate(self, value):
        if not isinstance(value, self.kind) or isinstance(value, bool):
            raise TypeError(f"{self.public_name} must be a number")
        if self.minimum is not None and value < self.minimum:
            raise ValueError(f"{self.public_name} must be >= {self.minimum}")
        if self.maximum is not None and value > self.maximum:
            raise ValueError(f"{self.public_name} must be <= {self.maximum}")


class OneOf(Field):
    def __init__(self, *options):
        self.options = set(options)

    def validate(self, value):
        if value not in self.options:
            raise ValueError(f"{self.public_name} must be one of {sorted(self.options)}")


class Product:
    name = String(min_len=2, max_len=20)
    price = Number(minimum=0)
    stock = Number(minimum=0, maximum=10_000)
    category = OneOf("food", "tools", "toys")

    def __init__(self, name, price, stock, category):
        self.name, self.price, self.stock, self.category = name, price, stock, category

    def __repr__(self):
        return "Product(" + ", ".join(f"{f}={getattr(self, f)!r}" for f in self._fields) + ")"


p = Product("hammer", 12.5, 40, "tools")
print(p)
print("declared fields:", Product._fields)
print("descriptor on class:", type(Product.price).__name__, Product.price.public_name)
print("stored privately:", sorted(vars(p)))

attempts = [("name", "x"), ("price", -3), ("price", "free"), ("stock", 20000),
            ("category", "garden"), ("stock", True), ("name", "mallet"), ("stock", 35)]
for attr, value in attempts:
    try:
        setattr(p, attr, value)
        print(f"set {attr}={value!r}: ok")
    except (TypeError, ValueError) as exc:
        print(f"set {attr}={value!r}: {type(exc).__name__}: {exc}")
print(p)
