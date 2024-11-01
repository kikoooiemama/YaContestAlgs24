# Created by Nikolay Pakhomov 01.11.2024
def calculate_min_days(n, k, a):
    min_days = 0
    return min_days


n_list = []
k_list = []
a_list = []
result_list = []
with open('input_test.txt') as f:
    test_n = int(f.readline().strip())
    for i in range(test_n):
        f.readline()
        nn, kk = map(int, f.readline().split())
        aa = list(map(int, f.readline().split()))
        n_list.append(nn)
        k_list.append(kk)
        a_list.append(aa)

with open('output_test.txt') as f:
    for i in range(test_n):
        result_list.append(int(f.readline().strip()))

for i in range(test_n):
    res = calculate_min_days(n_list[i], k_list[i], a_list[i])
    print(f"Result: {res}, Answer: {result_list[i]}, Right: {res == result_list[i]}")
