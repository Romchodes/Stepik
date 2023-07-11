'''
Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают треугольные, прямоугольные и круглые.
Чтобы быстро вычислять жилплощадь, требуется написать программу,
на вход которой подаётся тип фигуры комнаты и соответствующие параметры,
которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.
Формат ввода, который используют Малевийцы:

треугольник
a
b
c
где a, b и c — длины сторон треугольника

прямоугольник
a
b
где a и b — длины сторон прямоугольника

круг
r
где r — радиус окружности
'''

import math
def triangle_square(a, b, c): # треугольник
    p = (a + b + c)/2
    s = math.sqrt(p*((p - a)*(p - b)*(p - c)))
    print('Площадь треугольника равна: ', s, '\n---------------')

def rectangle_square(a,b): # прямоугольник
    s = a * b
    print('Площадь прямоугольника равна: ', s, '\n---------------')

def circle_square(r):
    s = 3.14 * (r ** 2)
    print('Площадь круга равна: ', s, '\n---------------')

while True:
    figure = input('Введите название фигуры (прямоугольник, круг, треугольник): ')
    if figure == 'треугольник':
        a = float(input('Введите сторону a: '))
        b = float(input('Введите сторону b: '))
        c = float(input('Введите сторону c: '))
        triangle_square(a, b, c)
    elif figure == 'прямоугольник':
        a = float(input('Введите сторону a: '))
        b = float(input('Введите сторону b: '))
        rectangle_square(a, b)
    elif figure == 'круг':
        r = float(input('Введите радиус круга: '))
        circle_square(r)
    else:
        print('Неверно введено название фигуры\n---------------')