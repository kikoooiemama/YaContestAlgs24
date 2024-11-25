# Created by Nikolay Pakhomov 21.11.2024
import sys

import sys


def mod_fact(r, mod):
    if r == 0:
        return 1
    answer = j = 1
    while j < r + 1:
        answer = (answer * (j % mod)) % mod
        j += 1
    return answer


def find_options(res, a, n, p, k):
    if n:
        for j in range(n + 1, 0, -1):
            if j > n - k:
                if j <= p:
                    find_options(res, a + [j], n - j, j, k)
    else:
        res.append(a)


def pp(mm, nn, mod):
    j = nn
    th = nn - mm
    rs = 1
    while j > th and j > 1:
        rs = rs * (j % mod) % mod
        j -= 1
    return rs


def mod_frees(n_slots, n_free, mod):
    options = []
    find_options(options, [], n_free, n_free, n_slots)
    cs = 0
    for option in options:
        j = 0
        cs_opt = 1
        remainder = n_free
        while j < len(option):
            am = option[j]
            if am == 1:
                cs_opt = (cs_opt * ((n_slots - j) % mod)) % mod
            else:
                cs_opt = (cs_opt * (((n_slots - j) % mod) * pp(am, remainder, mod)) % mod) % mod
            remainder = remainder - am
            j += 1
        cs = (cs + cs_opt) % mod
    return cs


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
        if len(grandsons) > 0:
            tree[0].append(son)
            if len(tree[0]) > 2:
                return -1
        else:
            tree[1].add(son)
            structures.pop(son)
    if len(tree[0]) == 2:
        for sub_tree in tree[0]:
            sub_tree_combs_by_mod = rec_find_subtree_one(sub_tree, structures, mod)
            if sub_tree_combs_by_mod == -1:
                return -1
            combs = (combs * sub_tree_combs_by_mod) % mod
        combs = (combs * (2 % mod)) % mod
        combs = (combs * mod_fact(len(tree[1]), mod)) % mod
    elif len(tree[0]) == 1:
        sub_tree = tree[0][0]
        if len(tree[1]):
            sub_combs = rec_find_subtree_one(sub_tree, structures, mod)
            if sub_combs == -1:
                return -1
            combs = (combs * sub_combs) % mod
            combs = (combs * mod_fact(len(tree[1]), mod)) % mod
            combs = (combs * (2 % mod)) % mod
        else:
            sub_combs = rec_find_subtree_one_pr(sub_tree, structures, mod)
            if sub_combs == -1:
                return -1
            combs = (combs * sub_combs) % mod
    elif len(tree[0]) == 0:
        combs = (combs * mod_fact(len(tree[1]), mod)) % mod
    return combs


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
    if n == len(singles):
        return mod_fact(n + 1, mod)
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
    trees_shifts_by_mod = mod_fact(trees_n, mod)
    result = (trees_combinations * trees_shifts_by_mod) % mod
    solos_by_mod = mod_frees(trees_els_n + 2, len(singles), mod)
    result = (result * solos_by_mod) % mod
    return result


sys.setrecursionlimit(1000000000)
n_list = []
m_list = []
k_list = []
result_list = []
a_b_list = []
test_n = 13
for i in range(2, test_n + 2):
    with open(f"input{i}.txt") as f:
        amount, m, k = map(int, f.readline().split())
        n_list.append(amount)
        m_list.append(m)
        k_list.append(k)
        a_b = []
        for m_i in range(m):
            first, second = map(int, f.readline().split())
            a_b.append((first, second))
        a_b_list.append(a_b)

    with open(f"output{i}.txt") as f:
        result_list.append(int(f.readline().strip()))

for ii in range(test_n):
    ans = calculate_combinations(n_list[ii], k_list[ii], a_b_list[ii])
    print(f"Test-{ii + 2}, Result: {ans}, Answer: {result_list[ii]}, Right: {ans == result_list[ii]}")
