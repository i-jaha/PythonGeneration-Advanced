'''Умножение матриц 🌶️
Напишите программу, которая перемножает две матрицы.

На вход программе подаются два натуральных числа n и m – 
количество строк и столбцов в первой матрице, 
затем элементы первой матрицы, 
затем пустая строка. 
Далее следуют числа m и k – 
количество строк и столбцов второй матрицы, 
затем элементы второй матрицы.

Программа должна вывести результирующую матрицу, 
разделяя элементы символом пробела.
'''

n, m = [int(i) for i in input().split()]
matrix_1 = [[int(i) for i in input().split()] for _ in range(n)]
input()
m2, k = [int(i) for i in input().split()]
matrix_2 = [[int(i) for i in input().split()] for _ in range(m2)]

if m == m2:
    matrix_3 = [[0 for _ in range(k)] for _ in range(n)]
    for i in range(n):
        for j in range(k):
            for r in range(m):
                matrix_3[i][j] += matrix_1[i][r] * matrix_2[r][j]
    for row in matrix_3:
        print(*row)
else:
    print("Невозможно перемножить: несовпадение размерностей.")