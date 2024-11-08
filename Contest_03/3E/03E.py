# Created by Nikolay Pakhomov 04.11.2024
# Переведем из инфиксной записи в постфиксную и применим код из задачи D
# def check_correct(seq):
#     stack = []
#     is_correct = True
#     for s in seq:
#
#     return True


def calculate_postfix(postfix):
    stack = []
    for el in postfix:
        if el == "+":
            stack.append(stack.pop(-1) + stack.pop(-1))
        elif el == "*":
            stack.append(stack.pop(-1) * stack.pop(-1))
        elif el == "-":
            stack.append(-(stack.pop(-1) - stack.pop(-1)))
        else:
            stack.append(int(el))
    return stack[0]


def convert_to_postfix(infix):
    stack = []
    res = []
    for el in infix:
        if el in "+-*()":
            pass
        else:
            op = int(el)
            res.append(op)

    result = ""
    return result


with open("input.txt") as f:
    expression = f.readline().split()

# cr = check_correct(expression)
pf = convert_to_postfix(expression)
print(pf if pf == "WRONG" else calculate_postfix(pf))
