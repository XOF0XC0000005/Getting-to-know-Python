x, y = map(int, input("X, Y = ").split())
flag = False
for i in range(x + y):
    if flag:
        break
    for j in range(x + y):
        if i + j == x and i * j == y:
            flag = True
            print(*sorted([i, j]))
            break