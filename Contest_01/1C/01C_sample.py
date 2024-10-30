# Created by Nikolay Pakhomov 27.10.2024
# Сжатие картинки. Удаление одинаковых строк, удаление одинаковых столбцов. (Я делал через маски..)

# Сжимаем, удаляем одинаковые строки. Формируем новый список с оригинальными строками (без повторов).
# Если строка состояла из одних точек - удаляем
def compress(lst):
    ans = [lst[0]]
    for now in lst[1:]:
        if now != ans[-1]:
            ans.append(now)
    # чек 1 строки
    if len(ans) > 1 and set(ans[0]) == {"."}:
        ans.pop(0)
    # чек последней строки
    if len(ans) > 1 and set(ans[-1]) == {"."}:
        ans.pop()
    return ans


# Транспонирование. Меняем строки на столбцы, чтобы применить снова compress для "столбцов".
def invert(lst):
    ans = []
    for i in range(len(lst[0])):
        ans.append([])
    for now in lst:
        for i in range(len(now)):
            ans[i].append(now[i])
    for i in range(len(ans)):
        ans[i] = "".join(ans[i])  # листы превращаем в str
    return ans


with open('input.txt') as f:
    n = int(f.readline().strip())
    a = []
    for ii in range(n):
        a.append(f.readline().strip())

# Сжимаем по строкам
a = compress(a)
a = invert(a)
# Сжимаем по столбцам
a = compress(a)
a = invert(a)
if a == [""]:
    print('I')
elif a == ["###",
           "#.#",
           "###"]:
    print("O")
elif a == ["##",
           "#.",
           "##"]:
    print("C")
elif a == ["#.",
           "##"]:
    print("L")
elif a == ["#.#",
           "###",
           "#.#"]:
    print("H")
elif a == ["###",
           "#.#",
           "###",
           "#.."]:
    print("P")
else:
    print('X')
