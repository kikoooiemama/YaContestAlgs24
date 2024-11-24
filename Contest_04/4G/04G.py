# Created by Nikolay Pakhomov 13.11.2024
# Дерева 2, поэтому всегда можно поменять деревья местами и тогда количество комбинаций УДВОИТСЯ.
# Понимаем как считать комбинации для дятлов на 2х деревьях без связи
# Понимаем как считать комбинации для дятлов, где двое с 1 связью
# Понимаем как считать комбинации для дятлов где, L с 1 связью


# Решения нет:
# - 2 дятла не могут иметь > 1 общих знакомых
# - 2 дятла, являющиеся знакомыми дятла Х, не могут быть знакомыми
# - 2 дятла, являющиеся знакомыми дятла Х, могут иметь только еще 1 знакомого, у которого есть знакомые.
# - У дятла есть 3 знакомых, у которых по 1.

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
# (2^b * П (sub_b_size_i!)) * (b + l)! * 2^l * (2l + (SUM b_size_i) + 2)^s
# П (sub_b_size_i!) * (b + l)! * 2^(l+b) * (2l + (SUM b_size_i) + 2)^s

# not only solos: (2^(b + l) * П (sub_b_size_i!)) * (b + l)! * (2l + (SUM b_size_i) + 2)^s  - обобщенная формула
# only solos, n==s: (s+1)!

# Trees == 1, t = 1:
# В tree может быть и subtree

# Вычисление факториала по модулю
def mod_fact(r, mod):
    result = j = 1
    while j < r + 1:
        result *= r % mod
        j += 1


# Считаем все комбинации для дерева
def calculate_for_tree():
    pass


# Считаем комбинации для всех дятлов
def calculate_combinations(n, mod, edges):
    pairs = {}
    branches = {}
    forest = {}
    structures = {}
    singles = set()
    for j in range(1, n + 1):
        singles.add(j)
    for el in edges:
        a, b = el[0], el[1]
        # dads, sons
        if structures.get(a, None) is None and structures.get(b, None) is not None:
            structures[a] = [b, set(), 0]
            structures[b][1].add(a)
        elif structures.get(b, None) is None and structures.get(a, None) is not None:
            structures[b] = [{a}, {a}, 0]
            structures[a][0].add(b)
            structures[a][1].add(b)
        elif structures.get(a, None) is None and structures.get(b, None) is None:
            structures[a] = [{b}, {b}, 0]
            structures[b] = [{a}, {a}, 0]
        else:
            structures[a][0].add(b)
            structures[a][1].add(b)
            structures[b][0].add(a)
            structures[b][1].add(a)


a_b = []
with open("input.txt") as f:
    # 1 <= n <= 10^6, 1 <= M <= 10^7 - количество пар знакомых дятлов, 1 <= k <= 2*10^6
    amount, m, k = map(int, f.readline().split())
    for i in range(m):
        first, second = map(int, f.readline().split())
        a_b.append((first, second))
print(calculate_combinations(amount, k, a_b))
