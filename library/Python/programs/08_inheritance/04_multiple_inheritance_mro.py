"""Multiple inheritance, the diamond problem, and C3 method resolution order."""


class Base:
    def greet(self):
        return ["Base"]


class Left(Base):
    def greet(self):
        return ["Left"] + super().greet()


class Right(Base):
    def greet(self):
        return ["Right"] + super().greet()


class Diamond(Left, Right):
    def greet(self):
        return ["Diamond"] + super().greet()


class Flipped(Right, Left):
    pass


def names(cls):
    return " -> ".join(c.__name__ for c in cls.__mro__)


print("Diamond MRO:", names(Diamond))
print("Diamond().greet():", Diamond().greet())
print("Flipped MRO:", names(Flipped))
print("Flipped().greet():", Flipped().greet())
print("Left().greet():", Left().greet())


class X: pass
class Y: pass
class A(X, Y): pass
class B(Y, X): pass

try:
    class C(A, B):
        pass
except TypeError as exc:
    print("TypeError:", exc)

class P1: value = "P1"
class P2: value = "P2"
class Child(P1, P2): pass

print("attribute from first parent:", Child.value)
print("mro() method:", [c.__name__ for c in Child.mro()])
