# Created by Nikolay Pakhomov 08.11.2024
def check_seq(seq):
    brackets = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for bracket in seq:
        if bracket in brackets.keys():
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return "no"
            if stack[-1] in brackets.keys():
                if brackets.get(stack[-1]) == bracket:
                    stack.pop(-1)
                else:
                    return "no"
            else:
                return "no"
    if len(stack) != 0:
        return "no"
    return "yes"


with open("input.txt") as f:
    string = f.readline().strip()

print(check_seq(string))
