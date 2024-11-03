# Created by Nikolay Pakhomov 03.11.2024
import timeit

code_to_test = """

"""
# вычисление времени выполнения кода
elapsed_time = timeit.timeit(code_to_test, number=100) / 100
print('Elapsed time: ', elapsed_time)