"""Doubly linked list with a sentinel node and O(1) operations at both ends."""


class _Node:
    __slots__ = ("value", "prev", "next")

    def __init__(self, value=None):
        self.value = value
        self.prev = self.next = self


class DoublyLinkedList:
    def __init__(self, items=()):
        self._sentinel = _Node()
        self._len = 0
        for item in items:
            self.push_back(item)

    def _insert_between(self, value, before, after):
        node = _Node(value)
        node.prev, node.next = before, after
        before.next = after.prev = node
        self._len += 1
        return node

    def _unlink(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        self._len -= 1
        return node.value

    def push_front(self, value):
        return self._insert_between(value, self._sentinel, self._sentinel.next)

    def push_back(self, value):
        return self._insert_between(value, self._sentinel.prev, self._sentinel)

    def pop_front(self):
        if not self._len:
            raise IndexError("pop from empty list")
        return self._unlink(self._sentinel.next)

    def pop_back(self):
        if not self._len:
            raise IndexError("pop from empty list")
        return self._unlink(self._sentinel.prev)

    def __iter__(self):
        node = self._sentinel.next
        while node is not self._sentinel:
            yield node.value
            node = node.next

    def __reversed__(self):
        node = self._sentinel.prev
        while node is not self._sentinel:
            yield node.value
            node = node.prev

    def __len__(self):
        return self._len

    def __str__(self):
        return "[" + " <-> ".join(map(str, self)) + "]"


dll = DoublyLinkedList("bcd")
dll.push_front("a")
dll.push_back("e")
print("list:", dll, "len", len(dll))
print("backwards:", list(reversed(dll)))
print("pop_front:", dll.pop_front(), "pop_back:", dll.pop_back())
print("now:", dll)

playlist = DoublyLinkedList(["intro", "verse", "chorus", "bridge", "outro"])
node = playlist._sentinel.next
moves = ["next", "next", "prev", "next", "next", "next"]
for move in moves:
    node = node.next if move == "next" else node.prev
    if node is playlist._sentinel:
        node = node.next if move == "next" else node.prev
    print(f"{move:>4}: now playing {node.value}")

while playlist:
    playlist.pop_back()
print("emptied playlist length:", len(playlist), str(playlist))
