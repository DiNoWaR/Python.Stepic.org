_first = float(input())
_second = float(input())
_operation = input()


def zero_divide():
    return 'Деление на 0!'


def calculate(first, second, operation):
    if operation == '+':
        print(first + second)
    elif operation == '-':
        if second < 0:
            second = second * (-1)
            print(first + second)
        else:
            print(first - second)
    elif operation == '*':
        print(first * second)
    elif operation == '/':
        if second == 0:
            print(zero_divide())
        else:
            print(first / second)
    elif operation == 'mod':
        if second == 0:
            print(zero_divide())
        else:
            print(first % second)
    elif operation == 'pow':
        print(first ** second)
    elif operation == 'div':
        if second == 0:
            print(zero_divide())
        else:
            print(first // second)


calculate(_first, _second, _operation)
