# Created by Nikolay Pakhomov 12.03.2024

fight = set()
desk = []
with open('input4.txt') as f:
    for i in range(8):
        desk.append(f.readline().strip())

for i in range(8):
    for j in range(8):
        if desk[i][j] == 'R':
            k = i
            check = False
            while k > -1:
                if check:
                    if desk[k][j] == 'B' or desk[k][j] == 'R':
                        break
                m = k * 8 + j
                fight.add(m)
                k -= 1
                check = True

            k = i
            check = False
            while k < 8:
                if check:
                    if desk[k][j] == 'B' or desk[k][j] == 'R':
                        break
                m = k * 8 + j
                fight.add(m)
                k += 1
                check = True

            d = j
            check = False
            while d > -1:
                if check:
                    if desk[i][d] == 'B' or desk[i][d] == 'R':
                        break
                m = i * 8 + d
                fight.add(m)
                d -= 1
                check = True

            d = j
            check = False
            while d < 8:
                if check:
                    if desk[i][d] == 'B' or desk[i][d] == 'R':
                        break
                m = i * 8 + d
                fight.add(m)
                d += 1
                check = True

        if desk[i][j] == 'B':
            idx = i * 8 + j
            fight.add(idx)

            k, d = i, j
            check = False
            while k > -1 and d > -1:
                if check:
                    if desk[k][d] == 'B' or desk[k][d] == 'R':
                        break
                m = k * 8 + d
                fight.add(m)
                k -= 1
                d -= 1
                check = True

            k, d = i, j
            check = False
            while k > -1 and d < 8:
                if check:
                    if desk[k][d] == 'B' or desk[k][d] == 'R':
                        break
                m = k * 8 + d
                fight.add(m)
                k -= 1
                d += 1
                check = True

            k, d = i, j
            check = False
            while k < 8 and d < 8:
                if check:
                    if desk[k][d] == 'B' or desk[k][d] == 'R':
                        break
                m = k * 8 + d
                fight.add(m)
                k += 1
                d += 1
                check = True

            k, d = i, j
            check = False
            while k < 8 and d > -1:
                if check:
                    if desk[k][d] == 'B' or desk[k][d] == 'R':
                        break
                m = k * 8 + d
                fight.add(m)
                k += 1
                d -= 1
                check = True

result = 64 - len(fight)
print(result)
