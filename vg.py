n = [int(i)for i in input().split()]
x = int(input())
c = False

for i in range(len(n)-1) :
    if x==n[i] :
        print(i,end=' ')
        c = True
if  len(n)==1 and n[0]==0 and x==0 :
    c = True
    print(0, end=' ')
elif c == False : print('Отсутствует')
