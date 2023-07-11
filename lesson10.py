'''
Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
первое число,
второе число
и операцию,
после чего применяет операцию к введённым числам ("первое число" "операция" "второе число")
и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.
'''

first = float(input())
second = float(input())
operation = input()

def calculation():
    if second == 0 and (operation == '/' or operation == 'mod' or operation == 'div'): # можно operation in ('/', 'mod', 'div')
        print('Деление на 0!')
    elif operation == 'mod':
        answer = (first % second)
        print(answer)
    elif operation == 'pow':
        answer = (first ** second)
        print(answer)
    elif operation == 'div':
        answer = (first // second)
        print(answer)
    elif operation == '+':
        answer = (first + second)
        print(answer)
    elif operation == '-':
        answer = (first - second)
        print(answer)
    elif operation == '/':
        answer = (first / second)
        print(answer)
    elif operation == '*':
        answer = (first * second)
        print(answer)
    elif operation not in ('+', '-', '/', '*', 'mod', 'pow', 'div'):
        print('Введена невалидная операция')

calculation()