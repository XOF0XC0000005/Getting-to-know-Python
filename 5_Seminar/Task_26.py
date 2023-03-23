# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def power(first_num, second_num):
    if second_num == 1:
        return first_num
    return int(first_num) * power(int(first_num), int(second_num) - 1)

first_number = input("Введите число: ")
second_number = input("Введите в какую степень требуется возвести: ")

print(f"A = {first_number}; B = {second_number} -> " + str(power(first_number, second_number)))