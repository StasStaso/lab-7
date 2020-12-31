import random

a = []
for i in range(8):
    b = []
    for j in range(8):
        x = random.randint(-1,10)
        b.append(x)
    a.append(b)
for i in range(len(a)):
    print(a[i])
for i in range(8):
    for j in range(8):
        if a[i][j] < 0:
            print("Сума а[{0}] рядку: {1} ".format(i,sum(a[i])))
            break

