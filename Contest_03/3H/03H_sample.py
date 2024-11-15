# Created by Nikolay Pakhomov 04.11.2024
with open("input.txt") as f:
    n = int(f.readline().strip())
    stack_sum = [0]
    for i in range(n):
        s = f.readline().strip()
        if s == "-":
            op = '-'
        else:
            op, num = s[0], int(s[1:])
        if op == "+":
            stack_sum.append(stack_sum[-1] + num)
        if op == "-":
            print(stack_sum[-1] - stack_sum[-2])
            stack_sum.pop()
        if op == "?":
            print(stack_sum[-1] - stack_sum[-num - 1])
