code = open("C:/Users/ibelousov/Desktop/file.txt", 'r').readline()

result = ''
alpha = ''
digit = 0

for i in code:
    if i.isalpha():
        result += alpha * digit
        alpha = i
        digit = 0
    if i.isdigit():
        digit = int(str(digit) + i)

result += alpha * digit

print(result)