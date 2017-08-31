import math


def evaluate_triangle_square():
    a = float(input())
    b = float(input())
    c = float(input())

    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(s)


def evaluate_circle_square():
    r = float(input())
    s = 3.14 * r * r
    print(s)


def evaluate_rectangle_square():
    a = float(input())
    b = float(input())
    s = a * b
    print(s)


operation = input()

if operation == 'треугольник':
    evaluate_triangle_square()
elif operation == 'прямоугольник':
    evaluate_rectangle_square()
elif operation == 'круг':
    evaluate_circle_square()
