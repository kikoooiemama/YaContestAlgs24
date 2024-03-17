# Идея в том, чтобы представить данные отрезками. А затем проанализировать нахождения левых и правых границ отрезков
# на горизонтальной оси

with open('input.txt') as f:
    vas = f.readline().split()
    mash = f.readline().split()

p, v = map(int, vas)
q, m = map(int, mash)

p1, p2 = p - v, p + v
q1, q2 = q - m, q + m

# проверяем пересечение отрезков
if max(p1, q1) <= min(p2, q2):
    print(max(p2, q2) - min(p1, q1) + 1)
else:
    print(p2 + q2 - p1 - q1 + 2)
