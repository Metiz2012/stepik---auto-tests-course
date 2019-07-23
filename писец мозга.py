with open("C:/Users/ibelousov/Desktop/file.txt") as file_in, open ("C:/Users/ibelousov/Desktop/file2.txt") as file_out:
 alpha={}
 v=''
 key=''
 i=0
 for z in file_in : # Приведение текста к строке
    z=z.strip()
 while i < len(z):
     a = z[i]

     for j in range(i, (len(z))):
         if '0' <= a <= '9':
             v += v + 'a'

         else:
             key = a




