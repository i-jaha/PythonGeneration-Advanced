'''Транспонирование матрицы
Напишите программу, которая транспонирует квадратную матрицу.

На вход программе подаётся натуральное число n — 
количество строк и столбцов в матрице, затем элементы матрицы.

Программа должна вывести транспонированную матрицу.

Примечание 1. 
Транспонированная матрица — матрица, 
полученная из исходной матрицы заменой строк на столбцы.

Примечание 2. 
Задачу можно решить без использования вспомогательного списка. 
'''

# review 1
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
result = [[0 for _ in range(n)] for _ in range(n)]

for row in range(n):
    for col in range(n):
        result[row][col] = matrix[col][row]

for row in result:
    print(*row)




# review 2
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    print(*row)