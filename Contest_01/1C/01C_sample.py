# Created by Nikolay Pakhomov 17.03.2024

# жадный алгоритм
n = int(input())
ans = 0
for i in range(n):
    a = int(input())
    ans += a // 4
    if a % 4 == 1 or a % 4 == 2:
        ans += a % 4
    if a % 4 == 3:
        ans += 2
print(ans)