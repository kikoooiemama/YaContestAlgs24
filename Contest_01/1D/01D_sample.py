# Created by Nikolay Pakhomov 17.03.2024

# Решение с помощью массивов сдвига из лекции №2
# И по факту вся задача это моделирование

desk = []
with open('input4.txt') as f:
    for i in range(8):
        desk.append(f.readline().strip())

field = [list('-' * 10)]
for i in range(8):
    field.append(['-'] + list(desk[i]) + ['-'])
field.append(list('-' * 10))
for i in range(1, 10):
    for j in range(1, 10):
        if field[i][j] == 'R' or field[i][j] == 'B':
            # моделирование хода ладьи
            if field[i][j] == 'R':
                di = [0, 0, 1, -1]
                dj = [1, -1, 0, 0]
            else:
                di = [1, 1, -1, -1]
                dj = [1, -1, 1, -1]
            for dest in range(4):
                ni, nj = i + di[dest], j + dj[dest]
                while field[ni][nj] == '*' or field[ni][nj] == '.':
                    field[ni][nj] = '.'
                    ni += di[dest]
                    nj += dj[dest]
ans = 0
for row in field:
    for cell in row:
        if cell == '*':
            ans += 1
print(ans)
