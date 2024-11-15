# Created by Nikolay Pakhomov 04.11.2024
def is_main(x):
    return x == a or x == b


def right(x):
    return (x - 1) % 4


def can_go(x):
    return len(qs[x]) > 0 and qs[x][0][0] <= time


qs = [[], [], [], []]
with open("input.txt") as f:
    n = int(f.readline())
    a, b = map(int, f.readline().split())
    a -= 1
    b -= 1
    for i in range(n):
        d, t = map(int, f.readline().split())
        qs[d - 1].append((t, i))
ans = [0] * n
for i in range(4):
    qs[i].sort()
time = 1
while n > 0:
    moves = [False] * 4
    for dir in range(4):
        if can_go(dir):
            t, idx = qs[dir][0]
            if is_main(dir) and is_main(right(dir)) and can_go(right(dir)):
                continue
            if not is_main(dir) and (can_go(right(dir)) or can_go(a) or can_go(b)):
                continue
            moves[dir] = True
    for i in range(4):
        if moves[i]:
            n-=1
            t, idx = qs[i].pop(0)
            ans[idx] = time
    time += 1
print(*ans, sep='\n')
