x=str(input())
a=0
b=0
for i in range(6):
    z=int(x[i])
    if i<=2:
        a+=z
    else:
        b+=z
print ("Счастливый" if a==b  else ("Обычный"))

