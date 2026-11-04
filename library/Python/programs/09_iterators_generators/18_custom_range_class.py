"""A float-friendly range class that is iterable, reversible, sized, and indexable."""
from fractions import Fraction


class FRange:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise ValueError("step must not be zero")
        self.start, self.stop, self.step = Fraction(start), Fraction(stop), Fraction(step)

    def __len__(self):
        n = (self.stop - self.start) / self.step
        return max(0, -(-n.numerator // n.denominator))

    def __getitem__(self, i):
        if i < 0:
            i += len(self)
        if not 0 <= i < len(self):
            raise IndexError("FRange index out of range")
        return self.start + i * self.step

    def __iter__(self):
        value = self.start
        while (value < self.stop) if self.step > 0 else (value > self.stop):
            yield value
            value += self.step

    def __reversed__(self):
        for i in range(len(self) - 1, -1, -1):
            yield self[i]

    def __contains__(self, x):
        offset = (Fraction(x) - self.start) / self.step
        return offset.denominator == 1 and 0 <= offset < len(self)


r = FRange(0, 1, Fraction(1, 4))
print("values:", [str(v) for v in r])
print("len:", len(r), "| r[1]:", r[1], "| r[-1]:", r[-1])
print("reversed:", [float(v) for v in reversed(r)])
print("0.5 in r:", 0.5 in r, "| 0.6 in r:", 0.6 in r)

down = FRange(3, 0, Fraction(-1, 2))
print("down:", [float(v) for v in down], "len", len(down))
print("sum of FRange(1, 2, 0.1):", float(sum(FRange(1, 2, Fraction(1, 10)))))
print("empty:", list(FRange(5, 1)), len(FRange(5, 1)))
try:
    r[10]
except IndexError as exc:
    print("IndexError:", exc)
print("enumerate:", [(i, float(v)) for i, v in enumerate(FRange(0, 1, 0.5))])
