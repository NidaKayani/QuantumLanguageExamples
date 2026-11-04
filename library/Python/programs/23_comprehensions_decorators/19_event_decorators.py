"""An event bus where handlers subscribe via decorators with filters, priorities and once-only flags."""
from collections import defaultdict


class EventBus:
    def __init__(self):
        self.handlers = defaultdict(list)

    def on(self, event, *, priority=0, when=None, once=False):
        def decorator(func):
            self.handlers[event].append({"func": func, "priority": priority, "when": when, "once": once})
            self.handlers[event].sort(key=lambda h: -h["priority"])
            return func
        return decorator

    def emit(self, event, **payload):
        results = []
        for handler in list(self.handlers[event]):
            if handler["when"] and not handler["when"](payload):
                continue
            results.append(handler["func"](**payload))
            if handler["once"]:
                self.handlers[event].remove(handler)
        return results


bus = EventBus()
audit = []


@bus.on("order", priority=10)
def validate(item, qty, user):
    return f"validated {qty}x {item}"


@bus.on("order", when=lambda p: p["qty"] >= 10)
def bulk_discount(item, qty, user):
    return f"bulk discount for {user}"


@bus.on("order", priority=5, once=True)
def welcome(item, qty, user):
    return f"first-order gift for {user}"


@bus.on("order", priority=-1)
def record(item, qty, user):
    audit.append((user, item, qty))
    return "recorded"


@bus.on("login", when=lambda p: p["user"].startswith("admin"))
def admin_alert(user):
    return f"ALERT admin login {user}"


orders = [("book", 1, "ann"), ("pen", 12, "bob"), ("ink", 3, "ann")]
for item, qty, user in orders:
    print(f"order {item}/{qty}/{user}:", bus.emit("order", item=item, qty=qty, user=user))

for user in ("ann", "admin_root"):
    print(f"login {user}:", bus.emit("login", user=user))

print("unknown event:", bus.emit("logout", user="ann"))
print("audit trail:", audit)
print("remaining order handlers:", [h["func"].__name__ for h in bus.handlers["order"]])
