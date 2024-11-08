# Created by Nikolay Pakhomov 04.11.2024
with open("input.txt") as f:
    n = int(f.readline().strip())
    arr = list(map(int, f.readline().split()))

mod = 10 ** 9 + 7
pref_sums = [0] * (n + 1)
for i in range(1, n + 1):
    pref_sums[i] = (pref_sums[i - 1] + arr[i - 1]) % mod
suff_sums = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    suff_sums[i] = (suff_sums[i + 1] + arr[i]) % mod
ans = 0
for now_pos in range(1, n - 1):
    ans = (ans + pref_sums[now_pos] * arr[now_pos] * suff_sums[now_pos + 1]) % mod
print(ans)
