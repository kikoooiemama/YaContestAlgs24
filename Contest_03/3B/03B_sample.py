# Created by Nikolay Pakhomov 04.11.2024
with open("input.txt") as f:
    n = int(f.readline())
    nums = list(map(int, f.readline().split()))
ans = [-1] * n
stack = []
for i in range(n):
    while len(stack) > 0 and nums[i] < stack[-1][0]:
        ans[stack[-1][1]] = i
        stack.pop()
    stack.append((nums[i], i))
print(*ans)
