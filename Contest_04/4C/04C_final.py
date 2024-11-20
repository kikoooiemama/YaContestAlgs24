# Created by Nikolay Pakhomov 13.11.2024
import sys


def calculate_depth_and_time(rt, previous_depth):
    children = tree[rt][1]
    depth = previous_depth + 1
    start_time = time[0]
    time[0] = time[0] + 1
    for child in children:
        tree[child][2] = depth
        calculate_depth_and_time(child, depth)
    end_time = time[0]
    tree[rt][3] = (start_time, end_time)


def find_lca(s_a, s_b, node, res):
    s_node = tree[node][3]
    s_depth = tree[node][2]
    children = tree[node][1]
    if s_node[0] < s_a[0] and s_node[0] < s_b[0] and s_node[1] >= s_a[1] and s_node[1] >= s_b[1]:
        if s_depth > res[0]:
            res[0] = s_depth
            res[1] = node
            for child in children:
                find_lca(s_a, s_b, child, res)


def lca(a, b, rt):
    result = [-1, rt]
    s_a = tree[a][3]
    s_b = tree[b][3]
    if s_a[0] == s_b[0] and s_a[1] == s_b[1]:
        return a
    if s_a[0] > s_b[0] and s_a[1] <= s_b[1]:
        return b
    elif s_b[0] > s_a[0] and s_b[1] <= s_a[1]:
        return a
    else:
        find_lca(s_a, s_b, rt, result)
    return result[1]


sys.setrecursionlimit(1000000)
with open("input2.txt") as f:
    n = int(f.readline())
    tree = {}
    root = set()
    for i in range(n - 1):
        son, dad = f.readline().split()
        tree[son] = tree.get(son, [dad, [], 0, (0, 0)])
        if tree[son][0] is None:
            tree[son][0] = dad
            root.discard(son)
        tree[dad] = tree.get(dad, [None, [], 0, (0, 0)])
        tree[dad][1].append(son)
        if tree[dad][0] is None:
            root.add(dad)
    requests = [pair.strip().split() for pair in f.readlines()]
root = root.pop()

time = [0]
calculate_depth_and_time(root, 0)
for pair in requests:
    print(lca(pair[0], pair[1], root))
