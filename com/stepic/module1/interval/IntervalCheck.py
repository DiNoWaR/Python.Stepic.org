inInterval = False

x1 = -15
x2 = 12

y1 = 14
y2 = 17

z1 = 19

inputNumber = int(input(''))

if x1 < inputNumber <= x2 or y1 < inputNumber < y2 or inputNumber >= z1:
    inInterval = True

print(inInterval)
