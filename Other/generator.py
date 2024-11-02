# Created by Nikolay Pakhomov 02.11.2024

line0 = f"190002\n"
line1 = "1 " + "1000000000 " * 190000 + "1000000000" + "\n"
with open("../Contest_02/2H/input_max2.txt", "w") as f:
    f.write(line0)
    f.write(line1)
