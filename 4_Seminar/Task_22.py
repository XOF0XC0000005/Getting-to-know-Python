# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import random

first_subsequence_length = input("Введите длину первой последовательности: ")
second_subsequence_length = input("Введите дину второй последовательности: ")
dict_subsequence = {}
result = []

first_subsequence = [random.randint(1, 20) for _ in range(int(first_subsequence_length))]
second_subsequence = [random.randint(1, 20) for _ in range(int(second_subsequence_length))]


for i in range(len(first_subsequence)):
    if dict_subsequence.get(first_subsequence[i]) == None:
        dict_subsequence[first_subsequence[i]] = 1

for i in range(len(second_subsequence)):
    if dict_subsequence.get(second_subsequence[i]) == 1:
        dict_subsequence[second_subsequence[i]] += 1
        result.append(second_subsequence[i])
result.sort()

print(first_subsequence)
print("----------------")
print(second_subsequence)
print(*result)
