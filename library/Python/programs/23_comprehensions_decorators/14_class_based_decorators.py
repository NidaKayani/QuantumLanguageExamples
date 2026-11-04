"""Decorators implemented as classes with __call__, including ones that work on methods via __get__."""
import functools


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


class Validate:
    def __init__(self, **rules):
        self.rules = rules

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(**kwargs):
            errors = [f"{k}: {msg}" for k, (check, msg) in self.rules.items() if not check(kwargs.get(k))]
            if errors:
                return {"ok": False, "errors": errors}
            return {"ok": True, "value": func(**kwargs)}
        return wrapper


class Audited:
    """Descriptor-aware decorator so it also works on instance methods."""

    def __init__(self, func):
        self.func = func
        self.log = []
        functools.update_wrapper(self, func)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return functools.partial(self, instance)

    def __call__(self, instance, *args):
        self.log.append(f"{type(instance).__name__}.{self.func.__name__}{args}")
        return self.func(instance, *args)


@CountCalls
def hello(name):
    return f"hello {name}"


@Validate(name=(lambda v: isinstance(v, str) and v.strip(), "required"),
          age=(lambda v: isinstance(v, int) and 0 < v < 130, "must be 1-129"))
def create_user(name, age):
    return f"user {name} aged {age}"


class Cart:
    def __init__(self):
        self.items = []

    @Audited
    def add(self, item, qty=1):
        self.items.append((item, qty))
        return len(self.items)


for n in ("ann", "bob", "cy"):
    hello(n)
print("hello called", hello.count, "times; name:", hello.__name__)

print(create_user(name="Ann", age=33))
print(create_user(name="  ", age=200))
print(create_user(name="Bo", age=-1))

cart = Cart()
cart.add("apple", 3)
cart.add("pear")
print("cart items:", cart.items)
print("audit log:", Cart.add.log)
print("decorator object type:", type(Cart.__dict__["add"]).__name__)
