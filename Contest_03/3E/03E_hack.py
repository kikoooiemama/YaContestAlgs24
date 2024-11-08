# Created by Nikolay Pakhomov 08.11.2024
with open("input.txt") as f:
    expression = f.readline()
try:
    a = eval(expression)
except (TypeError, SyntaxError, NameError):
    a = "WRONG"
print(a)
