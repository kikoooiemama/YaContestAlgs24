# Created by Nikolay Pakhomov 25.11.2024
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


# mod_frees и find_options можно объединить
def mod_frees(n_slots, n_free, mod):
    # это можно улучшить префиксными суммами.
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


n = 4
s_list = [1, 2, 3, 4, 5]
for s in s_list:
    print(mod_frees(n, s, 1000000))
