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

first_subsequence = [random.randint(1, 20) for _ in range(int(first_subsequence_length))]
second_subsequence = [random.randint(1, 20) for _ in range(int(second_subsequence_length))]

first_subsequence_set = set(first_subsequence)
second_subsequence_set = set(second_subsequence)
result_subsequence = first_subsequence_set.intersection(second_subsequence_set)

print(first_subsequence)
print("----------------")
print(second_subsequence)
if(len(result_subsequence) == 0):
    print("Нет совпадений")
else:
    print(*sorted(result_subsequence))