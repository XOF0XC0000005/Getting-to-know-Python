# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

while (True):
    number = input("Введите трехзначное число: ")

    if number.isdigit() == False:
        print("Введите число!")
    else:
        break
if int(number) < 100 or int(number) > 999:
    print("Введите трехзначное число!")

result = 0
initNumber = number
sequenceNums = ''

while (int(number) != 0):
    result = result + int(number) % 10
    number = int(number) / 10
print(initNumber, '->', result,
      '(', initNumber[0], '+', initNumber[1], '+', initNumber[2], ')')
