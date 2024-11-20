# Created by Nikolay Pakhomov 13.11.2024
# Неориентированное дерево (или просто дерево) – это конечный связный граф с выделенной вершиной (корнем) без циклов.
# Дерево не имеет петель и кратных рёбер.
# Вершина — точка, в которой две кривые, две прямые либо два ребра сходятся
def calculate_subtree_size(node):
    dad = tree[node][0]
    sons = tree[node][1]
    tree[node][2] = tree[node][2] + 1
    for son in sons:
        calculate_subtree_size(son)
    if dad is not None:
        tree[dad][2] = tree[dad][2] + tree[node][2]


# dad, sons, sub_size. dict - в 3.12 питоне упорядочены ключи
tree = {1: [None, [], 0]}
with open("input2.txt") as f:
    v = int(f.readline().strip())
    for i in range(v - 1):
        # одна из вершин новая - ее нужно добавить
        top_1, top_2 = map(int, f.readline().split())
        if tree.get(top_1, None) is None:
            tree[top_1] = [top_2, [], 0]
            tree[top_2][1].append(top_1)
        else:
            tree[top_2] = [top_1, [], 0]
            tree[top_1][1].append(top_2)

calculate_subtree_size(1)
print(f"{tree.pop(1)[2]}", end="")
for k in tree.keys():
    print(f" {tree.get(k)[2]}", end="")
