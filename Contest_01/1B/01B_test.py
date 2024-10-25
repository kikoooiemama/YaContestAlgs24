# Created by Nikolay Pakhomov 25.10.2024
def find_min(a_, b_, c_, d_):
    # в шкафу только 1 комплект цвета
    if a_ == 0:
        return (1, 1) if c_ == 0 else (1, c_ + 1)
    if b_ == 0:
        return (1, 1) if d_ == 0 else (1, d_ + 1)
    if c_ == 0:
        return (1, 1) if a_ == 0 else (a_ + 1, 1)
    if d_ == 0:
        return (1, 1) if b_ == 0 else (b_ + 1, 1)

    # в одинаковые значения
    if a_ == b_ and c_ == d_:
        if a_ > c_:
            return 1, c_ + 1
        else:
            return a_ + 1, 1
    elif a_ == b_ and c_ != d_:
        if a_ < max(c_, d_):
            return a_ + 1, 1
        else:
            return 1, min(c_, d_) + 1
    elif a_ != b_ and c_ == d_:
        if c_ < max(a_, b_):
            return 1, c_ + 1
        else:
            return min(a_, b_) + 1, 1

    # без одинаковых значений и нулей
    else:
        res = {}
        # способ 1
        bm_1 = b_ + 1
        rm_1 = a_ + 1
        bn_1 = d_ + 1
        rn_1 = c_ + 1
        res[bm_1 + bn_1] = (bm_1, bn_1)
        res[rm_1 + rn_1] = (rm_1, rn_1)
        # способ 2
        bm_2 = max(a_, b_) + 1
        bn_2 = 1
        rm_2 = 1
        rn_2 = max(c_, d_) + 1
        res[bm_2 + bn_2] = (bm_2, bn_2)
        res[rm_2 + rn_2] = (rm_2, rn_2)
        return res.get(min(res.keys()))


my_dir = "data/"
input_list = ["input1.txt", "input2.txt", "input3.txt", "input4.txt",
              "input5.txt", "input6.txt", "input7.txt", "input8.txt",
              "input9.txt", "input10.txt", "input11.txt"]
output_list = ["output1.txt", "output2.txt", "output3.txt", "output4.txt",
               "output5.txt", "output6.txt", "output7.txt", "output8.txt",
               "output9.txt", "output10.txt", "output11.txt"]

for i in range(len(output_list)):
    # Загрузка
    with open(my_dir + input_list[i]) as f:
        a, b, c, d = list(map(int, f.readlines()))
    # Исполняемый код
    m, n = find_min(a, b, c, d)
    # Загрузка
    with open(my_dir + output_list[i]) as f:
        answer = f.readline().strip()
    result = f"{m} {n}"
    # Результаты
    print(f"Test {i + 1}: {result == answer} [{result}, {answer}]")
