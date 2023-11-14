def generate_spiral_matrix(n):
    # Создаем пустую матрицу размером n x n
    matrix = [[0] * n for _ in range(n)]

    # Задаем начальные значения
    num = 1
    row_start, row_end, col_start, col_end = 0, n - 1, 0, n - 1

    while row_start <= row_end and col_start <= col_end:
        # Заполняем верхнюю строку
        for i in range(col_start, col_end + 1):
            matrix[row_start][i] = num
            num += 1
        row_start += 1

        # Заполняем правый столбец
        for i in range(row_start, row_end + 1):
            matrix[i][col_end] = num
            num += 1
        col_end -= 1

        # Заполняем нижнюю строку
        if row_start <= row_end:
            for i in range(col_end, col_start - 1, -1):
                matrix[row_end][i] = num
                num += 1
            row_end -= 1

        # Заполняем левый столбец
        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                matrix[i][col_start] = num
                num += 1
            col_start += 1

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Пример использования
n = int(input("Введите размерность n: "))
spiral_matrix = generate_spiral_matrix(n)
print_matrix(spiral_matrix)