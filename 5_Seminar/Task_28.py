# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# 2 2
# 4

def sum(first_num, second_num):
    
    if int(second_num) == 0:
        return int(first_num)
    return 1 + sum(first_num, second_num - 1)

print(sum(25, 10))