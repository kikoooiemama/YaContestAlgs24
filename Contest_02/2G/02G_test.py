# Created by Nikolay Pakhomov 02.11.2024
def find_max_len_substring(n, c, s):
    count_a = count_b = cur_c = 0
    i = r = best_l = best_r = 0
    while r < n:
        if s[r] == 'a':
            count_a += 1
        elif s[r] == 'b':
            count_b += 1
            cur_c += count_a
        if cur_c <= c:
            if r - i > best_r - best_l:
                best_r, best_l = r, i
            r += 1
        else:
            while i < n and cur_c > c:
                if s[i] == 'a':
                    count_a -= 1
                    cur_c -= count_b
                if s[i] == 'b':
                    count_b -= 1
                i += 1
            if cur_c <= c:
                if r - i > best_r - best_l:
                    best_r, best_l = r, i
                r += 1

    return best_r - best_l + 1


with open("input.txt") as f:
    s_len, max_difficulty = map(int, f.readline().split())
    row = f.readline().strip()

ans = find_max_len_substring(s_len, max_difficulty, row)
print(ans)


n_list = []
c_list = []
s_list = []
result_list = []
with open('input_test.txt') as f:
    test_n = int(f.readline().strip())
    for i in range(test_n):
        f.readline()
        nn, kk = map(int, f.readline().split())
        aa = f.readline().strip()
        n_list.append(nn)
        c_list.append(kk)
        s_list.append(aa)

with open('output_test.txt') as f:
    for i in range(test_n):
        result_list.append(int(f.readline().strip()))

for i in range(test_n):
    res = find_max_len_substring(n_list[i], c_list[i], s_list[i])
    print(f"Result: {res}, Answer: {result_list[i]}, Right: {res == result_list[i]}")
