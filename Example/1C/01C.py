# Created by Nikolay Pakhomov 11.03.2024
with open('input.txt') as f:
    n = int(f.readline().strip())
    ind = list(map(int, f.readlines()))

amount_s = 0
amount_t = 0
amount_b = 0

t = 4

for m in ind:
    amount_t += m // t
    rem = m % t
    if rem == 0:
        continue
    if rem == 1:
        amount_s += 1
    elif rem == 2:
        amount_s += 2
    elif rem == 3:
        amount_t += 1
        amount_b += 1

print(amount_s + amount_t + amount_b)
