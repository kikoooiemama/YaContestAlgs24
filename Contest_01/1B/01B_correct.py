# Created by Nikolay Pakhomov 11.03.2024

# Помогите комментатору сообщить, сколько голов необходимо забить ПЕРВОЙ команде, чтобы победить,
# не переводя игру в дополнительное время.

with open('input.txt') as f:
    a = f.readline()[:-1].split(':')
    b = f.readline()[:-1].split(':')
    flag = f.readline().strip()

m1 = list(map(int, a))
m2 = list(map(int, b))

if flag == '1':
    isM2Guest = True
    guest_score = [m2[0], m1[1]]
else:
    isM2Guest = False
    guest_score = [m1[0], m2[1]]

total_score = [m1[0] + m2[0], m1[1] + m2[1]]
result = 0

if total_score[0] == total_score[1]:
    if guest_score[0] <= guest_score[1]:
        result = 1

elif total_score[0] < total_score[1]:
    td = total_score[1] - total_score[0]

    if isM2Guest:
        if guest_score[0] >= guest_score[1]:
            result = td
        else:
            gd = guest_score[1] - guest_score[0]
            if gd >= td:
                result = td + 1
            else:
                result = td
    else:
        if guest_score[0] > guest_score[1]:
            result = td
        else:
            result = td + 1

print(result)
