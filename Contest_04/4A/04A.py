# Created by Nikolay Pakhomov 13.11.2024
# Идея: берем глубину из предка и делаем +1, если у предка нашелся свой предок,
# то проходимся рекурсивно по всем потомкам с + 1
def find_depth(rt, previous_depth):
    children = tree[rt][1]
    depth = previous_depth + 1
    for child in children:
        tree[child][2] = depth
        find_depth(child, depth)


with open("input2.txt") as f:
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
    find_depth(root, 0)
    for name in sorted(tree.keys()):
        print(name, tree[name][2])
