# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai . Последняя строка содержит число X

# Пример
# Введите длину массмва: 5
# Вывод массива - 1 2 3 4 5
# Введите отслеживаемое число 6
# Самое близжайшее число к 6 -> 5

import random

array_length = input("Введите длину массива: ")
array = [random.randint(1, 40) for _ in range(int(array_length))]
print(array)
find = input("Введите отслеживаемое число: ")

result = array[0]
temp = abs(int(find) - array[0])

for i in range(len(array) - 1):
    if abs(int(find) - array[i + 1]) < temp:
        temp = abs(int(find) - array[i + 1])
        result = array[i + 1]
        if temp == abs(int(find) - array[i + 1] and result > array[i + 1]):
            result = array[i + 1]
print('-> ' + str(result))