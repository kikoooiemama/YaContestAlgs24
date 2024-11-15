# Created by Nikolay Pakhomov 04.11.2024
with open("input.txt") as f:
    n, b = map(int, f.readline().split())
    a = list(map(int, f.readline().split()))

inq = ans = 0
for now in a:
    inq += now
    ans += inq
    inq -= min(inq, b)
ans += inq
print(ans)
