# Created by Nikolay Pakhomov 04.11.2024
import collections


def sol():
    # добавляем максимум в дек. он будет по индексу 0
    def deq_app(x):
        while len(deq) > 0 and deq[-1] < x:
            deq.pop()
        deq.append(x)

    def deq_del(x):
        if x == deq[0]:
            deq.popleft()

    hw.sort()
    ans = hw[-1][0] - hw[0][0]
    deq = collections.deque()
    now_len = hw[0][1]
    right = 1
    for i in range(n):
        if hw[i][1] >= vasya:
            return 0
    for left in range(n - 1):
        while right < n and now_len < vasya:
            now_len += hw[right][1]
            deq_app(hw[right][0] - hw[right - 1][0])
            right += 1
        if now_len >= vasya:
            ans = min(ans, deq[0])
        now_len -= hw[left][1]
        deq_del(hw[left + 1][0] - hw[left][0])
    return ans


with open("input.txt") as f:
    n, vasya = map(int, f.readline().split())
    hw = list(zip(list(map(int, f.readline().split())), list(map(int, f.readline().split()))))

print(sol())
