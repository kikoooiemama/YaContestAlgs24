# Created by Nikolay Pakhomov 04.11.2024
with open("input.txt") as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))
    m, k = map(int, f.readline().split())
    x = list(map(int, f.readline().split()))

left = 0
ans = [0] * n
moves = 0

for right in range(1, n):
    if a[right] == a[right - 1]:
        if moves < k:
            ans[right] = left
            moves += 1
        else:
            while moves >= k:
                if a[left] == a[left + 1]:
                    moves -= 1
                left += 1
            ans[right] = left
            moves += 1
    elif a[right] < a[right - 1]:
        left = right
        moves = 0

    ans[right] = left
to_print = []
for idx in x:
    to_print.append(ans[idx - 1] + 1)
print(*to_print)
