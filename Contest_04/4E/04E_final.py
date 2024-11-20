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


sys.setrecursionlimit(1000000000)
tree = {1: [None, [], 0]}
with open("input.txt") as f:
    v = int(f.readline().strip())
    for i in range(v - 1):
        top_1, top_2 = map(int, f.readline().split())
        if tree.get(top_1, None) is None and tree.get(top_2, None) is not None:
            tree[top_1] = [top_2, [], 0]
            tree[top_2][1].append(top_1)
        elif tree.get(top_2, None) is None and tree.get(top_1, None) is not None:
            tree[top_2] = [top_1, [], 0]
            tree[top_1][1].append(top_2)
        elif tree.get(top_2, None) is None and tree.get(top_1, None) is None:
            ##
            pass


calculate_subtree_size(1)
print(f"{tree.pop(1)[2]}", end="")
for k in tree.keys():
    print(f" {tree.get(k)[2]}", end="")
