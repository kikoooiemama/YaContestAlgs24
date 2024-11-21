# Created by Nikolay Pakhomov 13.11.2024
import sys


def calculate_subtree_size(node):
    dad = tree[node][0]
    sons = tree[node][1]
    tree[node][2] = tree[node][2] + 1
    for son in sons:
        calculate_subtree_size(son)
    if dad is not None:
        tree[dad][2] = tree[dad][2] + tree[node][2]


def find_dad(node):
    sons = tree[node][1]
    for son in sons:
        tree[son][0] = node
        tree[son][1].discard(node)
        find_dad(son)


sys.setrecursionlimit(1000000000)
tree = {1: [None, set(), 0]}
with open("input.txt") as f:
    v = int(f.readline().strip())
    for i in range(v - 1):
        top_1, top_2 = map(int, f.readline().split())
        if tree.get(top_1, None) is None and tree.get(top_2, None) is not None:
            tree[top_1] = [None, {top_2}, 0]
            tree[top_2][1].add(top_1)
        elif tree.get(top_2, None) is None and tree.get(top_1, None) is not None:
            tree[top_2] = [None, {top_1}, 0]
            tree[top_1][1].add(top_2)
        elif tree.get(top_1, None) is None and tree.get(top_2, None) is None:
            tree[top_1] = [None, {top_2}, 0]
            tree[top_2] = [None, {top_1}, 0]
        else:
            tree[top_1][1].add(top_2)
            tree[top_2][1].add(top_1)

find_dad(1)
calculate_subtree_size(1)
print(f"{tree.pop(1)[2]}", end="")
for k in sorted(tree.keys()):
    print(f" {tree.get(k)[2]}", end="")
