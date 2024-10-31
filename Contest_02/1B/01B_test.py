# Created by Nikolay Pakhomov 01.11.2024
def count_kit(n, k, cars):
    ans = 0
    l, r = 0, 0
    now_sum = 0
    while r < n:
        if r == l:
            now_sum = cars[r]
        else:
            now_sum += cars[r]
        if now_sum < k:
            r += 1
        elif now_sum == k:
            r += 1
            ans += 1
        else:
            now_sum -= cars[l]
            now_sum -= cars[r]
            l += 1
    return ans


with open("input.txt") as f:
    a, b = map(int, f.readline().split())
    c = list(map(int, f.readline().split()))

n_list = []
k_list = []
cars_list = []
result_list = []
with open('input_test.txt') as f:
    test_n = int(f.readline().strip())
    for i in range(test_n):
        f.readline()
        a, b = map(int, f.readline().split())
        c = list(map(int, f.readline().split()))
        n_list.append(a)
        k_list.append(b)
        cars_list.append(c)

with open('output_test.txt') as f:
    for i in range(test_n):
        result_list.append(int(f.readline().strip()))

for i in range(test_n):
    res = count_kit(n_list[i], k_list[i], cars_list[i])
    print(f"Result: {res}, Answer: {result_list[i]}, Right: {res == result_list[i]}")