"""Huffman coding: build a prefix-code tree with heapq, encode, decode, and measure compression."""
import heapq
from collections import Counter
from dataclasses import dataclass, field
from itertools import count
from typing import Optional


@dataclass(order=True)
class Node:
    weight: int
    tie: int
    symbol: Optional[str] = field(default=None, compare=False)
    left: Optional["Node"] = field(default=None, compare=False)
    right: Optional["Node"] = field(default=None, compare=False)


def build_tree(text):
    ids = count()
    heap = [Node(w, next(ids), sym) for sym, w in sorted(Counter(text).items())]
    heapq.heapify(heap)
    while len(heap) > 1:
        a, b = heapq.heappop(heap), heapq.heappop(heap)
        heapq.heappush(heap, Node(a.weight + b.weight, next(ids), None, a, b))
    return heap[0]


def assign_codes(node, prefix="", table=None):
    table = {} if table is None else table
    if node.symbol is not None:
        table[node.symbol] = prefix or "0"
    else:
        assign_codes(node.left, prefix + "0", table)
        assign_codes(node.right, prefix + "1", table)
    return table


def decode(bits, root):
    out, node = [], root
    for bit in bits:
        node = node.left if bit == "0" else node.right
        if node.symbol is not None:
            out.append(node.symbol)
            node = root
    return "".join(out)


def main():
    text = "this is an example of a huffman tree built from plain english text"
    root = build_tree(text)
    codes = assign_codes(root)
    freq = Counter(text)
    print(f"{'sym':>4} {'freq':>4}  code")
    for sym, code in sorted(codes.items(), key=lambda kv: (len(kv[1]), kv[1])):
        print(f"{sym!r:>4} {freq[sym]:>4}  {code}")
    bits = "".join(codes[ch] for ch in text)
    assert decode(bits, root) == text
    print(f"Original: {len(text) * 8} bits, encoded: {len(bits)} bits "
          f"({len(bits) / (len(text) * 8):.1%})")
    print(f"Average code length: {len(bits) / len(text):.3f} bits/symbol")
    print("First 64 encoded bits:", bits[:64])
    prefix_free = all(not b.startswith(a) for a in codes.values() for b in codes.values() if a != b)
    print("Prefix-free:", prefix_free)
    print("Single-symbol input codes:", assign_codes(build_tree("aaaa")))


if __name__ == "__main__":
    main()
