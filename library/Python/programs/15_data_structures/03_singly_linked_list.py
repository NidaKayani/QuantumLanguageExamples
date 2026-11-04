"""A singly linked list with iteration, insertion, deletion and reversal."""

from typing import Any, Iterator, Optional


class Node:
    __slots__ = ("value", "next")

    def __init__(self, value: Any, next: Optional["Node"] = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, iterable=()):
        self.head: Optional[Node] = None
        self._size = 0
        for item in iterable:
            self.append(item)

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self._size += 1

    def prepend(self, value):
        self.head = Node(value, self.head)
        self._size += 1

    def insert_after(self, target, value):
        for node in self._nodes():
            if node.value == target:
                node.next = Node(value, node.next)
                self._size += 1
                return True
        return False

    def remove(self, value):
        prev, cur = None, self.head
        while cur:
            if cur.value == value:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                self._size -= 1
                return
            prev, cur = cur, cur.next
        raise ValueError(f"{value!r} not in list")

    def reverse(self):
        prev, cur = None, self.head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        self.head = prev

    def _nodes(self) -> Iterator[Node]:
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def __iter__(self):
        return (n.value for n in self._nodes())

    def __len__(self):
        return self._size

    def __contains__(self, value):
        return any(v == value for v in self)

    def __repr__(self):
        return " -> ".join(map(repr, self)) + " -> None"


ll = LinkedList([3, 5, 8])
print(ll, "len", len(ll))
ll.prepend(1)
ll.append(13)
ll.insert_after(5, 6)
print(ll)
ll.remove(6)
ll.remove(1)
print("after removals:", ll)
print("contains 8:", 8 in ll, "contains 6:", 6 in ll)
ll.reverse()
print("reversed:", ll)
print("as list:", list(ll), "sum:", sum(ll))
try:
    ll.remove(42)
except ValueError as exc:
    print("error:", exc)
