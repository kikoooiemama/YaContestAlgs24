# Created by Nikolay Pakhomov 27.10.2024
def count_kit(n, k, cars):
    ans = 0
    l, r = 0, 0
    now_sum = 0
    while r < n:
        if r == l:
            now_sum = cars[r]
        else:
            now_sum += cars[r]
        if now_sum < k:
            r += 1
        elif now_sum == k:
            r += 1
            ans += 1
        else:
            now_sum -= cars[l]
            now_sum -= cars[r]
            l += 1
    return ans


with open("input.txt") as f:
    a, b = map(int, f.readline().split())
    c = list(map(int, f.readline().split()))

result = count_kit(a, b, c)
print(result)
