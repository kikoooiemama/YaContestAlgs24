# Created by Nikolay Pakhomov 01.11.2024
import timeit

code_to_test = """
def get_prefix_sum(sequence, mod):
    prefixsum = [0] * (len(sequence) + 1)
    prefixmulti = [0] * (len(sequence) + 1)
    prefixsub = [0] * (len(sequence) + 1)
    for i in range(len(sequence) - 1, -1, -1):
        prefixsum[i] = prefixsum[i + 1] + sequence[i]
        prefixmulti[i] = sequence[i] * prefixsum[i + 1]
        prefixsub[i] = (prefixsub[i + 1] + prefixmulti[i])
    prefixsub.pop(0)
    return prefixsub


def find_number_by_mod(n, a, prefix_sum, mod):
    result = 0
    for i in range(n - 2):
        result += (a[i] * prefix_sum[i]) % mod
    return result


with open("input_time.txt") as f:
    nn = int(f.readline().strip())
    al = list(map(int, f.readline().split()))

# Сортировка O(n*log n)
# al.sort()
factor = 1_000_000_007
prefix = get_prefix_sum(al, factor)
ans = find_number_by_mod(nn, al, prefix, factor)
print(ans)
"""
# вычисление времени выполнения кода
elapsed_time = timeit.timeit(code_to_test, number=100) / 100
print('Elapsed time: ', elapsed_time)
