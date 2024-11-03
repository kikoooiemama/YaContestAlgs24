# Created by Nikolay Pakhomov 27.10.2024
def get_evidence_list(n, a, m, k, x):
    print(f"a: {a}")
    print(f"k: {k}")
    print(f"x: {x}")
    result = ""
    return result


with open("input.txt") as f:
    a_len = int(f.readline())
    a_list = list(map(int, f.readline().split()))
    x_len, max_shifts = map(int, f.readline().split())
    x_list = list(map(int, f.readline().split()))

ans = get_evidence_list(a_len, a_list, x_len, max_shifts, x_list)
print(ans.strip())
