# Created by Nikolay Pakhomov 04.11.2024
with open("input.txt") as f:
    n, r = map(int, f.readline().split())
    arr = list(map(int, f.readline().split()))

ans = 0
left = 0
right = 0
while left < n and right < n:
    while right < n and arr[right] - arr[left] <= r:
        right += 1
    ans += n - right
    left += 1
print(ans)
