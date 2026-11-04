"""Binary tree traversals (in/pre/post/level order) written as generators."""
from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right


def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def inorder(node):
    if node:
        yield from inorder(node.left)
        yield node.value
        yield from inorder(node.right)


def preorder(node):
    if node:
        yield node.value
        yield from preorder(node.left)
        yield from preorder(node.right)


def postorder(node):
    if node:
        yield from postorder(node.left)
        yield from postorder(node.right)
        yield node.value


def level_order(root):
    queue = deque([(root, 0)])
    while queue:
        node, depth = queue.popleft()
        if node:
            yield depth, node.value
            queue.extend([(node.left, depth + 1), (node.right, depth + 1)])


root = None
for v in [50, 30, 70, 20, 40, 60, 80, 35, 65]:
    root = insert(root, v)

print("inorder:  ", list(inorder(root)))
print("preorder: ", list(preorder(root)))
print("postorder:", list(postorder(root)))
levels = {}
for depth, value in level_order(root):
    levels.setdefault(depth, []).append(value)
for depth, values in levels.items():
    print(f"level {depth}: {values}")
print("first value > 45 (lazy):", next(v for v in inorder(root) if v > 45))
