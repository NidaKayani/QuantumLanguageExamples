"""Attribute hooks: __getattr__ for dynamic lookups, __setattr__ for change tracking, __delattr__ guards."""


class AttrDict(dict):
    """Dictionary whose keys are also attributes, recursively."""

    def __getattr__(self, name):
        try:
            value = self[name]
        except KeyError:
            raise AttributeError(f"no setting named {name!r}") from None
        return AttrDict(value) if isinstance(value, dict) else value

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        del self[name]


class Tracked:
    def __init__(self, **values):
        object.__setattr__(self, "_changes", [])
        for k, v in values.items():
            setattr(self, k, v)
        self._changes.clear()

    def __setattr__(self, name, value):
        old = self.__dict__.get(name, "<unset>")
        if old != value:
            self._changes.append((name, old, value))
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        if name.startswith("_"):
            raise AttributeError(f"cannot delete internal attribute {name}")
        self._changes.append((name, self.__dict__[name], "<deleted>"))
        object.__delattr__(self, name)


class Proxy:
    """Forwards everything to a wrapped object while counting accesses."""

    def __init__(self, target):
        self._target = target
        self._hits = {}

    def __getattr__(self, name):
        self._hits[name] = self._hits.get(name, 0) + 1
        return getattr(self._target, name)


config = AttrDict({"db": {"host": "localhost", "port": 5432}, "debug": False})
print("db host:", config.db.host, "| port:", config.db.port)
config.debug = True
config.timeout = 30
print("after setattr:", dict(config))
del config.timeout
try:
    config.missing
except AttributeError as exc:
    print("AttributeError:", exc)

user = Tracked(name="ann", role="viewer", active=True)
user.role = "editor"
user.active = True
user.email = "ann@example.com"
del user.email
for change in user._changes:
    print("change:", change)
try:
    del user._changes
except AttributeError as exc:
    print("guarded:", exc)

words = Proxy(["delta", "alpha", "charlie"])
words.append("bravo")
words.sort()
print("proxied list:", words._target, "| count of alpha:", words.count("alpha"))
words.append("echo")
print("access counts:", dict(sorted(words._hits.items())))
print("getattr with default:", getattr(user, "nickname", "n/a"), "| hasattr role:", hasattr(user, "role"))
