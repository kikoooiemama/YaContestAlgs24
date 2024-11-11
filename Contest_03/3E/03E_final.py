# Created by Nikolay Pakhomov 04.11.2024
def check_correct(string):
    if len(string) == 0:
        return "WRONG"
    previous = -1
    un = False
    counter = 0
    res = []
    i = 0
    while i < len(string):
        if string[i] == "-" and i == 0:
            j = i + 1
            if j < len(string) and string[j].isdigit():
                un = True
            i += 1
            continue
        if string[i].isdigit():
            num = string[i]
            i += 1
            while i < len(string) and string[i].isdigit():
                num += string[i]
                i += 1
            if previous == 0:
                return "WRONG"
            else:
                if un:
                    res.append("0")
                    res.append("-")
                    res.append(num)
                    un = False
                else:
                    res.append(num)
                previous = 0
            continue
        if string[i] in "+*":
            if previous != -1 and previous != 0 and previous != 3:
                return "WRONG"
            else:
                res.append(string[i])
                previous = 1
        if string[i] == "-":
            if previous == 1 or previous == 4:
                return "WRONG"
            if previous == 2:
                j = i + 1
                if j < len(string) and string[j].isdigit():
                    un = True
            else:
                res.append(string[i])
                previous = 4
        if string[i] == "(":
            counter += 1
            if previous == 0 or previous == 3:
                return "WRONG"
            else:
                res.append(string[i])
                previous = 2
        if string[i] == ")":
            counter -= 1
            if previous != -1 and previous != 0 and previous != 3:
                return "WRONG"
            else:
                res.append(string[i])
                previous = 3
        i += 1

    if len(res) == 0:
        return "WRONG"
    if counter != 0 or res[-1] in "*+-(" or res[0] in "*+":
        return "WRONG"
    return res


def calculate_postfix(postfix):
    if len(postfix) == 1:
        if postfix[0].isdigit():
            return postfix[0]
        else:
            return "WRONG"
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
    if len(stack) == 0:
        return "WRONG"
    return stack[0]


def convert_to_postfix(infix):
    stack = []
    res = []
    for el in infix:
        if el in "+-*":
            if el in "+-":
                j = len(stack) - 1
                while j > -1:
                    if stack[j] == "(":
                        break
                    res.append(stack.pop(-1))
                    j -= 1
            else:
                j = len(stack) - 1
                while j > -1:
                    if stack[j] == "(" or stack[j] in "+-":
                        break
                    res.append(stack.pop(-1))
                    j -= 1
            stack.append(el)
        elif el == "(":
            stack.append(el)
        elif el == ")":
            j = len(stack) - 1
            while j > -1 and stack[j] != "(":
                res.append(stack.pop(-1))
                j -= 1
            stack.pop(-1)
        else:
            res.append(el)
    for i in range(len(stack) - 1, -1, -1):
        res.append(stack.pop(i))
    return res


with open("input.txt") as f:
    expression = f.readline().strip()

cr = check_correct(expression)
print(cr if cr == "WRONG" else calculate_postfix(convert_to_postfix(cr)))
