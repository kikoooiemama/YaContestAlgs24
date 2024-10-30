# Created by Nikolay Pakhomov 27.10.2024
# 4 способа вытаскивать вещи!!! Мы выбираем тот, где сумма N+M минимальна!
# 1. Синий: B + 1, D + 1
# 2. Красный: A + 1, C + 1
# 3. Майки обоих, любые носки: max(A, B) + 1, 1
# 4. Носки обоих цветов и любая майка: 1, max(C,D) + 1

with open('input.txt') as f:
    a, b, c, d = list(map(int, f.readlines()))

ans = []
if a > 0 and c > 0:
    ans.append([b + 1, d + 1])
if b > 0 and d > 0:
    ans.append([a + 1, c + 1])
if a > 0 and b > 0:
    ans.append([max(a, b) + 1, 1])
if c > 0 and d > 0:
    ans.append([1, max(c, d) + 1])
m = min(ans, key=sum)
print(*m)
