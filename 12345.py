a = int(input())
b = int(input())
c = int(input())
d = int(input())
i=1
for i in range(b-a+2) :
    if i==0 : continue
    else :
      for j in range(d-c+2) :
        if j==0:
            continue
        else :
          if j*i<10 :
              print('  ',end='')
          else :
              print(' ', end='')
          print (j*i,end='')
      print()








