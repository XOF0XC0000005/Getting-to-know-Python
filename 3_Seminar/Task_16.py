# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:
# Введите длину массива: 5
# Выводится массив рандомных чисел - 1 2 3 4 5
# Введите отслеживаемое число: 3
# число 3 -> 1

import random

array_length = input("Введите длину массива: ")
array = [random.randint(1, 10) for i in range(int(array_length))]
print(array)
find = input("Введите отслеживаемое число: ")

dict = {}

for i in range(len(array)):
    if dict.get(array[i]) == None:
        dict[array[i]] = 1
    else:
        dict[array[i]] += 1

print(f"число {find} -> {dict[int(find)]}")