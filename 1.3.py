y = str(input())

resultA = 0
resultB = 0
for index in range(6):
    digit = int(y[index])
    if index <= 2:
        resultA += digit
    else:
        resultB += digit

print("Счастливый" if int(resultA) == int(resultB) else "Обычный")
