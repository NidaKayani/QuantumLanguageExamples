"""A skip list (with a deterministic level generator) used as an ordered set."""

MAX_LEVEL = 5


class LevelGen:
    """Tiny LCG so level choice is reproducible."""
    def __init__(self, seed=12345):
        self.state = seed

    def level(self):
        lvl = 1
        while lvl < MAX_LEVEL:
            self.state = (self.state * 1103515245 + 12345) % 2 ** 31
            if (self.state >> 16) % 2:
                break
            lvl += 1
        return lvl


class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * level


class SkipList:
    def __init__(self):
        self.head = Node(None, MAX_LEVEL)
        self.levels = LevelGen()
        self.size = 0

    def _path(self, key):
        update, node = [None] * MAX_LEVEL, self.head
        for lvl in reversed(range(MAX_LEVEL)):
            while node.forward[lvl] and node.forward[lvl].key < key:
                node = node.forward[lvl]
            update[lvl] = node
        return update

    def insert(self, key):
        update = self._path(key)
        nxt = update[0].forward[0]
        if nxt and nxt.key == key:
            return False
        new = Node(key, self.levels.level())
        for lvl in range(len(new.forward)):
            new.forward[lvl] = update[lvl].forward[lvl]
            update[lvl].forward[lvl] = new
        self.size += 1
        return True

    def __contains__(self, key):
        nxt = self._path(key)[0].forward[0]
        return nxt is not None and nxt.key == key

    def remove(self, key):
        update = self._path(key)
        target = update[0].forward[0]
        if not target or target.key != key:
            raise KeyError(key)
        for lvl in range(len(target.forward)):
            update[lvl].forward[lvl] = target.forward[lvl]
        self.size -= 1

    def range(self, lo, hi):
        node = self._path(lo)[0].forward[0]
        while node and node.key <= hi:
            yield node.key
            node = node.forward[0]

    def show(self):
        for lvl in reversed(range(MAX_LEVEL)):
            keys, node = [], self.head.forward[lvl]
            while node:
                keys.append(str(node.key))
                node = node.forward[lvl]
            print(f"  L{lvl}: " + " ".join(keys))


sl = SkipList()
for k in [30, 10, 50, 20, 70, 60, 40, 10, 80, 5]:
    sl.insert(k)
print("size:", sl.size)
sl.show()
print("contains 40:", 40 in sl, "contains 45:", 45 in sl)
print("range [15, 60]:", list(sl.range(15, 60)))
sl.remove(50)
print("after removing 50:", list(sl.range(0, 100)))
