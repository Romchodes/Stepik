'''
Цикл For и функция range
range(0, to, 1) параметры по-умолчанию, первый элемент 0, второй элемент по-умолчанию не задан всегда, шаг 1
'''

for i in 2, 3, 4:
    print(i*i)
print('---------')

for i in range(10): # Тут числа 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    print(i*i, end = ' ')
print('\n---------')

for i in range(5):
    print(i, end = ' ')
print('\n---------')

for i in range(2,5):
    print(i, end = ' ')
print('\n---------')

for i in range(2,15,4):
    print(i, end = ' ')
print('\n---------')

for i in range(5+1):
    print(i, end = ' ')
print('\n---------')

'''
Вывести квадрат из звездочек, сторона которого равна количеству звездочек, введенных пользователем
'''
n = int(input('Введите число звездочек: '))
for i in range(n):
    print(n * '*')

n = int(input('Введите число звездочек: '))
for i in range(n):
    for j in range(n):
        print('*', end = '')
    print()