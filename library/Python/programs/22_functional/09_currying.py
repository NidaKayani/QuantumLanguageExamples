"""A curry decorator based on inspect-free arity tracking, plus manual closures."""
from functools import wraps


def curry(arity):
    def decorator(func):
        @wraps(func)
        def curried(*args):
            if len(args) >= arity:
                return func(*args[:arity])
            return lambda *more: curried(*args, *more)
        return curried
    return decorator


@curry(3)
def volume(length, width, height):
    return length * width * height


@curry(2)
def add(a, b):
    return a + b


@curry(3)
def clamp(low, high, value):
    return max(low, min(high, value))


def adder(a):
    return lambda b: lambda c: a + b + c


print("volume(2)(3)(4) =", volume(2)(3)(4))
print("volume(2, 3)(4) =", volume(2, 3)(4))
print("volume(2)(3, 4) =", volume(2)(3, 4))
print("volume(2, 3, 4) =", volume(2, 3, 4))

base_two = volume(2)
slab = base_two(10)
print("slabs of 2x10 with heights 1..5:", [slab(h) for h in range(1, 6)])

increment = add(1)
print("map(add(1)):", list(map(increment, [10, 20, 30])))
print("map(add(100)):", list(map(add(100), range(3))))

percent = clamp(0, 100)
byte = clamp(0, 255)
values = [-20, 50, 130, 300]
print("clamp 0..100:", [percent(v) for v in values])
print("clamp 0..255:", [byte(v) for v in values])

print("manual closures:", adder(1)(2)(3), adder("a")("b")("c"))


def uncurry(f, n):
    def go(*args):
        result = f
        for a in args[:n]:
            result = result(a)
        return result
    return go


print("uncurried adder:", uncurry(adder, 3)(10, 20, 30))
print("name preserved:", volume.__name__, add.__name__)
