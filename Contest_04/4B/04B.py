# Created by Nikolay Pakhomov 13.11.2024
import sys


def calculate_sons(rt):
    n_sons = 0
    children = tree[rt][1]
    if len(children) > 0:
        for child in children:
            n_sons += calculate_sons(child) + 1
    else:
        return 0
    tree[rt][2] = n_sons
    return n_sons


sys.setrecursionlimit(100000)
with open("input.txt") as f:
    n = int(f.readline())
    # 0 - dad, 1 - sons, 2 - depth
    tree = {}
    root = set()
    for i in range(n - 1):
        son, dad = f.readline().split()
        tree[son] = tree.get(son, [dad, [], 0])
        if tree[son][0] is None:
            tree[son][0] = dad
            root.discard(son)
        tree[dad] = tree.get(dad, [None, [], 0])
        tree[dad][1].append(son)
        if tree[dad][0] is None:
            root.add(dad)
    root = root.pop()
    calculate_sons(root)
    for name in sorted(tree.keys()):
        print(name, tree[name][2])
