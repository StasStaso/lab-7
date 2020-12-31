import math

n = int(input("К-сть рядків: "))
m = int(input("К-сть стовпчів: "))
c = int(input("Введіть число: "))
a = []
b = []
for i in range(1,n+1):
    n = []
    for j in range(1,m+1):
        x = round(j*math.cos(i**2+c),2)
        n.append(x)
    a.append(n)
for i in range(len(a)):
    for j in range(m):
        if (i+j) % 2 != 0:
            b.append(a[i][j])
for i in range(len(a)):
    print(a[i])
print("Суму елементів матриці А, сума індексів яких непарна = {0}".format(sum(b)))
