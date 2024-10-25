# Created by Nikolay Pakhomov 25.10.2024

def find(x1_, y1_, x2_, y2_, x_, y_):
    if x_ < x1_:
        if y_ > y2_:
            return "NW"
        elif y_ < y1_:
            return "SW"
        else:
            return "W"
    elif x_ > x2_:
        if y_ > y2_:
            return "NE"
        elif y_ < y1_:
            return "SE"
        else:
            return "E"
    else:
        if y_ > y2_:
            return "N"
        else:
            return "S"


my_dir = "data/"
input_list = ["input1.txt", "input2.txt", "input3.txt", "input4.txt",
              "input5.txt", "input6.txt", "input7.txt", "input8.txt"]
output_list = ["output1.txt", "output2.txt", "output3.txt", "output4.txt",
               "output5.txt", "output6.txt", "output7.txt", "output8.txt"]

for i in range(len(output_list)):
    # Загрузка
    with open(my_dir + input_list[i]) as f:
        x1, y1, x2, y2, x, y = list(map(int, f.readlines()))
    # Исполняемый код
    result = find(x1, y1, x2, y2, x, y)
    # Загрузка
    with open(my_dir + output_list[i]) as f:
        answer = f.readline().strip()
    # Результаты
    print(f"Test {i + 1}: {result == answer} [{result}, {answer}]")
