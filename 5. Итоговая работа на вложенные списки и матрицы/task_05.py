'''Симметричная матрица
Напишите программу проверки симметричности квадратной матрицы 
относительно побочной диагонали.

На вход программе подаётся натуральное число n — 
количество строк и столбцов в матрице, затем элементы матрицы.

Программа должна вывести YES, 
если матрица симметрична, 
и слово NO в противном случае.
'''

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
symmetric = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n - 1 - j][n - 1 - i]:
            symmetric = False
            break
    if not symmetric:
        break

print("YES" if symmetric else "NO")