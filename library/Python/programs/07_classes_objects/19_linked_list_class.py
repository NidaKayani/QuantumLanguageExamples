"""A singly linked list class with append, prepend, reverse, iteration, and indexing."""


class Node:
    __slots__ = ("value", "next")

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, iterable=()):
        self.head = None
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

    def remove(self, value):
        prev, cur = None, self.head
        while cur:
            if cur.value == value:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                self._size -= 1
                return True
            prev, cur = cur, cur.next
        return False

    def reverse(self):
        prev, cur = None, self.head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        self.head = prev

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def __getitem__(self, index):
        if index < 0:
            index += self._size
        for i, value in enumerate(self):
            if i == index:
                return value
        raise IndexError("LinkedList index out of range")

    def __len__(self):
        return self._size

    def __repr__(self):
        return " -> ".join(map(str, self)) or "(empty)"


ll = LinkedList([3, 5, 7])
ll.prepend(1)
ll.append(9)
print(ll, "| len:", len(ll))
print("ll[2] =", ll[2], "| ll[-1] =", ll[-1])
ll.reverse()
print("reversed:", ll)
print("remove 5:", ll.remove(5), "| remove 42:", ll.remove(42))
print("now:", ll, "| sum:", sum(ll), "| 7 in ll:", 7 in ll)
try:
    ll[10]
except IndexError as exc:
    print("IndexError:", exc)
print("empty:", LinkedList())
