# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# Пример:
# 5 -> 1 0 1 1 0
# 2

import random

while(True):
    n = input("Введите количество монеток: ")
    if(n.isdigit() == False):
        print("Введите число или неотрицательное число")
    elif(int(n) <= 0):
        print("Введите число больше 0")
    else:
        break

coin_sides = list()

for i in range(int(n)):
    coin_sides.append(random.randint(0, 1))

if(coin_sides.count(1) < coin_sides.count(0)):
    print(n,' -> ',*coin_sides)
    print(coin_sides.count(1))
elif(coin_sides.count(1) == coin_sides.count(0)):
    print(n,' -> ',*coin_sides)
    print("Нет разницы")
else:
    print(n,' -> ',*coin_sides)
    print(coin_sides.count(0))
