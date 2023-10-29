'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк.
После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов
первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
Sample Input 1:
9 5 3
0 7 -1
-5 2 9
end
Sample Output 1:
3 21 22
10 6 19
20 16 -1

Sample Input 2:
1
end
Sample Output 2:
4
'''

matrix1 = []
matrix2 = []
matrix3 = []
x = 0
'''заполняю матрицу строковыми значениями и триггерюсь на 'end', чтобы завершить ввод'''
while True:
    mat = [i for i in input().split()]
    if 'end' in mat:
        break
    matrix1.append(mat)
    x += 1
'''преобразую строковую матрицу в числовую'''
for i in range(x):
    newMat = []
    for j in range(len(matrix1[0])):
        newMat.append(int(matrix1[i][j]))
    matrix2.append(newMat)
'''
отдельно расписал для граничных значений (i[max],j[min]) - элемент слева внизу,
(i[min], j[max]) - элемент справа вверху,
(i[max], j[max]) - элемент справа внизу
вычисления 
и общий кейс, когда (i, j) не в углах, сюда же подходит случай (i[min], j[min]) - элемент слева вверху
плюс этим же закрывается кейс, когда матрица состоит из 1 столбца/колонки или 1 элемента
'''
for i in range(x):
    newnewMat = []
    for j in range(len(matrix1[0])):
        if (i < (x-1)) and (j < (len(matrix1[0])-1)):
            newnewMat.append(matrix2[i-1][j] + matrix2[i+1][j] + matrix2[i][j-1] + matrix2[i][j+1])
        elif j == (len(matrix1[0]) - 1) and i < (x - 1):
            newnewMat.append(matrix2[i][0] + matrix2[i][j-1] + matrix2[i-1][j] + matrix2[i+1][j])
        elif i == (x - 1) and (j < (len(matrix1[0])-1)):
            newnewMat.append(matrix2[i][j+1] + matrix2[i][j - 1] + matrix2[i-1][j] + matrix2[0][j])
        elif i == (x - 1) and (j == (len(matrix1[0]) - 1)):
            newnewMat.append(matrix2[i][j-1] + matrix2[i][0] + matrix2[i - 1][j] + matrix2[0][j])
        # else:
        #     newnewMat.append(matrix2[i][0] + matrix2[i][j-1] + matrix2[0][j] + matrix2[i-1][j])
    matrix3.append(newnewMat)
for i in range(x):
    for j in range(len(matrix3[0])):
        print(matrix3[i][j], end = ' ')
    print()

''' [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [3, 3, 3]'''