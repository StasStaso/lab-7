n = int(input("К-сть рядків: "))
m = int(input("К-сть стовпчів: "))
A = [[int(input("A[{0}][{1}] = ".format(i,j))) for j in range(0, m)] for i in range(0, n)]
for k in A:
    print(k)
s = 1
for i in range(n):
    for j in range(m):
        if A[i][j] % 2 == 0 and A[i][j] > 0:
            s *= A[i][j]
print("Добуток додатних парних елементів матриці = {0}".format(s))
