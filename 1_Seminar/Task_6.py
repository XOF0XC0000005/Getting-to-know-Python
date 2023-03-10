# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*

# 385916 -> yes
# 123456 -> no

while (True):
    number = input("Введите шестизначное число: ")
    if number.isdigit() == False:
        print("Введите число!")
    elif int(number) < 100000 or int(number) > 999999:
        print("Введите шестизначное число!")
    else:
        break

right_side = 0
left_side = 0
initNumber = number

while (int(number) != 0):
    temp = int(number) % 10
    if (len(str(number)) > 3):
        right_side = right_side + temp
        number = int(number) // 10
    else:
        left_side = left_side + temp
        number = int(number) // 10

if (right_side == left_side):
    print(initNumber, '->', 'yes')
else:
    print(initNumber, '->', 'no')
