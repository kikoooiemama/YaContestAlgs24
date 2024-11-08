# Created by Nikolay Pakhomov 08.11.2024

try:
    a = eval("(1 + ) * 5")
except (TypeError, SyntaxError):
    a = "WRONG"
print(a)
