# Created by Nikolay Pakhomov 24.10.2024
with open('input.txt') as f:
    x1, y1, x2, y2, x, y = list(map(int, f.readlines()))

if x < x1:
    if y > y2:
        print("NW")
    elif y < y1:
        print("SW")
    else:
        print("W")
elif x > x2:
    if y > y2:
        print("NE")
    elif y < y1:
        print("SE")
    else:
        print("E")
else:
    if y > y2:
        print("N")
    else:
        print("S")
