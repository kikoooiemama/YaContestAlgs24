# Created by Nikolay Pakhomov 04.11.2024
def define_order(a, b, f_dict, r_dict):
    if f_dict[a] == b:
        order_list = [(a, b), (r_dict.get(a), r_dict.get(b))]
    else:
        order_list = [b, a, f_dict.get(b), f_dict.get(a)] if r_dict[a] == b else [a, b, f_dict.get(a), f_dict.get(b)]
    return order_list


# Раскидаем всех на 4 очереди и будем решать порядок! O(4N)
def find_time(n, a, b, cars, result_order):
    forward_dict = {1: 3, 2: 4, 3: 1, 4: 2}
    right_dict = {1: 4, 2: 1, 3: 2, 4: 3}
    priority = define_order(a, b, forward_dict, right_dict)
    counter = c = t = 0
    queue_1 = []
    queue_2 = []
    queue_3 = []
    queue_4 = []
    while counter < n:
        while c < n:
            pass
    result = []
    return result


m_list = []
ans = {}
with open("input.txt") as f:
    n_m = int(f.readline())
    a_main, b_main = map(int, f.readline().split())
    for i in range(n_m):
        source, time = map(int, f.readline().split())
        m_list.append((i, source, time, time))
        ans[i] = time

m_list = sorted(m_list, key=lambda x: (x[2], x[0]))
order = f
find_time(n_m, a_main, b_main, m_list, ans)
for v in ans.values():
    print(v)
