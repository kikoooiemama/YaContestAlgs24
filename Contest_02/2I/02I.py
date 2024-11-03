# Created by Nikolay Pakhomov 27.10.2024
# 1 - воодушевление -> max(b)
# 0 - скучно -> max(a)
def find_order(n, a, b, p):
    result = []
    history = {}
    idx_list = []
    for i in range(1, n+1):
        idx_list.append(i)
        history[i] = 0
    idx_list = [i for i in range(1, n + 1)]
    # 'интерес' стек
    interest = sorted(list(zip(a, b, idx_list)), key=lambda x: (x[0], x[1], -x[2]), reverse=True)
    print(interest)
    # 2 стек
    utility = sorted(list(zip(a, b, idx_list)), key=lambda x: (x[1], x[0], -x[2]), reverse=True)
    print(utility)
    i = u = 0
    for mood in p:
        # 1 - воодушевление -> max(b)
        if mood:
            while history.get(utility[u][2]) and u < n:
                u += 1
            number = utility[u][2]
            history[number] = 1
            result.append(number)
        # # 1 - воодушевление -> max(b)
        else:
            while history.get(interest[i][2]) and i < n:
                i += 1
            number = interest[i][2]
            history[number] = 1
            result.append(number)
    return result


with open("input.txt") as f:
    days = int(f.readline().strip())
    a_list = list(map(int, f.readline().split()))
    b_list = list(map(int, f.readline().split()))
    p_list = list(map(int, f.readline().split()))

print(days)
print(f"a: {a_list}")
print(f"b: {b_list}")
print(f"p: {p_list}")
ans = find_order(days, a_list, b_list, p_list)
print(ans)
