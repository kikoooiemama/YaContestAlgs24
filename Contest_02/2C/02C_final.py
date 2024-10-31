# Created by Nikolay Pakhomov 27.10.2024
def count_vars(n, r, d):
    ans = 0
    last = 0
    for i in range(n):
        while (last < n) and d[last] - d[i] <= r:
            last += 1
        ans += n - last
    return ans


with open("input.txt") as f:
    a, b = map(int, f.readline().split())
    m = list(map(int, f.readline().split()))

result = count_vars(a, b, m)
print(result)
