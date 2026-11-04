"""Class bodies as namespaces: nested classes, class-level computation, and __class__."""


class Config:
    BASE_URL = "https://api.example.com"
    VERSION = 2
    PREFIX = f"{BASE_URL}/v{VERSION}"
    # class-level names are not visible inside comprehensions, so bind PREFIX via a default
    ENDPOINTS = (lambda prefix=PREFIX: {n: f"{prefix}/{n}" for n in ("users", "orders")})()

    class Limits:
        max_requests = 100
        window_seconds = 60

        @classmethod
        def rate(cls):
            return cls.max_requests / cls.window_seconds

    class Retry:
        attempts = 3
        backoff = [2 ** i for i in range(3)]


class Node:
    created = 0

    def __init__(self, label):
        self.label = label
        type(self).created += 1

    def clone(self):
        return self.__class__(self.label + "'")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.label!r})"


class SpecialNode(Node):
    pass


print("endpoints:")
for name, url in Config.ENDPOINTS.items():
    print(f"  {name}: {url}")
print("rate:", round(Config.Limits.rate(), 4), "req/s")
print("retry backoff:", Config.Retry.backoff)
print("nested qualname:", Config.Limits.__qualname__)

n = Node("root")
s = SpecialNode("leaf")
print(n.clone(), s.clone())
print("Node.created:", Node.created, "| SpecialNode.created:", SpecialNode.created)
print("class name and module:", Node.__name__, Node.__module__)
