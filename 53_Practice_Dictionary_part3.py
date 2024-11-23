'''
Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел, которые нужно считать.
Далее считывает n строк с числами x[i],
по одному числу в каждой строке. Итого будет n+1 строк.

При считывании числа x[i] программа должна на отдельной строке вывести значение f(x[i])).
Функция f(x) уже реализована и доступна для вызова.

Функция вычисляется достаточно долго и зависит только от переданного аргумента x.
Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.

Sample Input:
5
5
12
9
20
12

Sample Output:
11
41
47
61
41
'''

def f(x): # рандомная функция, чтобы вызвать ее при выполнении основной функции (так как в условиях f(x) определена)
    f = x - 1
    return f
#  в 2-х вариантах ниже представлены долгие решения,
#  так как при вводе одинаковых значений снова тратится время на вычисление значений функции для этих значений

# def functionN():
#     n = int(input())
#     l = []
#     for i in range(n):
#         inp = int(input())
#         l.append(inp)
#     for x in l:
#         print(f(x))
#
# functionN()

# def functionN():
#     n = int(input())
#     l = {}
#     u = 0
#     for i in range(n):
#         inp = int(input())
#         l[u] = inp
#         u += 1
#     for x in l.values():
#         print(f(x))
#
# functionN()

def functionN():
    n = int(input())
    l = {}
    for i in range(n):
        inp = int(input())
        if inp in l:
            print(l[inp])
            continue
        l[inp] = f(inp)
        print(l[inp])

functionN()

'''
Еще вариант решения
def functionN():
    n = int(input())
    l = {}
    for i in range(n):
        inp = int(input())
        if inp not in l:
            l[inp] = f(inp)
        print(l[inp])

functionN()
'''