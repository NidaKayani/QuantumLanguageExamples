"""A list-backed Stack class used for bracket matching and RPN evaluation."""

import operator


class StackEmptyError(Exception):
    pass


class Stack:
    def __init__(self, items=()):
        self._items = list(items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise StackEmptyError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise StackEmptyError("peek at empty stack")
        return self._items[-1]

    def __len__(self):
        return len(self._items)

    def __bool__(self):
        return bool(self._items)

    def __repr__(self):
        return f"Stack({self._items})"


PAIRS = {")": "(", "]": "[", "}": "{"}


def balanced(text):
    stack = Stack()
    for ch in text:
        if ch in "([{":
            stack.push(ch)
        elif ch in PAIRS:
            if not stack or stack.pop() != PAIRS[ch]:
                return False
    return not stack


OPS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


def eval_rpn(expr):
    stack = Stack()
    for tok in expr.split():
        if tok in OPS:
            b, a = stack.pop(), stack.pop()
            stack.push(OPS[tok](a, b))
        else:
            stack.push(float(tok))
    return stack.pop()


s = Stack([1, 2])
s.push(3)
print(s, "peek:", s.peek(), "len:", len(s))
print("popped:", s.pop(), s.pop(), s.pop())
try:
    s.pop()
except StackEmptyError as exc:
    print("error:", exc)

for text in ["(a[b]{c})", "([)]", "{{[]}}()", "((", ""]:
    print(f"{text!r:>12} balanced: {balanced(text)}")
for expr in ["3 4 + 2 *", "5 1 2 + 4 * + 3 -", "2 3 4 * 5 6 * + -", "10 4 /"]:
    print(f"{expr:<20} = {eval_rpn(expr):g}")
