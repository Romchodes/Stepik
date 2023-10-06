'''
Напишите программу, которая получает на вход три целых числа, по одному числу в строке,
и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.
3 2 1
2 3 1
2 1 3
5 5 2
'''

def max_min_counter(a, b, c):
    if a > b and a > c and c > b:
        max = a
        min = b
        avr = c
    elif a > b and a > c and b == c:
        max = a
        min = b
        avr = c
    elif a > b > c:
        max = a
        min = c
        avr = b
    elif a > c and b > c and a == b:
        max = a
        min = c
        avr = b
    elif a > b and c > b and a == c:
        max = a
        min = b
        avr = c
    elif a == b == c:
        max = a
        min = b
        avr = c
    elif b > a and b > c and c > a:
        max = b
        min = a
        avr = c
    elif b > a > c:
        max = b
        min = c
        avr = a
    elif b > a and b > c and a == c:
        max = b
        min = c
        avr = a
    elif b > a and c > a and b == c:
        max = b
        min = a
        avr = c
    elif c > b > a:
        max = c
        min = a
        avr = b
    elif c > b and c > a and a == b:
        max = c
        min = a
        avr = b
    elif c > b and c > a and a > b:
        max = c
        min = b
        avr = a
    print(max)
    print(min)
    print(avr)

a = int(input())
b = int(input())
c = int(input())

max_min_counter(a, b, c)