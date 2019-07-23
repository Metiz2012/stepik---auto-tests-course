a = int(input())
b = int(input())
d=0
x=0
if   (a!=b!=0 and a!=0 and a%b==0 ) or a==b  :
     d=int(a)
elif a!=b!=0 and a!=0 and b%a==0  :
     d=int(b)

elif a!=b!=0 and a!=0 and (((a+b)%2==0) and (a%2==0 and b%2==0))and(a%10!=0 and b%10!=0)  :
    if a>b :
     x=a
     p=b
    else :
     x=b
     p=a
    while (x%2)==0:
           x/=2
    d=int(p*x)
elif a!=b!=0 and a!=0 and (a%10==0 and b%10==0)  :
    if a>b :
        x = a
        p = b
        x = b
        p = a
    while (x%10)==0:
           x/=10
    d=int(p*x)
elif a!=b!=0 and a!=0 and (((a+b)%3==0) and (a%3==0 and b%3==0))  :
    if a>b :
     x=a
     p=b
    else :
     x=b
     p=a
    while (x%3)==0:
           x/=3
    if x==1 :
        d = int(p * x)*3
    else:
        d=int(p*x)
elif b==0:
    d=a
elif a==0:
    d=b
else :
    d=a*b
print(d)