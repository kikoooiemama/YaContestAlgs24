# Created by Nikolay Pakhomov 27.10.2024
def get_median_idx(n):
    if n % 2 == 0:
        return n // 2 - 1
    else:
        return n // 2


def calculate_seq(n, a):
    result = ""
    for i in range(n):
        idx = get_median_idx(len(a))
        result += f" {a[idx]}"
        a.pop(idx)
    return result[1:]


with open("input.txt") as f:
    nn = int(f.readline().strip())
    al = list(map(int, f.readline().split()))

al.sort()
ans = calculate_seq(nn, al)
print(ans)
