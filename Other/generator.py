# Created by Nikolay Pakhomov 02.11.2024
import random

n = 2 * 10 ** 5
m = n - 1
height = 10 ** 9
print(f"n: {n}, m: {m}, height: {height}")
line0 = f"{n} {height}\n"
h = [i for i in range(999800000, 1000000000)]
h.reverse()
w = [5000] * n
print(len(h))
print(len(w))
print(h[:10])
print(w[:10])
line1 = " ".join(list(map(str, h))) + '\n'
line2 = " ".join(list(map(str, w))) + '\n'
with open("../Contest_03/3J/input_time5.txt", "w") as f:
    f.write(line0)
    f.write(line1)
    f.write(line2)

#
# # a = [(random.randint(999900000, 1000000000)) for i in range(100000)]
# a = [i for i in range(999900000, 1000000000)]
# line1 = " ".join(list(map(str, a))) + '\n'
# # b = [(random.randint(999900000, 1000000000)) for i in range(100000)]
# b = [i for i in range(999800000, 999900000)]
# line2 = " ".join(list(map(str, b))) + '\n'
# c = [random.randint(0, 1) for i in range(100000)]
# line3 = " ".join(list(map(str, c))) + '\n'
# print(len(a))
# print(len(b))
# print(len(c))
# print(f"{len(a) == len(b) == len(c)}")
# line0 = f"100000\n"
# with open("../Contest_03/3H/input_m.txt", "w") as f:
#     f.write(line0)
#     for i in range(50000):
#         linei = "+1000000000\n"
#         f.write(linei)
#     for i in range(50000):
#         linei = "-\n"
#         f.write(linei)
#     # f.write(line1)
#     # f.write(line2)
#     # f.write(line3)
