# Created by Nikolay Pakhomov 13.11.2024
# Дерева 2, поэтому всегда можно поменять деревья местами и тогда количество комбинаций УДВОИТСЯ.
# Понимаем как считать комбинации для дятлов на 2х деревьях без связи
# Понимаем как считать комбинации для дятлов, где двое с 1 связью
# Понимаем как считать комбинации для дятлов где, L с 1 связью
# Если дятла 2 и они имеют 2х общих знакомых - ответа нет, т.к. это пересечение.
# У 2х дятлов может быть только 1 общий знакомый.
def mod_fact(r, mod):
    result = j = 1
    while j < r + 1:
        result *= r % mod
        j += 1


batches = {}
sort_tree = {}
with open("input.txt") as f:
    # 1 <= n <= 10^6, 1 <= M <= 10^7 - количество пар знакомых дятлов, 1 <= k <= 2*10^6
    n, m, k = map(int, f.readline().split())
    for i in range(1, n + 1):
        sort_tree[i] = []
    for i in range(m):
        a, b = map(int, f.readline().split())
        sort_tree[a].append(b)
        sort_tree[b].append(a)

print(n, m, k)
print(sort_tree)
