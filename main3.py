import random

n = int(input("К-сть рядків: "))
m = int(input("К-сть стовпчів: "))
c = int(input("Введіть число: "))
a = []
for i in range(n):
    n = []
    for j in range(m):
        x = random.randint(0,9)
        n.append(x*c)
    a.append(n)
for i in range(len(a)):
    print(a[i])
