# Открытие тхт файла
with open("C:/Users/ibelousov/Desktop/file.txt") as s:
    vvod = s.read().strip().lower()
z = list(vvod.split())

# Алгоритм с записью в словарь. Ключ- сама комбинация букв, значение-счетчик внутри
x = {}
for i in z:
    if i not in x:
        x[i] = 1
    elif i in x:
        x[i] += 1
print(x)

# Непосредственный вывод максимального значения в словаре
count = 0
for key, value in x.items():
    if value > count:
        z = key
        x = value
        count = x
    else:
        continue
print(z, x)