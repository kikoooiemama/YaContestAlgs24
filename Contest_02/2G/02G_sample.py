# Created by Nikolay Pakhomov 04.11.2024
with open("input.txt") as f:
    n, c = map(int, f.readline().split())
    s = f.readline().strip()
cnt_a = 0
cnt_b = 0
badness = 0
ans = 0
right = 0
for left in range(n):
    while right < n and badness <= c:
        if s[right] == 'a':
            cnt_a += 1
        if s[right] == 'b':
            cnt_b += 1
            badness += cnt_a
        if badness > c:
            ans = max(ans, right - left)
        else:
            ans = max(ans, right - left + 1)
        right += 1
    if s[left] == 'a':
        cnt_a -= 1
        badness -= cnt_b
    if s[left] == 'b':
        cnt_b -= 1
print(ans)
