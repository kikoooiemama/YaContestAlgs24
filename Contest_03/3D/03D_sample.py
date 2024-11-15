# Created by Nikolay Pakhomov 04.11.2024
with open("input.txt") as f:
    inp_list = f.readline().split()
stack = []
for now in inp_list:
    if now.isdigit():
        stack.append(int(now))
    else:
        param2 = stack[-1]
        param1 = stack[-2]
        stack.pop()
        stack.pop()
        if now == "+":
            stack.append(param1 + param2)
        if now == "*":
            stack.append(param1 * param2)
        if now == "-":
            stack.append(param1 - param2)
print(stack[0])
