# Created by Nikolay Pakhomov 12.11.2024
import timeit

code_to_test = """
def get_psp(n, w, s):
    order = {"(": (0, ")"), ")": (0, "("), "[": (0, "]"), "]": (0, "[")}
    start = ""
    for i in range(len(w)):
        order[w[i]] = (i, order[w[i]][1])
        if len(start) == 0 and w[i] in "([":
            start += w[i]
    end = order[start][1]
    seq_type = 0 if order[start][0] < order[end][0] else 1
    stack = []
    for sym in s:
        if sym in "([":
            stack.append(sym)
        else:
            stack.pop(-1)
    stack.reverse()
    ending = [order[i][1] for i in stack]
    m = len(ending)
    k = n - len(s) - m
    result = s
    i = j = 0
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
    print(len(result))
    return result


with open("input_max.txt") as f:
    size = int(f.readline().strip())
    weight = f.readline().strip()
    first = f.readline().strip()

print(get_psp(size, weight, first))

"""
# вычисление времени выполнения кода
elapsed_time = timeit.timeit(code_to_test, number=100) / 100
print('Elapsed time: ', elapsed_time)
