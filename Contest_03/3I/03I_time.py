# Created by Nikolay Pakhomov 12.11.2024
def get_order(n, nums):
    result = []
    return result


n_list = []
a_list = []
b_list = []

car_list = []
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
