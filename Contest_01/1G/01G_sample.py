# Created by Nikolay Pakhomov 17.03.2024

# У нас X юнитов, у казармы противника Y очков здоровья, на каждом ходу казарма производит
# P юнитов противника

# На каждом ходу сначала часть наших юнитов атакует казарму ИЛИ юнита противника,
# затем юниты противника атакуют наших, затем казарма производит юниты

# Задача: разрушить казарму и уничтожить всех врагов

# Мой алгоритм не сработал, потому что я всегда убивал всех юнитов, а потом ломал казарму.
# Но может быть случай, когда часть бойцов надо отправить на ломание казарм, а часть
# на уничтожение врагов (то есть не фулл урон в казарму) - будет эффективней, ведь целью
# является минимизация раундов!

# Ограничение 5000. Определим моменты, когда нужно наносить весь урон казарме, а когда нет.

# Функция моделирования
def calc(t, myunits, barhp, enemyprod):
    rounds = 0
    enemyunits = 0
    while barhp >= t:
        if enemyunits >= myunits:
            return 10 ** 9
        barhp -= myunits - enemyunits
        enemyunits = 0
        if barhp >= 0:
            enemyunits += enemyprod
        rounds += 1

    while barhp > 0:
        if myunits <= 0:
            return 10 ** 9
        if barhp >= myunits:
            barhp -= myunits
        else:
            enemyunits -= myunits - barhp
            barhp = 0
        myunits -= enemyunits
        if barhp > 0:
            enemyunits += enemyprod
        rounds += 1

    while enemyunits > 0:
        if myunits <= 0:
            return 10 ** 9
        enemyunits -= myunits
        if enemyunits > 0:
            myunits -= enemyunits
        rounds += 1

    return rounds


with open('input5.txt') as f:
    x = int(f.readline().strip())
    y = int(f.readline().strip())
    p = int(f.readline().strip())

ans = 10 ** 9
# до какого уровня казармы мы будем стучать стратегией №1 (экономим силы), а затем переключаться на стратегию №2
# (весь урон по казарме, остальное на выживших)
# Тут видимо перебор стратегий
for t in range(0, y + 1):
    ans = min(ans, calc(t, x, y, p))
if ans != 10 ** 9:
    print(ans)
else:
    print(-1)
