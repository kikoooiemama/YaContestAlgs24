# Created by Nikolay Pakhomov 27.10.2024
# Идея такая: рассматриваем не 8 случаев, а 4.
with open('input.txt') as f:
    x1, y1, x2, y2, x, y = list(map(int, f.readlines()))

ans = ""
if y > y2:
    ans += "N"
if y < y1:
    ans += "S"
if x < x1:
    ans += "W"
if x > x2:
    ans += "E"
print(ans)
