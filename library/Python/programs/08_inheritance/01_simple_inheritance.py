"""Single inheritance: a base Animal class and subclasses overriding behavior."""


class Animal:
    def __init__(self, name, legs=4):
        self.name = name
        self.legs = legs

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} the {type(self).__name__.lower()} has {self.legs} legs and says {self.speak()!r}"


class Dog(Animal):
    def speak(self):
        return "Woof"

    def fetch(self, item):
        return f"{self.name} fetches the {item}"


class Cat(Animal):
    def speak(self):
        return "Meow"


class Bird(Animal):
    def __init__(self, name, can_fly=True):
        super().__init__(name, legs=2)
        self.can_fly = can_fly

    def speak(self):
        return "Tweet" if self.can_fly else "Squawk"


zoo = [Dog("Rex"), Cat("Tom"), Bird("Tweety"), Bird("Pingu", can_fly=False), Animal("Generic")]
for animal in zoo:
    print(animal.describe())

print(zoo[0].fetch("ball"))
print("Dog bases:", [b.__name__ for b in Dog.__bases__])
print("Bird MRO:", [c.__name__ for c in Bird.__mro__])
print("inherited method is same function:", Dog.describe is Animal.describe)
print("overridden:", Dog.speak is Animal.speak)
print("has fetch:", [hasattr(a, "fetch") for a in zoo])
