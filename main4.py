n = int(input("n = "))
a = [[int(input("A[{0}][{1}] = ".format(i,j))) for j in range(0, n)] for i in range(0, n)]
for k in range(n):
    print(a[k])
print('-'*(n*3))


for j in range(n):
    if j %2 != 0:
        b =[]
        for i in range(n):
            b.append(a[i][j])
        b = sorted(b, reverse= True)
        for i in range(n):
            a[i][j] = b[i]
for i in range(n):
    print(a[i])
