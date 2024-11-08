# Created by Nikolay Pakhomov 04.11.2024

with open("input.txt") as f:
    n = int(f.readline().strip())
    a = list(map(int, f.readline().split()))
    b = list(map(int, f.readline().split()))
    p = list(map(int, f.readline().split()))

sorted_a = []
for i in range(n):
    sorted_a.append((a[i], b[i], i))
sorted_b = sorted_a[:]
sorted_a.sort(reverse=True, key=lambda x: (x[0], x[1], -x[2]))
sorted_b.sort(reverse=True, key=lambda x: (x[1], x[0], -x[2]))
a_pos = b_pos = 0
ans = []
used = set()
for i in range(n):
    if p[i] == 0:
        while sorted_a[a_pos][2] in used:
            a_pos += 1
        algo = sorted_a[a_pos][2]
        a_pos += 1
    else:
        while sorted_b[b_pos][2] in used:
            b_pos += 1
        algo = sorted_b[b_pos][2]
        b_pos += 1
    ans.append(algo + 1)
    used.add(algo)
print(*ans)
