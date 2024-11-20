# Created by Nikolay Pakhomov 13.11.2024
import sys


def print_tree(node):
    left, right, depth = tree[node][0][0], tree[node][0][1], "." * tree[node][1]
    if left is not None:
        print_tree(left)
    print(f"{depth}{node}")
    if right is not None:
        print_tree(right)


with open("input.txt") as f:
    requests = [string.strip() for string in f.readlines()]
tree = {}
sys.setrecursionlimit(100000)
for req in requests:
    if req.startswith("A"):
        v = int(req.split()[1])
        if tree.get(v, None) is not None:
            print("ALREADY")
            continue
        if not len(tree):
            tree[v] = [[None, None], 0]
            root = v
            print("DONE")
            continue
        print("DONE")
        node_i = root
        cur_depth = 0
        while node_i is not None:
            cur_node = tree[node_i]
            cur_depth += 1
            if v < node_i:
                if cur_node[0][0] is None:
                    cur_node[0][0] = v
                    tree[v] = [[None, None], cur_depth]
                    node_i = None
                else:
                    node_i = cur_node[0][0]
            else:
                if cur_node[0][1] is None:
                    cur_node[0][1] = v
                    tree[v] = [[None, None], cur_depth]
                    node_i = None
                else:
                    node_i = cur_node[0][1]

    elif req.startswith("S"):
        v = int(req.split()[1])
        print("NO") if tree.get(v, None) is None else print("YES")
    else:
        print_tree(root)
