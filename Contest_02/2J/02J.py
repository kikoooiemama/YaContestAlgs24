# Created by Nikolay Pakhomov 27.10.2024
def get_idx_stops_and_iters(n, a_seq):
    # количество "переход с одинаковой весомостью" для каждого отрезка [stop, x_i]
    iters_sum = [0]
    # индексы улик, переход с которых будет означать "переход с одинаковой весомостью"
    iters_idx_per_stop = {0: []}
    # номер улики для каждого x_i, при котором прекращается перебор
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
            # iters_sum[-1] += 1
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
    print(f"a: {a_seq}")
    print(f"stops:     {stops}")
    print(f"iters_sum: {iters_sum}")
    print(f"iters_idx: {iters_idx_per_stop}")
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


with open("input2.txt") as f:
    a_len = int(f.readline())
    a_list = list(map(int, f.readline().split()))
    x_len, max_shifts = map(int, f.readline().split())
    x_list = list(map(int, f.readline().split()))

ans = find_x_for_experiment(a_len, a_list, x_len, max_shifts, x_list)
print(ans.strip())
# ans = get_evidence_list(a_len, a_list, x_len, max_shifts, x_list)
# print(" ".join(list(map(str, ans))))
