line = 'W10z1I13p2F9B8M16I8z1u7l11w10B15T17p18M9h3w3U20p10'

collection = []

isLastWasDigit = False

currentString = ''
currentNumber = 0

for symbol in line:
    isDigit = symbol.isdigit()

    if isLastWasDigit and not isDigit:
        collection.append((currentString, currentNumber))
        currentString = ''
        currentNumber = 0

    if isDigit:
        currentNumber *= 10
        currentNumber += int(symbol)
    else:
        currentString += symbol

    isLastWasDigit = isDigit

if isLastWasDigit:
    collection.append((currentString, currentNumber))

for key, value in collection:
    print(key * value, end='')







