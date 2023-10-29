'''
Игра сапер. Даны размеры поля для игры в сапер и координаты мин, стоящих на этом поле. Вывести поле игры на экран.
'''

n, m, k = [int(i) for i in input().split()] # n - строки, m - столбцы, k - число мин
a = [[0 for j in range(m)]for i in range(n)] # генерируем двумерный список (матрицу), состоящую из 0
for i in range(k): # теперь для введенного количества мин k вводим координаты мин в матрице a
    row, col = [int(i) - 1 for i in input().split()] # так как элементы в коде начинаются с 0, а обычно вводят цифры,
#                                                      опираясь на обычные числовые последовательности, начинающиеся с 1
    a[row][col] = -1 # тут ставим в ячейку матрицы по введенным координатам мину = -1
for i in range(n): # перебираем строки
    for j in range(m): # перебираем столбцы
        if a[i][j] == 0: # проверяем, что в ячейке нет мины (мина это -1, а 0 - нет мины)
# дальше перебираем соседние клетки на наличие мин (по диагонали и сверху, снизу, справа, слева)
            for di in range(-1, 2): # тут перебираем построчно
                for dj in range(-1, 2): # тут перебираем по столбцам
                    ai = i - di # координата ячейки по горизонтали
                    aj = j - dj # координата ячейки по вертикали (ai, aj)
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1: # проверяем, что соседняя ячейка есть в матрице
#                                                                         и что в ячейке есть мина = -1
                        a[i][j] += 1 # если в соседних ячейках есть мина, то прибавляем к значению ячейки единицу
for i in range(n): # теперь отрисовываем поле, тут идем по строкам
    for j in range(m): # тут идем по столбцам
        if a[i][j] == -1: # проверяем, что элемент матрицы равен -1, то есть мина
            print('*', end = '\t') # выводим мину и в конце добавляем табуляцию, чтобы не переходить на другую строку
        elif a[i][j] == 0: # проверяем, что элемент матрицы равен 0, то есть мин нет
            print('.', end = '\t') # выводим точку (нет мин) и в конце добавляем табуляцию
        else: # во всех других случаях
            print(a[i][j], end = '\t') # выводим число мин, с которыми граничит ячейка
    print()
