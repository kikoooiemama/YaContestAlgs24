# Created by Nikolay Pakhomov 13.11.2024
import sys

sys.setrecursionlimit(1000000000)


def get_ans(num, is_root, father):
    global ans, bad
    if bad:
        return 0
    if is_root and len(g[num]) == 1 and len(g[g[num][0]]) > 1:
        get_ans(g[num][0], True, -1)
        return

    visited[num] = True
    cnt_big_childs = 0
    subtree_size = 1
    for child in g[num]:
        if bad:
            return 0
        if visited[child] and child != father:
            # нашли цикл.
            bad = True
            return 0
        elif not visited[child]:
            c_size = get_ans(child, False, num)
            subtree_size += c_size
            if c_size >= 2:
                cnt_big_childs += 1
            if (is_root and cnt_big_childs > 2) or (not is_root and cnt_big_childs > 1):
                bad = True
                return 0

    cnt_small_childs = len(g[num]) - cnt_big_childs - 1 + int(is_root)
    ans = (ans * factorial[cnt_small_childs]) % k
    if is_root:
        ans = (ans * 2) % k
        if (cnt_small_childs > 0 and cnt_big_childs > 0) or (cnt_big_childs == 2):
            ans = (ans * 2) % k
    return subtree_size


with open("input.txt") as f:
    n, m, k = map(int, f.readline().split())
    if m > n - 1:
        print(0)
    else:
        factorial = [1] * (n + 1)
        for i in range(2, n + 1):
            factorial[i] = (factorial[i - 1] * i) % k
        g = []
        bad = False
        ans = 1
        lonely = 0
        trees = 0
        visited = [False] * (n + 1)
        for i in range(n + 1):
            g.append([])
        for i in range(m):
            a, b = map(int, f.readline().split())
            g[a].append(b)
            g[b].append(a)
        for i in range(1, n + 1):
            if not visited[i] and len(g[i]) > 0:
                trees += 1
                get_ans(i, True, -1)
            if len(g[i]) == 0:
                lonely += 1
        if bad:
            print(0)
        else:
            ans = (ans * factorial[trees]) % k
            not_lonely = n - lonely
            for i in range(lonely):
                ans = (ans * (2 + not_lonely + i)) % k
            print(ans)
