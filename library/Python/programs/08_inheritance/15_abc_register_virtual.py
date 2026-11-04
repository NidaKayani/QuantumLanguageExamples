"""Virtual subclasses via ABC.register and structural checks with __subclasshook__."""
from abc import ABC, abstractmethod


class Sized(ABC):
    @abstractmethod
    def size(self):
        ...

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Sized:
            if any("size" in vars(B) for B in C.__mro__):
                return True
        return NotImplemented


class Serializer(ABC):
    @abstractmethod
    def dumps(self, obj):
        ...


class Box:
    def __init__(self, items):
        self.items = items

    def size(self):
        return len(self.items)


class LegacyEncoder:
    def dumps(self, obj):
        return repr(obj)


class Stone:
    pass


Serializer.register(LegacyEncoder)

print("Box is Sized (structural):", issubclass(Box, Sized), isinstance(Box([1, 2]), Sized))
print("Stone is Sized:", issubclass(Stone, Sized))
print("LegacyEncoder is Serializer (registered):", issubclass(LegacyEncoder, Serializer))
print("Serializer in LegacyEncoder MRO:", Serializer in LegacyEncoder.__mro__)
enc = LegacyEncoder()
print("isinstance(enc, Serializer):", isinstance(enc, Serializer))
print("dumps:", enc.dumps({"k": [1, 2]}))

for obj in [Box("abc"), Stone(), Box([])]:
    if isinstance(obj, Sized):
        print(f"{type(obj).__name__} size = {obj.size()}")
    else:
        print(f"{type(obj).__name__} has no size")
