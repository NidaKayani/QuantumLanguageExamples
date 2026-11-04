"""Type checks with isinstance and issubclass, including tuples of types and ABCs."""
from collections.abc import Sequence, Mapping, Iterable, Hashable, Callable


class Animal: pass
class Mammal(Animal): pass
class Dog(Mammal): pass
class Robot: pass


def classify(value):
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, (float, complex)):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, Mapping):
        return "mapping"
    if isinstance(value, Sequence):
        return "sequence"
    if isinstance(value, Iterable):
        return "iterable"
    if isinstance(value, Callable):
        return "callable"
    return "other"


rex = Dog()
print("rex is Dog/Mammal/Animal:", isinstance(rex, Dog), isinstance(rex, Mammal), isinstance(rex, Animal))
print("rex is Robot:", isinstance(rex, Robot))
print("rex is (Robot, Mammal):", isinstance(rex, (Robot, Mammal)))
print("Dog subclass of Animal:", issubclass(Dog, Animal), "| Animal of Dog:", issubclass(Animal, Dog))
print("everything is object:", issubclass(Robot, object), isinstance(3, object))
print("bool subclass of int:", issubclass(bool, int))

samples = [True, 42, 3.5, 2 + 1j, "hi", {"a": 1}, [1, 2], (3,), {4, 5}, len, None, range(3)]
for s in samples:
    print(f"{type(s).__name__:<17} -> {classify(s)}")

print("list hashable:", isinstance([], Hashable), "| tuple hashable:", isinstance((), Hashable))
print("type(rex) is Mammal:", type(rex) is Mammal, "| type(rex) is Dog:", type(rex) is Dog)
