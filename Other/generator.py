# Created by Nikolay Pakhomov 02.11.2024
import random

line0 = f"100000\n"
# a = [(random.randint(999900000, 1000000000)) for i in range(100000)]
a = [i for i in range(999900000, 1000000000)]
line1 = " ".join(list(map(str, a))) + '\n'
# b = [(random.randint(999900000, 1000000000)) for i in range(100000)]
b = [i for i in range(999800000, 999900000)]
line2 = " ".join(list(map(str, b))) + '\n'
c = [random.randint(0, 1) for i in range(100000)]
line3 = " ".join(list(map(str, c))) + '\n'
print(len(a))
print(len(b))
print(len(c))
print(f"{len(a) == len(b) == len(c)}")
with open("../Contest_02/2I/input_sort.txt", "w") as f:
    f.write(line0)
    f.write(line1)
    f.write(line2)
    f.write(line3)
