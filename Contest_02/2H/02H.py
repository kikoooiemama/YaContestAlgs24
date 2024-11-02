# Created by Nikolay Pakhomov 27.10.2024
# Важно увидеть закономерность, что при движении вправо, мы будем вычитать сумму правого отрезка и увеличивать на сумму
# левого отрезка. И по такой логике мы будем использовать префиксные суммы.
# Расчет суммы на отрезке [L, R).
def get_prefix_sum(n, nums):
    prefixsum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]
    return prefixsum


def rsq(p_sum, left, right):
    return p_sum[right] - p_sum[left]


def find_min_shifts(n, a, prefix_sum):
    # посчитаем первого кабинета и возьмем за основу.
    min_shifts = 0
    for i in range(n):
        min_shifts += i * a[i]

    print(f"min_shifts: {min_shifts}")
    previous_shifts = min_shifts
    current_shifts = min_shifts
    for i in range(1, n):
        current_shifts += rsq(prefix_sum, 0, i)
        current_shifts -= rsq(prefix_sum, i, n)
        min_shifts = min(current_shifts, min_shifts)
        if current_shifts > previous_shifts:
            break
        previous_shifts = current_shifts
        print(current_shifts)
    return min_shifts


with open("input2.txt") as f:
    rooms_n = int(f.readline())
    rooms = list(map(int, f.readline().split()))

ps = get_prefix_sum(rooms_n, rooms)
print(rooms)
print(ps)
print(f"Отрезок [1, 4]: {rsq(ps, 1, 4 + 1)}")
ans = find_min_shifts(rooms_n, rooms, ps)
print(ans)
