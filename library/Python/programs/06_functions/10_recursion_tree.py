"""Recursion over nested data: flattening, depth, tree sums, permutations, and Hanoi."""


def flatten(nested):
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item


def depth(nested):
    if not isinstance(nested, list):
        return 0
    return 1 + max((depth(x) for x in nested), default=0)


def tree_sum(node):
    """Sum a tree given as {'value': int, 'children': [...]}."""
    return node["value"] + sum(tree_sum(c) for c in node.get("children", []))


def permutations(seq):
    if len(seq) <= 1:
        return [seq]
    result = []
    for i, ch in enumerate(seq):
        for rest in permutations(seq[:i] + seq[i + 1:]):
            result.append(ch + rest)
    return result


def hanoi(n, src="A", dst="C", via="B", moves=None):
    if moves is None:
        moves = []
    if n:
        hanoi(n - 1, src, via, dst, moves)
        moves.append(f"{src}->{dst}")
        hanoi(n - 1, via, dst, src, moves)
    return moves


data = [1, [2, [3, [4, 5]], 6], (7, 8), [[[9]]]]
print("flatten:", list(flatten(data)))
print("depth:", depth([1, [2, [3, [4]]]]), depth([]), depth(5))

tree = {"value": 1, "children": [
    {"value": 2, "children": [{"value": 4}, {"value": 5}]},
    {"value": 3, "children": [{"value": 6}]},
]}
print("tree sum:", tree_sum(tree))
print("permutations of 'abc':", permutations("abc"))
moves = hanoi(3)
print(f"hanoi(3): {len(moves)} moves:", " ".join(moves))
