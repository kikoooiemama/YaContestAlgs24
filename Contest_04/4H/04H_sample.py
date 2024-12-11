# Created by Nikolay Pakhomov 13.11.2024
import sys

sys.setrecursionlimit(10000000)
INF = 10 ** 9 + 1


def cnt_cost(num, parent):
    if len(g[num]) == 1 and parent != -1:
        marked[num] = a[num]
        unmarked[num] = 0
        return
    nowcost = 0
    for child in g[num]:
        if child != parent:
            cnt_cost(child, num)
            nowcost += marked[child]
    unmarked[num] = nowcost
    nowcost = 0
    for child in g[num]:
        if child != parent:
            nowcost += min(marked[child], unmarked[child])
    marked[num] = nowcost + a[num]


def restore_ans(num, parent, is_mark):
    if is_mark:
        ans.append(num)
        for child in g[num]:
            if child != parent:
                if marked[child] < unmarked[child]:
                    restore_ans(child, num, True)
                else:
                    restore_ans(child, num, False)
    else:
        for child in g[num]:
            if child != parent:
                restore_ans(child, num, True)


with open("input.txt") as f:
    n = int(f.readline().strip())
    g = []
    for i in range(n + 1):
        g.append([])
    for i in range(n - 1):
        u, v = map(int, f.readline().split())
        g[u].append(v)
        g[v].append(u)
    a = [0] + list(map(int, f.readline().split()))
marked = [INF] * (n + 1)
unmarked = [INF] * (n + 1)
cnt_cost(1, -1)
if n == 1:
    unmarked[1] = INF
ans = []
if marked[1] < unmarked[1]:
    restore_ans(1, -1, True)
else:
    restore_ans(1, -1, False)
print(min(marked[1], unmarked[1]), len(ans))
print(*ans)
