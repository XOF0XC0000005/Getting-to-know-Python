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
