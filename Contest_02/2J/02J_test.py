# Created by Nikolay Pakhomov 03.11.2024
def get_idx_stops_and_iters(n, a_seq):
    iters_sum = [0]
    iters_idx_per_stop = {0: []}
    stops = [0]
    stop_idx = 0
    cur_iters_per_stop = 0
    r = 1
    previous = a_seq[0]
    while r < n:
        x = a_seq[r]
        if previous > x:
            stop_idx = r
            cur_iters_per_stop = 0
            iters_idx_per_stop[stop_idx] = []
        elif previous == x:
            cur_iters_per_stop += 1
            iters_idx_per_stop[stop_idx].append(r)
        previous = x
        iters_sum.append(cur_iters_per_stop)
        stops.append(stop_idx)
        r += 1

    return stops, iters_sum, iters_idx_per_stop


def find_x_for_experiment(n, a_seq, m, k, x_nums):
    if n == 1:
        return "1 " * m
    stops, iters_sum, iters_idx_per_stop = get_idx_stops_and_iters(n, a_seq)
    result = ""
    for num in x_nums:
        idx = num - 1
        st = stops[idx]
        iters = iters_sum[idx]
        if iters == 0:
            result += f"{st + 1} "
        else:
            iters_idx = iters_idx_per_stop.get(st)
            if iters > k:
                st = iters_idx[iters - 1 - k]
            result += f"{st + 1} "
    return result


n_list = []
a_list = []
m_list = []
k_list = []
x_list = []
result_list = []
with open('input_test.txt') as f:
    test_n = int(f.readline().strip())
    for ii in range(test_n):
        f.readline()
        nn = int(f.readline().strip())
        aa = list(map(int, f.readline().split()))
        mm, kk = map(int, f.readline().split())
        xx = list(map(int, f.readline().split()))
        n_list.append(nn)
        a_list.append(aa)
        m_list.append(mm)
        k_list.append(kk)
        x_list.append(xx)

with open('output_test.txt') as f:
    for ii in range(test_n):
        result_list.append(f.readline().strip())

for ii in range(test_n):
    res = find_x_for_experiment(n_list[ii], a_list[ii], m_list[ii], k_list[ii], x_list[ii])
    res_str = res.strip()
    # res_str = " ".join(list(map(str, res)))
    print(f"Result: {res_str}, Answer: {result_list[ii]}, Right: {res_str == result_list[ii]}")
