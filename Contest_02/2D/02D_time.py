# Created by Nikolay Pakhomov 01.11.2024
import timeit

code_to_test = """
def calculate_min_days(n, dist, cases):
    max_sum = 0
    now_sum = 0
    r = 0
    previous = 0
    for i in range(n):
        if cases[i] == previous:
            now_sum -= 1
            continue
        while (r < n) and (cases[r] - cases[i] <= dist):
            now_sum += 1
            r += 1
        max_sum = max(max_sum, now_sum)
        now_sum -= 1
        previous = cases[i]
    return max_sum


with open("input_time.txt") as f:
    b, c = map(int, f.readline().split())
    al = list(map(int, f.readline().split()))

al.sort()
ans = calculate_min_days(b, c, al)
print(ans)
"""
# вычисление времени выполнения кода
elapsed_time = timeit.timeit(code_to_test, number=100) / 100
print('Elapsed time: ', elapsed_time)
