# Created by Nikolay Pakhomov 27.10.2024
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
