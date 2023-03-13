while(True):
    n = input("Введите количество монеток: ")
    if(n.isdigit() == False):
        print("Введите число или неотрицательное число")
    else:
        break

coin_sides = list()

for i in range(int(n)):
    while(True):
        t = input("Введите число: ")
        if(t.isdigit() == False or (int(t) != 0 and int(t) != 1)):
            print("Введите число (0 или 1)")
        else:
            coin_sides.append(int(t))
            break

if(coin_sides.count(1) < coin_sides.count(0)):
    print(n,' -> ',*coin_sides)
    print(coin_sides.count(1))
elif(coin_sides.count(1) == coin_sides.count(0)):
    print(n,' -> ',*coin_sides)
    print("Нет разницы")
else:
    print(n,' -> ',*coin_sides)
    print(coin_sides.count(0))
