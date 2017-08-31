usual = 'Обычный'
lucky = 'Счастливый'

input_string = input()

first_number = int(input_string[0:3])
second_number = int(input_string[-3:])

z1 = first_number % 10
y1 = (first_number % 100) // 10
x1 = first_number // 100

z2 = second_number % 10
y2 = (second_number % 100) // 10
x2 = second_number // 100

if x1 + y1 + z1 == x2 + y2 + z2:
    print(lucky)
else:
    print(usual)