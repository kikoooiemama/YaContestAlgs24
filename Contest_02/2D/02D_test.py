# Created by Nikolay Pakhomov 01.11.2024
def calculate_min_days(n, dist, cases):
    """
        1<= N <= 2*10^5, 0 <= k <= 10^9, 1 <= a_i <= 10^9, a_i - не отсортированы.
        Задачу будет решать с помощью двух указателей.
        1 1 2 2 3 3 3 5 5
        Идея: нужно найти такое "окно"/"отрезок", в котором будет максимальное количество чисел. Поиск в отсортированном
        списке. Находим 1 отрезок. И так как справа числа все больше предыдущих, сдвигаем указатель L вправо на 1, а R
        продолжает двигаться дальше до конца по мере анализа.
    """
    max_sum = 0
    now_sum = 0  # количество дней
    r = 0
    previous = 0
    for i in range(n):
        # анализ повторных значений, их нужно пропускать т.к. для них будет одинаковое количество now_sum
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
    a_list[i].sort()
    res = calculate_min_days(n_list[i], k_list[i], a_list[i])
    print(f"Result: {res}, Answer: {result_list[i]}, Right: {res == result_list[i]}")
