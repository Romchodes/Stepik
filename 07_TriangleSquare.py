'''
В то далёкое время, когда Паша ходил в школу, ему очень не нравилась формула Герона для вычисления площади треугольника,
так как казалась слишком сложной. В один прекрасный момент Павел решил избавить всех школьников от страданий и написать
и распространить по школам программу, вычисляющую площадь треугольника по трём сторонам.
Одна проблема: так как эта формула не нравилась Павлу, он её не запомнил.
Помогите ему завершить доброе дело и напишите программу, вычисляющую площадь треугольника по переданным длинам трёх его
сторон по формуле Герона:
    S=sqrt(p(p−a)(p−b)(p−c))
где p=(a+b+c)/2 – полупериметр треугольника.
На вход программе подаются целые числа, выводом программы должно являться вещественное число,
соответствующее площади треугольника.
'''

import math

a = int(input('Введите длину стороны a: '))
b = int(input('Введите длину стороны b: '))
c = int(input('Введите длину стороны c: '))

def triangle_square(a, b, c):
    p = (a + b + c)/2
    s = math.sqrt(p*((p - a)*(p - b)*(p - c)))
    print('Площадь треугольника abc равна: ', s)

triangle_square(a, b, c)

'''
Верный ответ для отправки задания (без строчек, только код
'''
import math

a = int(input())
b = int(input())
c = int(input())

def triangle_square(a, b, c):
    p = (a + b + c)/2
    s = math.sqrt(p*((p - a)*(p - b)*(p - c)))
    print(s)

triangle_square(a, b, c)