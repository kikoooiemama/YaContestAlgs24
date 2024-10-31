# Created by Nikolay Pakhomov 27.10.2024
def count_vars(n, r, d):
    ans = 0
    last = 0
    for i in range(n):
        # Пока r меньше n и пока разница меньше r, мы двигаем r вправо.
        # Как только условие не выполняется -> мы берем [i:(r, n)] отрезки
        while (last < n) and d[last] - d[i] <= r:
            last += 1
        ans += n - last  # Тут будет 0, если вариантов нет, т.к. r=n после последней итерации
    return ans


with open("input.txt") as f:
    a, b = map(int, f.readline().split())
    m = list(map(int, f.readline().split()))

print(a, b)
print(m)
result = count_vars(a, b, m)
print(result)
