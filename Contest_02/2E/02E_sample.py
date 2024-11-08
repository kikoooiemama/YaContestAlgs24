# Created by Nikolay Pakhomov 04.11.2024
with open("input.txt") as f:
    n = int(f.readline().strip())
    arr = list(map(int, f.readline().split()))

arr.sort()
ans = []
left = n // 2 - 1
right = n // 2
while len(ans) < n:
    if (n - len(ans)) % 2 == 1:
        ans.append(arr[right])
        right += 1
    else:
        ans.append(arr[left])
        left -= 1
print(*ans)
