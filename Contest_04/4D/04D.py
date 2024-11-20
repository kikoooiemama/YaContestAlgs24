# Created by Nikolay Pakhomov 13.11.2024
def print_tree(node):

    left = print_tree()
    print(left)
    right = print_tree


with open("input.txt") as f:
    requests = [string.strip() for string in f.readlines()]
print(requests)
tree = {}
for req in requests:
    if req.startswith("A"):
        v = int(req.split()[1])
        if tree.get(v, None) is None:
            print("ALREADY")
            continue
        if not len(tree):
            tree[v] = [None, [None, None], 0]
            continue
        print(v)
    elif req.startswith("S"):
        v = int(req.split()[1])
        print("YES") if tree.get(v, None) is None else print("NO")
    else:
        print_tree()
