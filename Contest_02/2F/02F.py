# Created by Nikolay Pakhomov 27.10.2024
# Тупой алгоритм
def get_prefix_sum(sequence, mod):
    prefixsum = [0] * len(sequence + 1)
    for i in range(1, len(sequence) + 1):
        prefixsum[i] = prefixsum[i - 1] + sequence[i - 1]


def find_number_by_mod(n, a: list):
    i, j, k = 0
    r = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                pass
    return r


with open("input.txt") as f:
    nn = int(f.readline().strip())
    al = list(map(int, f.readline().split()))

# Сортировка O(n*log n)
al.sort()
ans = find_number_by_mod(nn, al)
print(ans)
