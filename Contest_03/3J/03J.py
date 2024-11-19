# Created by Nikolay Pakhomov 04.11.2024
# решение через сортировку по высоте и прогону с декой на поиск максимума на отрезке.
def find_min(n, height, chairs):
    chairs = sorted(chairs, key=lambda x: (x[0]))
    print(chairs)
    discomfort = 1000000000
    left = right = sum_w = 0
    # максимумы для каждого положения «окна». Первое - значение дискомфорта, второе - индекс крайнего левого стула.
    deq = []
    while left < n:
        if sum_w < height and right < n:
            sum_w += chairs[right][1]
            # заполнение дека для кандидатов
            dis, idx = (0, left) if right - left == 0 else (chairs[right][0] - chairs[right - 1][0], right - 1)
            # удаляем значения меньшие по сравнению с dis
            if len(deq) > 0:
                j = len(deq) - 1
                while j > -1 and deq[j][0] <= dis:
                    deq.pop(j)
                    j -= 1
            deq.append((dis, idx))
            # проверка на последний элемент. Он должен быть кандидатом!
            if right == n - 1:
                deq.append((0, right))
            right += 1
        if sum_w < height and right >= n:
            # вася никогда не сможет лечь на оставшиеся стулья.
            break
        if sum_w >= height:
            if len(deq) > 0:
                max_shift = deq[0]
                discomfort = min(max_shift[0], discomfort)
                if max_shift[1] == left:
                    deq.pop(0)
            sum_w -= chairs[left][1]
            left += 1
    return discomfort


with open("input2.txt") as f:
    chairs_len, vas_h = map(int, f.readline().split())
    zipped = list(zip(list(map(int, f.readline().split())), list(map(int, f.readline().split()))))

ans = find_min(chairs_len, vas_h, zipped)
print(ans)
