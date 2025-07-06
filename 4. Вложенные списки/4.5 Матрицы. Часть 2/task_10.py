'''
Магический квадрат ✨🌶️

Магическим квадратом порядка n называется квадратная таблица 
размера n×n, составленная из всех чисел 1,2,3, …, n^2 так, 
что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей 
равны между собой. 
Напишите программу, которая проверяет, 
является ли заданная квадратная матрица магическим квадратом.

На вход программе подается натуральное число n – 
количество строк и столбцов в матрице, 
затем элементы матрицы: 
n строк, по n чисел в каждой, разделенные пробелами.

Программа должна вывести YES, 
если матрица является магическим квадратом, 
или NO в противном случае.
'''

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

all_numbers = []
for row in matrix:
    for num in row:
        all_numbers.append(num)

right_list = list(range(1, n * n + 1))

if sorted(all_numbers) != right_list:
    print("NO")
else:
    target = sum(matrix[0])

    rows_ok = True
    for row in matrix:
        if sum(row) != target:
            rows_ok = False
            break

    cols_ok = True
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += matrix[i][j]
        if col_sum != target:
            cols_ok = False
            break

    diag1_sum = 0
    diag2_sum = 0
    for i in range(n):
        diag1_sum += matrix[i][i]
        diag2_sum += matrix[i][n - 1 - i]
    diag1 = diag1_sum == target
    diag2 = diag2_sum == target

    if rows_ok and cols_ok and diag1 and diag2:
        print("YES")
    else:
        print("NO")