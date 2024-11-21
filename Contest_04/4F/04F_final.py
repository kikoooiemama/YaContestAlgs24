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


def calculate_profit(node):
    depth = tree[node][2]
    sons = tree[node][1]
    profit = 0
    for son in sons:
        profit += calculate_profit(son)
    profit += depth
    tree[node][3] = profit
    return profit


sys.setrecursionlimit(1000000000)
tree = {1: [None, [], 0, 0]}
with open("input.txt") as f:
    n = int(f.readline().strip())
    a = list(map(int, f.readline().split()))
    for i_n in range(2, n + 1):
        i = i_n - 2
        tree[i_n] = [a[i], [], 0, 0]
        tree[a[i]][1].append(i_n)

calculate_subtree_size(1)
calculate_profit(1)
print(f"{tree.pop(1)[3]}", end="")
for k in tree.keys():
    print(f" {tree.get(k)[3]}", end="")
