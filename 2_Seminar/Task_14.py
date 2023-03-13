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