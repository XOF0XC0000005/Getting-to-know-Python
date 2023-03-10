# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

while (True):
    n = input("Введите n: ")
    m = input("Введите m: ")
    k = input("Введите число долек: ")

    if (n.isdigit() == False or m.isdigit() == False or k.isdigit() == False):
        # Не хотелось усложнять try except
        print("Введите числа или неотрицательные числа!)")
    else:
        break
if (int(n) * int(m) == int(k)):
    print("Бери всю шоколадку")
elif (int(k) > int(n) * int(m) or int(k) <= 0):
    print("Столько долек нет")
elif (n == k or m == k or int(k) % int(n) == 0 or int(k) % int(m) == 0):
    print(n, m, k, '-> yes')
else:
    print(n, m, k, '-> no')
