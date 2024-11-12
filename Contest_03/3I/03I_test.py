# Created by Nikolay Pakhomov 12.11.2024
def find_time(n, a, b, cars, result_order):
    forward_dict = {1: 3, 2: 4, 3: 1, 4: 2}
    right_dict = {1: 4, 2: 1, 3: 2, 4: 3}
    cross_type = forward_dict[a] == b
    if cross_type:
        priority = [a, b, right_dict.get(a), right_dict.get(b)]
    else:
        priority = [b, a, forward_dict.get(b), forward_dict.get(a)] if right_dict[a] == b else \
            [a, b, forward_dict.get(a), forward_dict.get(b)]
    q_1, q_2, q_3, q_4 = [], [], [], []
    counter = j = 0
    t = cars[0][2]
    while counter < n:
        while j < n and cars[j][2] == t:
            if cars[j][1] == priority[0]:
                q_1.append(cars[j])
            elif cars[j][1] == priority[1]:
                q_2.append(cars[j])
            elif cars[j][1] == priority[2]:
                q_3.append(cars[j])
            else:
                q_4.append(cars[j])
            j += 1
        free = True
        if cross_type:
            if len(q_1):
                rover = q_1.pop(0)
                result_order[rover[0]] = t
                counter += 1
                free = False
            if len(q_2):
                rover = q_2.pop(0)
                result_order[rover[0]] = t
                counter += 1
                free = False
            if len(q_3) and free:
                rover = q_3.pop(0)
                result_order[rover[0]] = t
                counter += 1
            if len(q_4) and free:
                rover = q_4.pop(0)
                result_order[rover[0]] = t
                counter += 1
        else:
            if len(q_1):
                rover = q_1.pop(0)
                result_order[rover[0]] = t
                counter += 1
                free = False
            if len(q_2) and free:
                rover = q_2.pop(0)
                result_order[rover[0]] = t
                counter += 1
                free = False
            if len(q_3) and free:
                rover = q_3.pop(0)
                result_order[rover[0]] = t
                counter += 1
                free = False
            if len(q_4) and free:
                rover = q_4.pop(0)
                result_order[rover[0]] = t
                counter += 1
        t = cars[j][2] if (len(q_1) + len(q_2) + len(q_3) + len(q_4)) == 0 and j < n else t + 1


n_list = []
a_list = []
b_list = []
m_list_list = []
ans_list = []
result_list = []
with open('input_test.txt') as f:
    test_n = int(f.readline().strip())
    for ii in range(test_n):
        f.readline()
        nn = int(f.readline())
        aa, bb = map(int, f.readline().split())
        m_list = []
        ans = {}
        for i in range(nn):
            source, time = map(int, f.readline().split())
            m_list.append((i, source, time))
            ans[i] = time
        n_list.append(nn)
        a_list.append(aa)
        b_list.append(bb)
        m_list_list.append(m_list)
        ans_list.append(ans)

with open('output_test.txt') as f:
    for ii in range(test_n):
        result_list.append(f.readline().strip())

for ii in range(test_n):
    rovers = sorted(m_list_list[ii], key=lambda x: (x[2], x[0]))
    find_time(n_list[ii], a_list[ii], b_list[ii], rovers, ans_list[ii])
    res_str = " ".join(list(map(str, ans_list[ii].values())))
    print(f"Result: {res_str}, Answer: {result_list[ii]}, Right: {res_str == result_list[ii]}")
