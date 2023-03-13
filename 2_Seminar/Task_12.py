a, b = map(int, input("a, b = ").split())
c = 0
for i in range(a + b):
    if c:
        break
    for j in range(a + b):
        if i + j == a and i * j == b:
            c = 1
            print(*sorted([i, j]))
            break