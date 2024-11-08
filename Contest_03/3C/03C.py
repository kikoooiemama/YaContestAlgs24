# Created by Nikolay Pakhomov 04.11.2024
# (n ≤  150000, k ≤ 10000, k ≤ n)
# Требуется для каждого положения «окна» определить минимум в нём.
# Выход: n−k+1 строк – минимумы для каждого положения «окна».
def find_windows_min(n, k, a):
    dequeue = [(a[0], 0)]  # кандидаты в минимум. всегда проверяем 1 элемент на актуальность!
    # формируем начало
    for i in range(1, k):
        if a[i] <= a[i - 1]:
            j = len(dequeue) - 1
            while j > -1:
                if dequeue[j][0] > a[i]:
                    dequeue.pop(j)
                else:
                    break
                j -= 1
        dequeue.append((a[i], i))
    # first
    print(dequeue[0][0])
    right = k
    while right < n:
        # выкалываем то что вне отрезка
        out = right - k
        if dequeue[0][1] == out:
            dequeue.pop(0)
        # анализируем новую точку.
        if a[right] <= a[right - 1]:
            j = len(dequeue) - 1
            while j > -1:
                if dequeue[j][0] > a[right]:
                    dequeue.pop(j)
                else:
                    break
                j -= 1
        dequeue.append((a[right], right))
        print(dequeue[0][0])
        right += 1


with open("input.txt") as f:
    a_len, window = map(int, f.readline().split())
    a_list = list(map(int, f.readline().split()))

find_windows_min(a_len, window, a_list)
