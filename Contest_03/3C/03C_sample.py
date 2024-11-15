# Created by Nikolay Pakhomov 04.11.2024
import collections

with open("input.txt") as f:
    n, k = map(int, f.readline().split())
    nums = list(map(int, f.readline().split()))
dq = collections.deque()
for i in range(n):
    if i >= k and nums[i - k] == dq[0]:
        dq.popleft()
    while len(dq) > 0 and dq[-1] > nums[i]:
        dq.pop()
    dq.append(nums[i])
    if i >= k - 1:
        print(dq[0])
