# Created by Nikolay Pakhomov 04.11.2024
# решение через сортировку по высоте и прогону с декой на поиск максимума на отрезке.
def find_min(n, height, chairs):
    print(chairs)
    chairs = sorted(chairs, key=lambda x: (x[0]))
    print(chairs)
    sum_w = 0
    discomfort = 1000000000
    left, right = 0, 0
    while left < n and right < n:
        if sum_w < height:
            sum_w += chairs[right]
            right += 1
        else:

            sum_w -= chairs[left]
            left += 1
    # while left < n:
    #     while right < n and sum_w < height:
    #         sum_w += chairs[right]
    result = 2
    return result


with open("input.txt") as f:
    chairs_len, vas_h = map(int, f.readline().split())
    zipped = list(zip(list(map(int, f.readline().split())), list(map(int, f.readline().split()))))

ans = find_min(chairs_len, vas_h, zipped)
print(ans)
