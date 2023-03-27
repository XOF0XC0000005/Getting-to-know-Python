import random

minimum = int(input("Введите начало диапазона: "))
maximum = int(input("Введите конец диапазона: "))
array = [random.randint(-10, 11) for _ in range(20)]
result_array = []
print(array)

for i in range(len(array)):
    if array[i] >= int(minimum) and array[i] <= int(maximum):
        result_array.append(i)
print(result_array)