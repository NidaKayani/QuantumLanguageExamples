"""Instance creation with __new__, singletons, interning caches, and copying objects."""
import copy


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialized = 0
        return cls._instance

    def __init__(self, name):
        self.name = name
        self.initialized += 1


class Color:
    _cache = {}

    def __new__(cls, name):
        key = name.lower()
        if key not in cls._cache:
            obj = super().__new__(cls)
            obj.name = key
            cls._cache[key] = obj
        return cls._cache[key]

    def __repr__(self):
        return f"Color({self.name!r})"


class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def __repr__(self):
        return f"Team({self.name!r}, {self.members})"


s1 = Singleton("first")
s2 = Singleton("second")
print("same object:", s1 is s2, "| name:", s1.name, "| init count:", s1.initialized)

red1, red2, blue = Color("Red"), Color("RED"), Color("blue")
print(red1, red2, blue, "| red1 is red2:", red1 is red2, "| cache size:", len(Color._cache))

original = Team("core", ["ann", "raj"])
shallow = copy.copy(original)
deep = copy.deepcopy(original)
shallow.members.append("li")
deep.members.append("zed")
deep.name = "fork"
print("original:", original)
print("shallow: ", shallow, "| shares list:", shallow.members is original.members)
print("deep:    ", deep, "| shares list:", deep.members is original.members)
