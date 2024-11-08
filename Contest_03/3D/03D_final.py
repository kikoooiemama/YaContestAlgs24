# Created by Nikolay Pakhomov 04.11.2024
with open("input.txt") as f:
    postfix = f.readline().strip().split()

stack = []
for el in postfix:
    a, b = 0, 0
    if el == "+":
        stack.append(stack.pop(-1) + stack.pop(-1))
    elif el == "*":
        stack.append(stack.pop(-1) * stack.pop(-1))
    elif el == "-":
        stack.append(-(stack.pop(-1) - stack.pop(-1)))
    else:
        stack.append(int(el))
print(stack[0])
