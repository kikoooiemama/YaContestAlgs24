# Created by Nikolay Pakhomov 04.11.2024
with open("input.txt") as f:
    n, k = map(int, f.readline().split())
    arr = list(map(int, f.readline().split()))
arr.sort()
ans = 0
left, right = 0, 0
while left < n and right < n:
    if arr[right] - arr[left] <= k:
        ans = max(ans, right - left + 1)
        right += 1
    else:
        left += 1
print(ans)
