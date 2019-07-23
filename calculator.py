a = float(input())
b = float(input())
c = str(input())
z = 0
if c == "+":
    z = a + b
    print(z)
elif c == "-":
    z = a - b
    print(z)
elif c == "/":
    if b != 0:
        z = a / b
        print(z)
    else:
        print("Деление на 0!")
elif c == "*":
    z = a * b
    print(z)
elif c == "mod":
    if b != 0:
        z = a % b
        print(z)
    else:
        print("Деление на 0!")
elif c == "pow":
    z = a ** b
    print(z)
elif c == "div":
    if b != 0:
        z = a // b
        print(z)
    else:
        print("Деление на 0!")
else:
    print("Данная операция не поддерживается")
