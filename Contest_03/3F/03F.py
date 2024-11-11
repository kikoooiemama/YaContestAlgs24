# Created by Nikolay Pakhomov 04.11.2024
def get_psp(n, w, s):
    order = {"(": (0, ")"), ")": (0, "("), "[": (0, "]"), "]": (0, "[")}
    # Если у строк A, B одинаковые подстроки s, то если A_s+1 < B_s+1, то A < B.
    start = ""
    for i in range(len(w)):
        order[w[i]] = (i, order[w[i]][1])
        if len(start) == 0 and w[i] in "([":
            start += w[i]
    end = order[start][1]
    # type 0 - вложенные, type 1 - последовательность
    seq_type = 0 if order[start][0] < order[end][0] else 1
    # Формируем ending
    stack = []
    for sym in s:
        if sym in "([":
            stack.append(sym)
        else:
            stack.pop(-1)
    stack.reverse()
    ending = [order[i][1] for i in stack]
    # ending = list(map(replace, stack))
    # Считываем сколько нужно доставить скобок.
    m = len(ending)
    k = n - len(s) - m
    print(f"k: {k}")
    result = s
    i = 0  # по k,
    j = 0  # по m, ending
    while len(result) < n:
        cur_close_value = order.get(ending[j])[0] if j < m else 100
        if i < k and order.get(start)[0] < cur_close_value:
            if seq_type:
                result += f"{start}{end}" * int(k / 2)
            else:
                result += start * int(k / 2)
                result += end * int(k / 2)
            i = k
        else:
            result += ending[j]
            j += 1
    return result


with open("input.txt") as f:
    size = int(f.readline().strip())
    weight = f.readline().strip()
    first = f.readline().strip()

print(get_psp(size, weight, first))
