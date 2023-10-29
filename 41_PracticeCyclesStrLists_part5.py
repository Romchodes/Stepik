'''
Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
Sample Input:
5

Sample Output:
1   2   3   4   5
16  17  18  19  6
15  24  25  20  7
14  23  22  21  8
13  12  11  10  9
'''

n = int(input())
mat = [[0 for j in range(n)] for i in range(n)]
sqr = n * n
num = 1
mati = 0
matj = 0
xi = 0
dopn = 2
r = -1
fstr = 0
min = -1
while num < sqr+1:
    for matj in range(xi, n-fstr):
        mat[mati][matj] = num
        num += 1
    xi += 1
    for mati in range(xi, n-fstr):
        mat[mati][matj] = num
        num += 1
    fstr += 1
    for matj in range(n-dopn, r, -1):
        mat[mati][matj] = num
        num += 1
    r += 1
    for mati in range(n-dopn, r, -1):
        mat[mati][matj] = num
        num += 1
    dopn += 1
    min += 1
for i in range(n):
    print(*mat[i], end = '\n')