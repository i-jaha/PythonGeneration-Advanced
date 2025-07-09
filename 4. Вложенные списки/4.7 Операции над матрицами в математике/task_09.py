'''Сложение матриц
Напишите программу для вычисления суммы двух матриц.
На вход программе подаются два натуральных числа n и m – 
количество строк и столбцов в матрицах, 
затем элементы первой матрицы, 
затем пустая строка, 
далее следуют элементы второй матрицы.

Программа должна вывести результирующую матрицу, 
разделяя элементы символом пробела.
'''

nums = [int(i) for i in input().split()]
n, m = nums[0], nums[1]
matrix_1 = [[int(i) for i in input().split()] for _ in range(n)]
input()
matrix_2 = [[int(i) for i in input().split()] for _ in range(n)]
matrix_3 = [[0 for _ in range(m)] for _ in range(n)]

for row in range(n):
    for col in range(m):
        matrix_3[row][col] = matrix_1[row][col] + matrix_2[row][col]

for row in matrix_3:
    print(*row)