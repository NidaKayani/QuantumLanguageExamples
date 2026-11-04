"""Running totals and scans with itertools.accumulate and various binary functions."""
from itertools import accumulate
import operator

data = [3, 1, 4, 1, 5, 9, 2, 6]
print("data:", data)
print("running sum:", list(accumulate(data)))
print("running product:", list(accumulate(data, operator.mul)))
print("running max:", list(accumulate(data, max)))
print("running min:", list(accumulate(data, min)))
print("with initial=100:", list(accumulate(data, initial=100)))

deposits = [100, -30, 250, -400, 75, -20]
balances = list(accumulate(deposits))
print("balances:", balances)
print("first overdraft at step:", next((i for i, b in enumerate(balances) if b < 0), None))

amortize = list(accumulate(range(5), lambda bal, _: round(bal * 1.05 - 100, 2), initial=1000))
print("loan balances:", amortize)

fib_pairs = accumulate(range(10), lambda pair, _: (pair[1], pair[0] + pair[1]), initial=(0, 1))
print("fibonacci via accumulate:", [p[0] for p in fib_pairs])

words = ["quantum", "language", "compiler"]
print("prefix concatenation:", list(accumulate(words, lambda a, b: a + "/" + b)))
