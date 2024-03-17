# Created by Nikolay Pakhomov 11.03.2024
with open('input.txt') as f:
    vas = f.readline().split()
    mash = f.readline().split()

p, v = map(int, vas)
q, m = map(int, mash)

p1, p2 = p - v, p + v
q1, q2 = q - m, q + m

result = 0

if p2 < q1 or q2 < p1:
    result = p2 + q2 - p1 - q1 + 2

elif p1 == q1:
    if q2 >= p2:
        result = q2 - q1 + 1
    else:
        result = p2 - p1 + 1

elif p1 > q1:
    if q2 > p2:
        result = q2 - q1 + 1
    else:
        result = p2 - q1 + 1

else:
    if p2 <= q2:
        result = q2 - p1 + 1
    else:
        result = p2 - p1 + 1

print(result)