# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# Пример:
# 10 -> 1 2 4 8

while(True):
    n = input("Введите число: ")
    if(n.isdigit() == False or int(n) < 1):
        print("Введите число")
    else:
        break
    
i = 0
result = []
temp = 0

while(int(temp) <= int(n)):
    if((2 ** i) <= int(n)):
        result.append(2 ** i)
        temp = result[i]
        i = i + 1
    else:
        break
print(n, ' -> ', *result)