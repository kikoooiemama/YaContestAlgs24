# Created by Nikolay Pakhomov 27.10.2024
def calculate_min_days(n, dist, cases):
    """
        1<= N <= 2*10^5, 0 <= k <= 10^9, 1 <= a_i <= 10^9, a_i - не отсортированы.
        Задачу будет решать с помощью двух указателей.
        1 1 2 2 3 3 3 5 5
        Идея: нужно найти такое "окно"/"отрезок", в котором будет максимальное количество чисел в пределах K. Поиск в
        отсортированном списке. Находим 1 отрезок. И так как справа числа все больше предыдущих, сдвигаем указатель L
        вправо на 1, а R продолжает двигаться дальше до конца по мере анализа.
    """
    max_sum = 0
    now_sum = 0  # количество дней
    r = 0
    previous = 0
    for i in range(n):
        # Анализ повторных значений, их нужно пропускать т.к. для них будет одинаковое количество now_sum
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


with open("input.txt") as f:
    b, c = map(int, f.readline().split())
    al = list(map(int, f.readline().split()))

# Сортировка O(n*log n)
al.sort()
ans = calculate_min_days(b, c, al)
print(ans)
