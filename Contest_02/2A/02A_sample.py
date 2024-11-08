# Created by Nikolay Pakhomov 04.11.2024
with open("input.txt") as f:
    n = int(f.readline().strip())
    a = list(map(int, f.readline().split()))

b = [0] * (n + 1)
for i in range(1, n + 1):
    b[i] = b[i - 1] + a[i - 1]
print(*b[1:])
