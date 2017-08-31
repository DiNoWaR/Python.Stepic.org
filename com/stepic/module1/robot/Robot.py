main_word = 'программист'

ending_with_a = 'а'
ending_with_ov = 'ов'
ending_with_empty = ''

result = None

number = int(input())


if number % 10 == 0 or number % 5 == 0:
    result = str(number) + ' ' + main_word + ending_with_ov
elif str(number).endswith('2') or str(number).endswith('3') or str(number).endswith('4'):

    if str(number).endswith('12') or str(number).endswith('13') or str(number).endswith('14'):
        result = str(number) + ' ' + main_word + ending_with_ov
    else:
        result = str(number) + ' ' + main_word + ending_with_a

elif str(number).endswith('1'):

    if str(number).endswith('11'):
        result = str(number) + ' ' + main_word + ending_with_ov
    else:
        result = str(number) + ' ' + main_word + ending_with_empty
else:
    result = str(number) + ' ' + main_word + ending_with_ov


print(result)
