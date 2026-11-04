"""Use lists as stacks and collections.deque as queues to solve small problems."""

from collections import deque


def balanced(expr):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in expr:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


def eval_rpn(tokens):
    stack = []
    ops = {"+": lambda a, b: a + b, "-": lambda a, b: a - b,
           "*": lambda a, b: a * b, "/": lambda a, b: a / b}
    for tok in tokens.split():
        if tok in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[tok](a, b))
        else:
            stack.append(float(tok))
    return stack.pop()


for e in ("(a[b]{c})", "([)]", "((", "", "{[()()]}"):
    print(f"{e!r:12} balanced: {balanced(e)}")

for expr in ("3 4 +", "5 1 2 + 4 * + 3 -", "2 3 4 * +", "10 2 8 * + 3 -"):
    print(f"{expr:22} = {eval_rpn(expr)}")

# queue simulation: round-robin task scheduling
tasks = deque([("A", 5), ("B", 2), ("C", 4)])
quantum = 2
timeline = []
while tasks:
    name, remaining = tasks.popleft()
    run = min(quantum, remaining)
    timeline.append(f"{name}{run}")
    if remaining - run > 0:
        tasks.append((name, remaining - run))
print("schedule:", " ".join(timeline))

# a bounded history with maxlen
history = deque(maxlen=3)
for page in ["home", "about", "blog", "post-1", "post-2"]:
    history.append(page)
print("recent pages:", list(history))
d = deque(range(6))
d.rotate(2)
print("rotated deque:", list(d))
