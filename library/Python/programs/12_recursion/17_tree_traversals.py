"""Recursive traversals and metrics on a binary tree built from tuples."""

from typing import Optional

# Tree node: (value, left, right) or None
Tree = Optional[tuple]

tree: Tree = ("F",
              ("B", ("A", None, None), ("D", ("C", None, None), ("E", None, None))),
              ("G", None, ("I", ("H", None, None), None)))


def preorder(t: Tree):
    if t:
        value, left, right = t
        yield value
        yield from preorder(left)
        yield from preorder(right)


def inorder(t: Tree):
    if t:
        value, left, right = t
        yield from inorder(left)
        yield value
        yield from inorder(right)


def postorder(t: Tree):
    if t:
        value, left, right = t
        yield from postorder(left)
        yield from postorder(right)
        yield value


def height(t: Tree) -> int:
    return 0 if t is None else 1 + max(height(t[1]), height(t[2]))


def leaves(t: Tree) -> list:
    if t is None:
        return []
    if t[1] is None and t[2] is None:
        return [t[0]]
    return leaves(t[1]) + leaves(t[2])


def mirror(t: Tree) -> Tree:
    return None if t is None else (t[0], mirror(t[2]), mirror(t[1]))


def paths(t: Tree, prefix=()):
    if t is None:
        return
    here = prefix + (t[0],)
    if t[1] is None and t[2] is None:
        yield "->".join(here)
    yield from paths(t[1], here)
    yield from paths(t[2], here)


def draw(t: Tree, indent: str = ""):
    if t is None:
        return
    draw(t[2], indent + "    ")
    print(indent + t[0])
    draw(t[1], indent + "    ")


print("preorder: ", " ".join(preorder(tree)))
print("inorder:  ", " ".join(inorder(tree)))
print("postorder:", " ".join(postorder(tree)))
print("height:", height(tree), "leaves:", leaves(tree))
print("mirrored inorder:", " ".join(inorder(mirror(tree))))
print("root-to-leaf paths:", list(paths(tree)))
print("sideways drawing:")
draw(tree)
