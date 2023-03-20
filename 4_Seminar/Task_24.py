# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9
import random

beds_number = input("Введите количество грядок: ")
beds_array = [random.randint(1, 10) for _ in range(int(beds_number))]
print(beds_array)
if(len(beds_array) == 1):
    result = beds_array[0]
elif(len(beds_array) == 2):
    result = beds_array[0] + beds_array[1]
else:
    last_element = beds_array[0]
    last_element_index = 0
    next_element = beds_array[2]
    next_element_index = 2
    temp = beds_array[0] + beds_array[1] + beds_array[2]
    result = temp
    for i in range(2, len(beds_array)):
        if(i == len(beds_array) - 1):
            break
        next_element = beds_array[next_element_index + 1]
        next_element_index += 1
        temp += next_element - last_element
        last_element = beds_array[last_element_index + 1]
        last_element_index += 1
        if result < temp:
            result = temp
print(result)
