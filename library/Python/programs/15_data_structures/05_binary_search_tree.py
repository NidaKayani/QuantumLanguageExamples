"""A binary search tree with insertion, lookup, deletion and traversals."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    key: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BST:
    def __init__(self, keys=()):
        self.root = None
        for k in keys:
            self.insert(k)

    def insert(self, key):
        def _ins(node):
            if node is None:
                return Node(key)
            if key < node.key:
                node.left = _ins(node.left)
            elif key > node.key:
                node.right = _ins(node.right)
            return node
        self.root = _ins(self.root)

    def __contains__(self, key):
        node = self.root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def delete(self, key):
        def _del(node, key):
            if node is None:
                return None
            if key < node.key:
                node.left = _del(node.left, key)
            elif key > node.key:
                node.right = _del(node.right, key)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                succ = node.right
                while succ.left:
                    succ = succ.left
                node.key = succ.key
                node.right = _del(node.right, succ.key)
            return node
        self.root = _del(self.root, key)

    def inorder(self):
        def _walk(node):
            if node:
                yield from _walk(node.left)
                yield node.key
                yield from _walk(node.right)
        return list(_walk(self.root))

    def height(self, node="root"):
        node = self.root if node == "root" else node
        return 0 if node is None else 1 + max(self.height(node.left), self.height(node.right))

    def floor(self, key):
        node, best = self.root, None
        while node:
            if node.key == key:
                return key
            if node.key < key:
                best, node = node.key, node.right
            else:
                node = node.left
        return best


tree = BST([50, 30, 70, 20, 40, 60, 80, 35, 45, 65])
print("inorder:", tree.inorder())
print("height:", tree.height())
print("contains 45:", 45 in tree, "contains 55:", 55 in tree)
print("floor(64):", tree.floor(64), "floor(10):", tree.floor(10))
for key in [20, 30, 50]:
    tree.delete(key)
    print(f"after deleting {key}: {tree.inorder()} root={tree.root.key}")
skewed = BST(range(1, 11))
print("height of tree built from sorted input:", skewed.height())
