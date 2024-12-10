# Created by Nikolay Pakhomov 13.11.2024
def get_cnt(name):
    if cnt[name] == -1:
        cnt[name] = 0
        if name in childs:
            for child in childs[name]:
                cnt[name] += get_cnt(child) + 1
    return cnt[name]


with open("input.txt") as f:
    n = int(f.readline())
    childs = {}
    cnt = {}
    for i in range(n - 1):
        child, parent = f.readline().split()
        if parent not in childs:
            childs[parent] = []
        childs[parent].append(child)
        cnt[child] = -1
        cnt[parent] = -1
for name in cnt:
    get_cnt(name)
for name in sorted(cnt.keys()):
    print(name, cnt[name])
