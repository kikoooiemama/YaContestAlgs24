# Created by Nikolay Pakhomov 04.11.2024
def eval_postfix(inp_list):
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
    return stack[0]


def make_postfix(infix_tokens):
    ops = {'+', '-', '*'}
    brackets = {'(', ')'}
    postfix_tokens = []
    prev_type = 'op'
    stack = []
    for token in infix_tokens:
        if token in ops and prev_type != 'num':
            return ["WRONG"]
        if token in ops:
            # выталкивание операций равных или больших по приоритету.
            while (token == "*" and len(stack) > 0 and stack[-1] == '*') or \
                    (token == "+" or token == "-") and (len(stack) > 0 and stack[-1] in ops):
                postfix_tokens.append(stack.pop())
            stack.append(token)
            prev_type = 'op'
        elif token.isdigit():
            if prev_type == 'num':
                return ['WRONG']
            postfix_tokens.append(token)
            prev_type = 'num'
        elif token in brackets:
            if token == '(':
                if prev_type == 'num':
                    return ["WRONG"]
                stack.append(token)
                prev_type = 'bracket'
            else:
                while len(stack) > 0 and stack[-1] != '(':
                    postfix_tokens.append(stack.pop())
                if len(stack) == 0:
                    return ["WRONG"]
                stack.pop()
        else:
            return ["WRONG"]
    if prev_type != 'num':
        return ['WRONG']
    # остаток стека надо записать в postfix_tokens
    while len(stack) > 0:
        if stack[-1] == '(':
            return ["WRONG"]
        postfix_tokens.append(stack.pop())
    return postfix_tokens


with open("input.txt") as f:
    expression = f.readline().strip()
if expression[0] == "-":
    expression = '0' + expression
expression = expression.replace('(-', '(0-')
symbols = ['+', '-', '*', '(', ')']
# добавляем пробелы между каждым элементом, т.к. python split умеет сплитить при нескольких пробелах без проблем
for ch in symbols:
    expression = expression.replace(ch, ' ' + ch + ' ')
tokens = make_postfix(expression.split())
if len(tokens) == 1:
    print(tokens[0])
else:
    print(eval_postfix(tokens))
