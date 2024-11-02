# Created by Nikolay Pakhomov 02.11.2024
def get_prefix_sum(n, nums):
    prefixsum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]
    return prefixsum


def rsq(p_sum, left, right):
    return p_sum[right] - p_sum[left]


def find_min_shifts(n, a, prefix_sum):
    min_shifts = 0
    for i in range(n):
        min_shifts += i * a[i]
    previous_shifts = min_shifts
    current_shifts = min_shifts
    for i in range(1, n):
        current_shifts += rsq(prefix_sum, 0, i)
        current_shifts -= rsq(prefix_sum, i, n)
        min_shifts = min(current_shifts, min_shifts)
        if current_shifts > previous_shifts:
            break
        previous_shifts = current_shifts
    return min_shifts


n_list = []
a_list = []
result_list = []
with open('input_test.txt') as f:
    test_n = int(f.readline().strip())
    for i in range(test_n):
        f.readline()
        nn = int(f.readline().strip())
        aa = list(map(int, f.readline().split()))
        n_list.append(nn)
        a_list.append(aa)

with open('output_test.txt') as f:
    for i in range(test_n):
        result_list.append(int(f.readline().strip()))

for i in range(test_n):
    ps = get_prefix_sum(n_list[i], a_list[i])
    res = find_min_shifts(n_list[i], a_list[i], ps)
    print(f"Result: {res}, Answer: {result_list[i]}, Right: {res == result_list[i]}")
