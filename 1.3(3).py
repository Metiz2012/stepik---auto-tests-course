a = str(input())
z = a.split(' ')

res = 0
for elem in z:
    if elem != '':
        res += int(elem)

print(res)