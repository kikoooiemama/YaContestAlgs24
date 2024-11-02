# Created by Nikolay Pakhomov 02.11.2024
import timeit

code_to_test = """
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
        #if current_shifts > previous_shifts:
        #   break
        previous_shifts = current_shifts
    return min_shifts


with open("input_max.txt") as f:
    rooms_n = int(f.readline())
    rooms = list(map(int, f.readline().split()))

ps = get_prefix_sum(rooms_n, rooms)
ans = find_min_shifts(rooms_n, rooms, ps)
print(ans)

"""
# вычисление времени выполнения кода
elapsed_time = timeit.timeit(code_to_test, number=100) / 100
print('Elapsed time: ', elapsed_time)
