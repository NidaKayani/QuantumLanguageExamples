"""A parameter list mixing every kind of argument, exercised with many call shapes."""


def signature_demo(a, b=2, /, c=3, *args, d, e=5, **kwargs):
    return {"a": a, "b": b, "c": c, "args": args, "d": d, "e": e, "kwargs": kwargs}


def show(label, pos=(), kw=None):
    try:
        result = signature_demo(*pos, **(kw or {}))
        print(f"{label}: {result}")
    except TypeError as exc:
        print(f"{label}: TypeError: {exc}")


show("minimal", (1,), {"d": 4})
show("all positional", (1, 2, 3, 10, 11), {"d": 4})
show("c by keyword", (1,), {"c": 30, "d": 40})
show("extra kwargs", (1, 2), {"d": 4, "z": 26, "b": "kw-b"})
show("missing d", (1, 2, 3))
show("a by keyword", (), {"a": 1, "d": 4})
show("duplicate c", (1, 2, 3), {"c": 9, "d": 4})

code = signature_demo.__code__
n = code.co_argcount + code.co_kwonlyargcount
print("parameter names:", code.co_varnames[:n])
print("defaults:", signature_demo.__defaults__)
print("kwdefaults:", signature_demo.__kwdefaults__)
