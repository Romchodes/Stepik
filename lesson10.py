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



def calculation():
    while True:
        first = float(input('Введите первое число: '))
        second = float(input('Введите второе число: '))
        operation = input('Введите одну из операций (+, -, /, *, mod, pow, div): ')
        if second == 0 and (operation == '/' or operation == 'mod' or operation == 'div'): # можно operation in ('/', 'mod', 'div')
            print('Деление на 0!')
        elif operation == 'mod':
            answer = (first % second)
            print('Остаток от деления равен: ', answer)
        elif operation == 'pow':
            answer = (first ** second)
            print('Первое число в степени, равной второму числу, равно: ', answer)
        elif operation == 'div':
            answer = (first // second)
            print('Целочесленное деление первого числа на второе равно: ', answer)
        elif operation == '+':
            answer = (first + second)
            print('Сумма двух чисел равна: ', answer)
        elif operation == '-':
            answer = (first - second)
            print('Разность двух чисел равна: ', answer)
        elif operation == '/':
            answer = (first / second)
            print('Частное двух чисел равна: ', answer)
        elif operation == '*':
            answer = (first * second)
            print('Произведение двух чисел равно: ', answer)
        elif operation not in ('+', '-', '/', '*', 'mod', 'pow', 'div'):
            print('Введена невалидная операция')
        elif type(first) not in (float, int) or type(second) not in (float, int):
            print('Введено невалидное число')

calculation()