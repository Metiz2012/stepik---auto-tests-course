a = int(input())
b = int(input())
c = int(input())
d = int(input())

print('  ', end='')

for i in range(c, d + 1, 1):
    space = ' ' if (i < 10) else ''
    print('\t' + str(i) + space, end='')

print()

for i in range(a, b + 1, 1):
    space = ' ' if (i < 10) else ''
    print(str(i) + space, end='')

    for j in range(c, d + 1, 1):
        multi = i * j
        space = ' ' if (multi < 10) else ''
        print('\t' + str(multi) + space, end='')

    print()

