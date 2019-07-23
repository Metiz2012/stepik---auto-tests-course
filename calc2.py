a = float(input())
b = float(input())
c = str(input())
z = 0


def calc(operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "/":
        return a / b
    elif operation == "*":
        return a * b
    elif operation == "mod":
        return a % b
    elif operation == "pow":
        return a ** b
    elif operation == "div":
        return a // b
    else:
        return None


try:
    print(calc(c))
except ZeroDivisionError:
    print('Деление на 0!')


