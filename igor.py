a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(' ', end='')
for i in range(c, d + 1, 1):
    print('  ', i, end='')
print()
for j in range(a, b + 1, 1):
    print(j, end='')
    for k in range(c, d + 1, 1):
        print(j * k, end='')
    print()
