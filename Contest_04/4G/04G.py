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
    if r == 0:
        return 1
    answer = j = 1
    while j < r + 1:
        answer = (answer * (j % mod)) % mod
        j += 1
    return answer


def mod_power(base, power, mod):
    if base == 0:
        return 0
    if power == 0:
        return 1
    answer = j = 1
    while j < power + 1:
        answer = (answer * (base % mod)) % mod
        j += 1
    return answer


def rec_find_subtree_one(rt, structures, mod):
    combs_one = 1
    sons = structures[rt][1]
    tree_one = [[], set()]
    structures.pop(rt)
    for son in sons:
        if not isinstance(structures[son][0], set):
            return -1
        structures[son][0] = rt
        grandsons = structures[son][1]
        grandsons.discard(rt)
        if len(grandsons) > 0:
            tree_one[0].append(son)
            if len(tree_one[0]) > 1:
                return -1
        else:
            tree_one[1].add(son)
            structures.pop(son)
    if len(tree_one[0]) == 1:
        sub_tree_one_by_mod = rec_find_subtree_one(tree_one[0][0], structures, mod)
        if sub_tree_one_by_mod == -1:
            return -1
        combs_one = sub_tree_one_by_mod
    combs_one = (combs_one * mod_fact(len(tree_one[1]), mod))
    combs_one = (combs_one * (2 % mod)) % mod
    return combs_one


def rec_find_subtree_one_pr(rt, structures, mod):
    combs_pr = 1
    sons = structures[rt][1]
    tree_pr = [[], set()]
    structures.pop(rt)
    for son in sons:
        if not isinstance(structures[son][0], set):
            return -1
        structures[son][0] = rt
        grandsons = structures[son][1]
        grandsons.discard(rt)
        if len(grandsons) > 0:
            tree_pr[0].append(son)
            if len(tree_pr[0]) > 2:
                return -1
        else:
            tree_pr[1].add(son)
            structures.pop(son)
    if len(tree_pr[0]) == 2:
        for sub_tree in tree_pr[0]:
            sub_tree_combs_by_mod = rec_find_subtree_one(sub_tree, structures, mod)
            if sub_tree_combs_by_mod == -1:
                return -1
            combs_pr = (combs_pr * sub_tree_combs_by_mod) % mod
        combs_pr = (combs_pr * (2 % mod)) % mod
    elif len(tree_pr[0]) == 1:
        sub_tree = tree_pr[0][0]
        sub_combs = rec_find_subtree_one(sub_tree, structures, mod)
        if sub_combs == -1:
            return -1
        combs_pr = (combs_pr * sub_combs) % mod
        combs_pr = (combs_pr * (2 % mod)) % mod
    combs_pr = (combs_pr * mod_fact(len(tree_pr[1]) + 1, mod)) % mod
    return combs_pr


# Считаем все комбинации для дерева
def find_tree(root, structures, mod):
    combs = 1
    sons = structures[root][1]
    structures.pop(root)
    tree = [[], set()]
    for son in sons:
        if not isinstance(structures[son][0], set):
            return -1
        structures[son][0] = root
        grandsons = structures[son][1]
        grandsons.discard(root)
        if len(grandsons) > 0:  # есть потомки
            tree[0].append(son)
            if len(tree[0]) > 2:  # у дятла есть 3 знакомых, у которых по 1 знакомому.
                return -1
        else:
            tree[1].add(son)
            structures.pop(son)
    # в зависимости от того, сколько сыновей у корня, делаем то или иное.
    if len(tree[0]) == 2:
        # нужно найти для каждого по
        for sub_tree in tree[0]:
            sub_tree_combs_by_mod = rec_find_subtree_one(sub_tree, structures, mod)
            if sub_tree_combs_by_mod == -1:
                return -1
            combs = (combs * sub_tree_combs_by_mod) % mod
        combs = (combs * (2 % mod)) % mod
        combs = (combs * mod_fact(len(tree[1]), mod)) % mod
    # У корня 1 ветка.
    elif len(tree[0]) == 1:
        sub_tree = tree[0][0]
        if len(tree[1]):
            # вариант x <- 1 -> 3 -> 4
            sub_combs = rec_find_subtree_one(sub_tree, structures, mod)
            if sub_combs == -1:
                return -1
            combs = (combs * sub_combs) % mod
            combs = (combs * mod_fact(len(tree[1]), mod)) % mod
            combs = (combs * (2 % mod)) % mod
        else:
            # 1 -> 3 -> 4
            sub_combs = rec_find_subtree_one_pr(sub_tree, structures, mod)
            if sub_combs == -1:
                return -1
            combs = (combs * sub_combs) % mod
    # Дерево - ветка.
    elif tree[0] == 0:
        combs = (combs * mod_fact(len(tree[1]), mod)) % mod
        combs = (combs * (2 % mod)) % mod
    return combs


# Считаем комбинации для всех дятлов
def calculate_combinations(n, mod, edges):
    if n == 1:
        return 2
    structures = {}
    singles = set()
    for j in range(1, n + 1):
        singles.add(j)
    for el in edges:
        a, b = el[0], el[1]
        if a == b:
            continue
        singles.discard(a)
        singles.discard(b)
        # dads, sons
        if structures.get(a, None) is None and structures.get(b, None) is not None:
            structures[a] = [{b}, {b}]
            structures[b][0].add(a)
            structures[b][1].add(a)
        elif structures.get(b, None) is None and structures.get(a, None) is not None:
            structures[b] = [{a}, {a}]
            structures[a][0].add(b)
            structures[a][1].add(b)
        elif structures.get(a, None) is None and structures.get(b, None) is None:
            structures[a] = [{b}, {b}]
            structures[b] = [{a}, {a}]
        else:
            structures[a][0].add(b)
            structures[a][1].add(b)
            structures[b][0].add(a)
            structures[b][1].add(a)
    # если графов нет.
    if n == len(singles):
        return mod_fact(n + 1, mod)
    # если графы есть, то едем дальше
    # (2^(trees_n) * trees_combinations * trees_n! * (2l + (SUM b_size_i) + 2)^s
    trees_els_n = n - len(singles)
    trees_n = 0
    trees_combinations = 1
    key = 1
    while len(structures) > 0:
        if structures.get(key, None) is None:
            key += 1
            continue
        tree_combs_by_mod = find_tree(key, structures, mod)
        if tree_combs_by_mod == -1:
            return 0
        trees_combinations = (trees_combinations * tree_combs_by_mod) % mod
        trees_combinations = (trees_combinations * (2 % mod)) % mod  # умножаем на 2, так как можно поменять местами.
        trees_n += 1
        key += 1
    # * trees_n!
    trees_shifts_by_mod = mod_fact(trees_n, mod)
    result = (trees_combinations * trees_shifts_by_mod) % mod
    # * (trees_els_n + 2)^s, s = len(singles)
    solos_by_mod = mod_power(trees_els_n + 2, len(singles), mod)
    result = (result * solos_by_mod) % mod
    return result


a_b = []
with open("input.txt") as f:
    # 1 <= n <= 10^6, 1 <= M <= 10^7 - количество пар знакомых дятлов, 1 <= k <= 2*10^6
    amount, m, km = map(int, f.readline().split())
    for i in range(m):
        first, second = map(int, f.readline().split())
        a_b.append((first, second))
print(calculate_combinations(amount, km, a_b))
