# Created by Nikolay Pakhomov 01.11.2024
def count_vars(n, r, d):
    ans = 0
    last = 0
    for i in range(n):
        while (last < n) and d[last] - d[i] <= r:
            last += 1
        ans += n - last
    return ans


n_list = []
r_list = []
d_list = []
result_list = []
with open('input_test.txt') as f:
    test_n = int(f.readline().strip())
    for i in range(test_n):
        f.readline()
        a, b = map(int, f.readline().split())
        c = list(map(int, f.readline().split()))
        n_list.append(a)
        r_list.append(b)
        d_list.append(c)

with open('output_test.txt') as f:
    for i in range(test_n):
        result_list.append(int(f.readline().strip()))

for i in range(test_n):
    res = count_vars(n_list[i], r_list[i], d_list[i])
    print(f"Result: {res}, Answer: {result_list[i]}, Right: {res == result_list[i]}")
