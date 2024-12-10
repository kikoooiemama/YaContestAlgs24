# Created by Nikolay Pakhomov 13.11.2024
import sys

sys.setrecursionlimit(100000)


def get_dist(na):
    if dist[na] == -1:
        if name not in parents:
            dist[na] = 0
        else:
            dist[na] = get_dist(parents[name]) + 1
    return dist[na]


with open("input.txt") as f:
    n = int(f.readline())
    parents = {}
    dist = {}
    for i in range(n - 1):
        child, parent = f.readline().split()
        parents[child] = parent
        dist[child] = -1
        dist[parent] = -1
for name in dist:
    get_dist(name)
for name in sorted(dist.keys()):
    print(name, dist[name])
