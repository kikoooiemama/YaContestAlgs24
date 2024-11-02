# Created by Nikolay Pakhomov 27.10.2024
def find_max_len_substring(n, c, s):
    if n == 1:
        return 1
    # c - может быть 0!!!
    count_a = count_b = cur_c = 0  # подсчет текущей грубости, a, b
    i = r = best_l = best_r = 0  # 2 указателя
    while r < n:
        # добавление
        if s[r] == 'a':
            count_a += 1
        elif s[r] == 'b':
            count_b += 1
            cur_c += count_a
        # Грубость подстроки в пределах допустимого
        if cur_c <= c:
            if r - i > best_r - best_l:
                best_r, best_l = r, i
            r += 1
        # Грубость подстроки вышла за рамки
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

print(s_len, max_difficulty)
print(row)
ans = find_max_len_substring(s_len, max_difficulty, row)
print(ans)
