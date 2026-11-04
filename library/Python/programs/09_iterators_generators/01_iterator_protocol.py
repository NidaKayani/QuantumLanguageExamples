"""Implementing the iterator protocol by hand with __iter__ and __next__."""


class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


class Range2D:
    """An iterable (not an iterator) that yields fresh iterators each time."""

    def __init__(self, rows, cols):
        self.rows, self.cols = rows, cols

    def __iter__(self):
        return Range2DIterator(self.rows, self.cols)


class Range2DIterator:
    def __init__(self, rows, cols):
        self.rows, self.cols = rows, cols
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.rows * self.cols:
            raise StopIteration
        cell = divmod(self.index, self.cols)
        self.index += 1
        return cell


cd = Countdown(5)
print("countdown:", list(cd))
print("exhausted:", list(cd))

it = iter(Countdown(3))
print("manual next:", next(it), next(it), next(it))
print("default on exhaustion:", next(it, "done"))

grid = Range2D(2, 3)
print("first pass:", list(grid))
print("second pass:", [f"{r}{c}" for r, c in grid])

words = iter(["alpha", "beta", "gamma"])
while True:
    try:
        word = next(words)
    except StopIteration:
        print("loop finished")
        break
    print("  got", word)
print("iter(cd) is cd:", iter(cd) is cd, "| iter(grid) is grid:", iter(grid) is grid)
