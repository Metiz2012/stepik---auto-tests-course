def closest_mod_5(x) :
    x=int(input())
    z=x
    y=0
    for i in range(5):
       if z%5==0 and y>=z :
           return(y)

       elif z%5==0 and y<z :
            y=x+5
            return (y)
       else :
          z=z+1
    y=z
print(y)

closest_mod_5(5)

