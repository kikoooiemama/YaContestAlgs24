# Created by Nikolay Pakhomov 13.11.2024
import sys

sys.setrecursionlimit(100000)


def cnt_money(num):
    size = 1
    for child in childs[num]:
        c_money, c_size = cnt_money(child)
        ans[num] += c_money + c_size
        size += c_size
    ans[num] += 1
    return ans[num], size


with open("input.txt") as f:
    n = int(f.readline().strip())
    bosses = list(map(int, f.readline().split()))

childs = []
ans = [0] * n
for i in range(n):
    childs.append([])
for i in range(n - 1):
    childs[bosses[i] - 1].append(i + 1)
cnt_money(0)
print(*ans)
