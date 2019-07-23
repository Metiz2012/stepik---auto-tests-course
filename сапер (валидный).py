n,m,k = [int(i) for i in input().split()]
a=[[0 for i in range(m)]for j in range(n)]
print(a)
v=0
while v < k:
    print('Введите число не превышающее диапазон ', m, n)
    b, c = [int(z)for z in input().split()]
    if a[b][c] == (-1):
        print('Поле занято введите другие координаты')
    else :
        a[b][c] = -1
        v += 1

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai=i+di
                    aj=j+dj
                    if  n>ai>=0 and 0<=aj<m and a[ai][aj] == -1 :
                         a[i][j] += 1
for i in range (n):
    for j in range(m):
        if a[i][j] == -1:
            a[i][j] = '*'
        elif a[i][j] == 0:
            a[i][j] = '.'
print(a)