# Created by Nikolay Pakhomov 27.10.2024
def calculate_min_days(n, k, a):
    """
        1<= N <= 2*10^5, 0 <= k <= 10^9, 1 <= a_i <= 10^9
    """
    min_days = 0
    return min_days


with open("input.txt") as f:
    b, c = map(int, f.readline().split())
    al = list(map(int, f.readline().split()))

ans = calculate_min_days(b, c, al)
print(ans)
