# Created by Nikolay Pakhomov 12.03.2024

# Можно подумать и понять, что достаточно написать одну цифру, а потом приписывать нули
# Можно подумать по другому и просто перебирать какую цифру приписать,
# быстро проверяя делимость...
# Кольцо вычетов по модулю? Если (x % k + y) % k это то же самое, что (x + y) % k
# Приписывание цифры digit к числу now по модулю k
# (now * 10 + d) % k

with open('input.txt') as f:
    n, k, d = map(int, f.readline().split())

# остаток
mod = n % k
ans = [n]
flag = True
for i in range(d):
    for new_digit in range(10):
        # (x + y) % k
        new_mod = (mod * 10 + new_digit) % k
        # Если за текущий день бухгалтер не смог приписать цифру так, что все число делится
        # на k, тогда возвращаем флаг устанавливаем в False - решения нет.
        if new_mod == 0:
            ans.append(new_digit)
            mod = new_mod
            break
    # если цикл for завершается без brake, то он переходит в else
    else:
        flag = False

if flag:
    print(''.join(map(str, ans)))
else:
    print(-1)
