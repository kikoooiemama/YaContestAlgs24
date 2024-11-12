# Created by Nikolay Pakhomov 12.11.2024
import timeit

code_to_test = """
with open("input_time.txt") as f:
    n, b = map(int, f.readline().split())
    a = list(map(int, f.readline().split()))
sum_time = a[0]
clients = a[0]
for i in range(1, n):
    clients -= b
    if clients < 0:
        clients = 0
    clients += a[i]
    sum_time += clients
clients -= b
if clients < 0:
    clients = 0
sum_time += clients
print(sum_time)

"""
# вычисление времени выполнения кода
elapsed_time = timeit.timeit(code_to_test, number=100) / 100
print('Elapsed time: ', elapsed_time)
