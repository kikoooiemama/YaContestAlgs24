# Created by Nikolay Pakhomov 01.11.2024
import timeit

code_to_test = """
def get_median_idx(n):
    if n % 2 == 0:
        return n // 2 - 1
    else:
        return n // 2


def calculate_seq(n, a):
    result = ""
    for i in range(n):
        idx = get_median_idx(len(a))
        result += f" {a[idx]}"
        a.pop(idx)
    return result[1:]


with open("input_time.txt") as f:
    nn = int(f.readline().strip())
    al = list(map(int, f.readline().split()))

al.sort()
ans = calculate_seq(nn, al)
print(ans)
"""
# вычисление времени выполнения кода
elapsed_time = timeit.timeit(code_to_test, number=100) / 100
print('Elapsed time: ', elapsed_time)
