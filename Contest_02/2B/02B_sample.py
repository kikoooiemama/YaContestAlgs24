# Created by Nikolay Pakhomov 04.11.2024
# поиск отрезков с нулевой суммы? идея от туда?
with open("input.txt") as f:
    n, k = map(int, f.readline().split())
    arr = list(map(int, f.readline().split()))

cnt = {0: 1}
now_sum = 0
ans = 0
for now in arr:
    now_sum += now
    ans += cnt.get(now_sum - k, 0)
    cnt[now_sum] = cnt.get(now_sum, 0) + 1
print(ans)
