# Created by Nikolay Pakhomov 12.02.2025
import random


# 1. Быстрая сортировка (Схема Хоара)
# Делим массив на 2. a[l, r] <= a[q] < a[q + 1, r]
# a[l, r] и a[q + 1, r] сортируются рекурсивным вызовом функции быстрой сортировки.
# Partition - алгоритм разбиения: В качестве разделяющего элемента берется обычно середина [left + right // 2].
# Далее начинается просмотр с левого конца массива до тех пор пока не найден элемент превосходящий разделяющий.
# Потом начинается просмотр с правого конца массива до тех пор пока не найдется элемент по значению меньше разделяющего.
# Найденные элементы меняются местами и таким образом получается, что справа нет ни одного элемента меньше разделяющего,
# а слева нет ни одного элемента больше разделяющего.
def partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i = i + 1
        while arr[i] < pivot:
            i += 1
        j = j - 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(nums):
    def _quick_sort(array, left, right):
        if left < right:
            split_index = partition(array, left, right)
            _quick_sort(array, left, split_index)  # a[l, q]
            _quick_sort(array, split_index + 1, right)  # [q + 1, r]

    _quick_sort(nums, 0, len(nums) - 1)


# 1a. Быстрая сортировка (Версия 2.0). Здесь памяти тратиться больше.
def quick_sort_short(array):
    if len(array) < 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort_short(less) + [pivot] + quick_sort_short(greater)


# 2. Сортировка пузырьком (Bubble sort).
# Алгоритм перестановок.
# Проходим несколько раз по элементам массива по порядку. Берем первую пару, если первое число больше второго, то нужно
# сделать перестановку между ними. Потом переходим к следующей паре и также либо переставляем, либо нет.
# Проверки пар проводятся до тех пока не случиться удачного прохода. А удачный проход - проход без перестановок.

def bubble_sort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True


# 3. Сортировка вставками (Insertion sort).
# В чем идея. Мы берем 1 элемент из исходного массива и решаем куда его вставить. В начальный момент времени
# отсортированная последовательность пуста соответственно.
# Последовательно берем числа их исходной последовательности и сравниваем его со всеми в отсортированной
# последовательности, определяя, таким образом, его место. Если число i меньше чем предыдущее число j, то нужно сдвинуть
# предыдущее вперед на 1, а i число вставить на его место.
def insertion_sort(array):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i - 1
        # если предыдущее число больше
        while j >= 0 and array[j] > item_to_insert:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = item_to_insert  # так как делаем j -= 1, то надо поставить +1


# Проверка алгоритмов.
N = 35
L = range(100)
random_array = [random.choice(L) for _ in range(N)]
print("Исходный массив:")
print(random_array)
print("Сортировка:")
choara = random_array.copy()
quick_sort(choara)
print(choara)
print(quick_sort_short(random_array.copy()))
bubble = random_array.copy()
bubble_sort(bubble)
print(bubble)
insertion = random_array.copy()
insertion_sort(insertion)
print(insertion)
print("Ответ:")
print(sorted(random_array.copy()))
