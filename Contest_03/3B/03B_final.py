# Created by Nikolay Pakhomov 08.11.2024
# Задача на поиск ближайшего меньшего справа. Используем стеки.
with open("input.txt") as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))
ans = [-1] * n
stack = []
for i in range(0, n):
    if len(stack) == 0 or a[i - 1] < a[i]:
        stack.append((a[i], i))
        continue
    else:
        for j in range(len(stack) - 1, -1, -1):
            if stack[j][0] > a[i]:
                ans[stack[j][1]] = i
                stack.pop(-1)
                continue
            else:
                break
        stack.append((a[i], i))

print(*ans)
