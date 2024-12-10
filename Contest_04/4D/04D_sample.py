# Created by Nikolay Pakhomov 13.11.2024

import sys

sys.setrecursionlimit(100000)


def add(tree, param):
    while tree != [] and tree[0] != param:
        if param < tree[0]:
            tree = tree[1]
        elif param > tree[0]:
            tree = tree[2]
    if tree == []:
        tree.append(param)
        tree.append([])
        tree.append([])
        return True
    elif tree[0] == param:
        return False


def search(tree, param):
    while tree != [] and tree[0] != param:
        if param < tree[0]:
            tree = tree[1]
        elif param > tree[0]:
            tree = tree[2]
    return tree != []
    s


def print_tree(tree, depth):
    if tree != []:
        print_tree(tree[1], depth + 1)
        print('.' * depth, tree[0], sep='')
        print_tree(tree[2], depth + 1)


fin = open("input.txt", "r")
tree = []
for line in fin:
    line = line.strip()
    if line == 'PRINTTREE':
        print_tree(tree, 0)
    else:
        comm, param = line.split()
        param = int(param)
        if comm == 'ADD':
            if add(tree, param):
                print('DONE')
            else:
                print('ALREADY')
        if comm == 'SEARCH':
            if search(tree, param):
                print('YES')
            else:
                print('NO')
