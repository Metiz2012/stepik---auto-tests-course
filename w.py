x = int(input())

a = x // 1000
b = x % 1000


def getSum(variable):
    result = 0
    for index in range(3):
        temp = (100 / (10 ** index))
        result += variable // temp
        variable = variable % temp

    return int(result)


print("Счастливый" if getSum(a) == getSum(b) else "Обычный")
