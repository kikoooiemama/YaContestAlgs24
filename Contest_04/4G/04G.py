# Created by Nikolay Pakhomov 13.11.2024
# Дерева 2, поэтому всегда можно поменять деревья местами и тогда количество комбинаций УДВОИТСЯ.
# Понимаем как считать комбинации для дятлов на 2х деревьях без связи
# Понимаем как считать комбинации для дятлов, где двое с 1 связью
# Понимаем как считать комбинации для дятлов где, L с 1 связью
# Если дятла 2 и они имеют 2х общих знакомых - ответа нет, т.к. это пересечение.
# У 2х дятлов может быть только 1 общий знакомый.

# Если N == 1, return 2
# Если в паре (1, 1) - один и тот же дятел -> ничего не делаем, знакомство не считаем.


# Only Solos: s, (s+1)!
# Lines == 1, Solos = s: s,
# Lines == l, Solos == s: (s, l), (2l+2))^s * (2^l * l!), где 2(l+1) - суммарное количество мест в 2х деревьях.
# Branch == 1: 2*(sub_b_size!)
# Branch == b: b! * П 2*(sub_b_size_i!) или b! * 2^b * П(sub_b_size_i!) ///(П от 1 до b)
# (по аналогии с sub_b_size^b), sub_b_size = b_size - 1, b_size - дятлов в ветке
# Branch == b, Solos == s: (s, b), места для solos = (SUM b_size_i) + 2
# ((SUM b_size_i) + 2)^s * (П 2*(sub_b_size_i!)) * b!  ///(SUM, П от 1 до b)
# Branch == b, Lines == l, Solos == s:
# (П 2*(sub_b_size_i!)) * (b + l)! * 2^l * (2l + (SUM b_size_i) + 2)^s - вот это верно скорее всего

# not only solos: (2^(b + l) * П (sub_b_size_i!)) * (b + l)! * (2l + (SUM b_size_i) + 2)^s  - обобщенная формула
# only solos, n==s: (s+1)!

# Trees == 1, t = 1:
# В tree может быть и subtree

def mod_fact(r, mod):
    result = j = 1
    while j < r + 1:
        result *= r % mod
        j += 1


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

singles = {}
pairs = {}
branches = {}
trees = {}
# Нужно научиться заполнять эти коллекции и следить за сложностью вычислений.

print(n, m, k)
print(sort_tree)
