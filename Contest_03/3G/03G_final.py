# Created by Nikolay Pakhomov 04.11.2024
with open("input.txt") as f:
    n, b = map(int, f.readline().split())
    a = list(map(int, f.readline().split()))
sum_time = a[0]
clients = a[0]
for i in range(1, n):
    clients -= b
    if clients < 0:
        clients = 0
    clients += a[i]
    sum_time += clients
clients -= b
if clients < 0:
    clients = 0
sum_time += clients
print(sum_time)
