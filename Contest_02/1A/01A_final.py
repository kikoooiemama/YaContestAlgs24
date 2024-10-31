# Created by Nikolay Pakhomov 27.10.2024
with open("input.txt") as f:
    n = int(f.readline().strip())
    a = list(map(int, f.readline().split()))

s = 0
result = []
for i in range(n):
    s += a[i]
    result.append(s)
print(" ".join(map(str, result)))
