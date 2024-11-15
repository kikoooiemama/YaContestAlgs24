# Created by Nikolay Pakhomov 04.11.2024
def check(s):
    closing = {')': '(', ']': '[', '}': '{'}
    stack = []
    for c in s:
        if c in closing:
            if len(stack) == 0 or stack[-1] != closing[c]:
                return False
            stack.pop()
        else:
            stack.append(c)
    return len(stack) == 0


with open("input.txt") as f:
    string = f.readline().strip()

if check(string):
    print('yes')
else:
    print('no')
