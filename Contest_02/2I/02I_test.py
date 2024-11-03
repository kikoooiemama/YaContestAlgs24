# Created by Nikolay Pakhomov 03.11.2024
def find_order(n, a, b, p):
    result = ""
    history = {}
    idx_list = []
    for i in range(1, n + 1):
        idx_list.append(i)
        history[i] = 0
    idx_list = [i for i in range(1, n + 1)]
    interest = sorted(list(zip(a, b, idx_list)), key=lambda x: (x[0], x[1], -x[2]), reverse=True)
    utility = sorted(list(zip(a, b, idx_list)), key=lambda x: (x[1], x[0], -x[2]), reverse=True)
    i = u = 0
    for mood in p:
        if mood:
            while history.get(utility[u][2]) and u < n:
                u += 1
            number = utility[u][2]
            history[number] = 1
            result += f"{number} "
        else:
            while history.get(interest[i][2]) and i < n:
                i += 1
            number = interest[i][2]
            history[number] = 1
            result += f"{number} "
    return result


n_list = []
a_list = []
b_list = []
p_list = []
result_list = []
with open('input_test.txt') as f:
    test_n = int(f.readline().strip())
    for ii in range(test_n):
        f.readline()
        days = int(f.readline().strip())
        aa = list(map(int, f.readline().split()))
        bb = list(map(int, f.readline().split()))
        pp = list(map(int, f.readline().split()))
        n_list.append(days)
        a_list.append(aa)
        b_list.append(bb)
        p_list.append(pp)

with open('output_test.txt') as f:
    for ii in range(test_n):
        result_list.append(f.readline().strip())

for ii in range(test_n):
    res = find_order(n_list[ii], a_list[ii], b_list[ii], p_list[ii])
    res_str = res.strip()
    print(f"Result: {res_str}, Answer: {result_list[ii]}, Right: {res_str == result_list[ii]}")
