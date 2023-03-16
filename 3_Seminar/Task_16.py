import random

array_length = input("Введите длину массива: ")
array = [random.randint(1, 10) for i in range(int(array_length))]
print(array)
find = input("Введите отслеживаемое число: ")

dict = {}

for i in range(len(array)):
    if dict.get(array[i]) == None:
        dict[array[i]] = 1
    else:
        dict[array[i]] += 1

print(f"число {find} -> {dict[int(find)]}")