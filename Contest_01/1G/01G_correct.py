# Created by Nikolay Pakhomov 17.03.2024

# Описание стратегии:
# Тактика №1 - уничтожение в первую очередь войск противника, а остаток бить по казармам.
# Тактика №2 - весь урон в казарму, а остаток бить по армии врага.

# В первую очередь используем тактику №1, а потом уже тактику №2. Однако, смена тактики не обязательно должна применятся
# в момент, когда здоровье казармы упадет до нуля. Порой наиболее оптимальным решением к переходу к тактике №2 будет
# определенный уровень здоровья казармы.

# После уничтожения казармы, нужно только убивать оставшиеся войска.


def find_min(baracksHpTh, myUnits, baracksHp, prod, min_ans):
    rounds = 0
    enemyUnits = 0

    # №1
    while baracksHp >= baracksHpTh:
        if enemyUnits >= myUnits:
            return 10 ** 9

        baracksHp -= myUnits - enemyUnits
        enemyUnits = 0
        if baracksHp > 0:
            enemyUnits += prod
        rounds += 1
        if rounds >= min_ans:
            return min_ans

    # №2
    while baracksHp > 0:
        if myUnits <= 0:
            return 10 ** 9

        if baracksHp >= myUnits:
            baracksHp -= myUnits
        else:
            enemyUnits -= myUnits - baracksHp
            baracksHp = 0
        myUnits -= enemyUnits
        if baracksHp > 0:
            enemyUnits += prod
        rounds += 1
        if rounds >= min_ans:
            return min_ans

    # казарма уничтожена
    while enemyUnits > 0:
        if myUnits <= 0:
            return 10 ** 9

        enemyUnits -= myUnits
        if enemyUnits > 0:
            myUnits -= enemyUnits
        rounds += 1
        if rounds >= min_ans:
            return min_ans

    return rounds


with open('input.txt') as f:
    x = int(f.readline().strip())
    y = int(f.readline().strip())
    p = int(f.readline().strip())

ans = 10 ** 9
for t in range(0, y + 1):
    ans = min(ans, find_min(t, x, y, p, ans))
if ans != 10 ** 9:
    print(ans)
else:
    print(-1)
