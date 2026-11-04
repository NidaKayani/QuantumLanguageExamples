"""collections.deque as a queue, bounded buffer, and rotating structure."""

from collections import deque

tickets = deque()
for customer in ["ann", "bob", "cid", "dee"]:
    tickets.append(customer)
    print(f"enqueue {customer:<4} -> {list(tickets)}")

while tickets:
    print(f"serving {tickets.popleft()}; waiting {list(tickets)}")

history = deque(maxlen=3)
for page in ["home", "about", "blog", "post-1", "post-2"]:
    history.append(page)
print("last three pages:", list(history), "maxlen:", history.maxlen)

d = deque(range(1, 8))
d.rotate(2)
print("rotate(2):", list(d))
d.rotate(-3)
print("rotate(-3):", list(d))
d.appendleft(0)
d.extendleft([-2, -1])
print("extendleft:", list(d))
print("index of 5:", d.index(5), "count of 3:", d.count(3), "d[0], d[-1]:", d[0], d[-1])


def josephus(n, k):
    circle = deque(range(1, n + 1))
    order = []
    while circle:
        circle.rotate(-(k - 1))
        order.append(circle.popleft())
    return order


elim = josephus(7, 3)
print("josephus(7, 3) elimination order:", elim, "survivor:", elim[-1])


def hot_potato(names, passes):
    q = deque(names)
    while len(q) > 1:
        q.rotate(-passes)
        out = q.pop()
        print(f"  {out} is out")
    return q[0]


print("hot potato winner:", hot_potato(["Al", "Bea", "Cy", "Di", "Ed"], 4))
