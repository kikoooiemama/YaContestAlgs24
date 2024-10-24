with open('input5.txt') as f:
    x = int(f.readline().strip())
    y = int(f.readline().strip())
    p = int(f.readline().strip())

# первый раунд всегда одинаковый
n = 1
z = 0
y = y - x if y > x else 0
if y > 0:
    z += p

# враг выжил после 1 раунда
if y != 0 or z != 0:
    while x > 0:
        n += 1
        dmg = x
        # принимаем решения снести в первую очередь казармы или войска
        if y > 0:
            if y >= x:
                if p < x:
                    # убиваем врагов
                    dmg = x - z
                    z = 0
                    # наносим урон казарме
                    y = y - dmg if y > dmg else 0
                else:
                    n = -1
                    break
            # y < x
            else:
                if p >= x:
                    dmg = x - y
                    y = 0
                    if dmg >= p:
                        z = 0
                    else:
                        df = z - dmg
                        if df/2 > x - df:
                            n = -1
                            break
                        else:
                            z = z - dmg
                            x = x - z
                else:
                    # убиваем врагов
                    dmg = x - z
                    z = 0
                    # наносим урон казарме
                    y = y - dmg if y > dmg else 0
        else:
            if z > 0:
                z = z - dmg if z > dmg else 0
            else:
                break
        # проверка на конец
        if y == 0 and z == 0:
            break
        # пополнение врагов
        if y > 0:
            z += p

print(n)
