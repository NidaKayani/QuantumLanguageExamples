"""Dynamic attribute access with getattr/setattr/hasattr and __getattr__ fallbacks."""


class Record:
    def __init__(self, **fields):
        for key, value in fields.items():
            setattr(self, key, value)

    def __getattr__(self, name):
        # only called when normal lookup fails
        if name.startswith("get_"):
            field = name[4:]
            return lambda default=None: self.__dict__.get(field, default)
        raise AttributeError(f"{type(self).__name__} has no field {name!r}")

    def __repr__(self):
        body = ", ".join(f"{k}={v!r}" for k, v in sorted(vars(self).items()))
        return f"Record({body})"


class Shape:
    def area_square(self, s):
        return s * s

    def area_circle(self, r):
        return round(3.14159 * r * r, 3)

    def area_triangle(self, b, h):
        return b * h / 2


rec = Record(name="Widget", price=9.99, qty=4)
print(rec)
print("getattr:", getattr(rec, "price"), "| default:", getattr(rec, "color", "n/a"))
print("hasattr qty:", hasattr(rec, "qty"), "| hasattr color:", hasattr(rec, "color"))
print("dynamic getter:", rec.get_name(), rec.get_color("blue"))
setattr(rec, "qty", rec.qty + 6)
delattr(rec, "price")
print("updated:", rec)
try:
    rec.weight
except AttributeError as exc:
    print("AttributeError:", exc)

shape = Shape()
for kind, args in [("square", (4,)), ("circle", (2,)), ("triangle", (6, 3)), ("hexagon", (1,))]:
    method = getattr(shape, f"area_{kind}", None)
    print(f"{kind:<9}", method(*args) if method else "unsupported")
print("methods:", [m for m in dir(Shape) if m.startswith("area_")])
